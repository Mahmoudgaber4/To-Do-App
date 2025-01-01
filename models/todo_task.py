from odoo import models, fields, api
from  odoo.exceptions import ValidationError
class TodoTask(models.Model):
    _name = "todo.task"
    _description = "To-Do Task"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    task_name = fields.Char(string="Task Name", size=15, default='New')
    assign_to = fields.Many2one('res.partner', string="Assign To", required=1)
    description = fields.Text(string="Description")
    due_date = fields.Date(string="Due Date", tracking=1)
    is_late = fields.Boolean()
    estimated_time = fields.Float(string="Estimated Time (hours)")
    line_ids = fields.One2many('task.line', 'task_id')
    total_time = fields.Float(compute="_compute_total_time", store=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed')
    ], default='new', tracking=1)

    _sql_constraints = [
        ('unique_task_name', 'unique(task_name)', 'this name is exist')
    ]

    def check_passed_due_date(self):
        task_ids = self.search([
            ('state', 'in', ['new', 'in_progress']),
            ('due_date', '>', fields.date.today())
        ])
        for rec in task_ids:
            rec.is_late = True


    def action_new(self):
        for rec in self:
            rec.write({
                'state': 'new'
            })
    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'
    def action_completed(self):
        for rec in self:
            rec.write({
                'state': 'completed'
            })

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

    @api.depends("line_ids.time")
    def _compute_total_time(self):
        for rec in self:
            rec.total_time = sum(rec.line_ids.mapped('time'))
    @api.constrains('estimated_time', 'total_time')
    def _check_total_time(self):
        for rec in self:
            if rec.total_time > rec.estimated_time:
                raise ValidationError("total time recorded cannot exceed estimated time")


class task_line(models.Model):
    _name = "task.line"

    task_id = fields.Many2one("todo.task")
    date = fields.Date(string="Date")
    description = fields.Char(string="Description")
    time = fields.Float(string="Time (hours)")

