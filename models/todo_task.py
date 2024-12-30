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
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='new', tracking=1)


    @api.constrains('due_date')
    def _passed_due_date(self):
        today_date = fields.Date.today()
        for rec in self:
            if today_date.day > rec.due_date.day:
                raise ValidationError('You passed date of your task ')

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

