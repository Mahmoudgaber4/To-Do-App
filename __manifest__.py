{
    "name": "To-Do App",
    "summary": "Manage your tasks here",
    "Category": "Eduction",
    "auther": "Mahmoud Gaber",
    "version": "17.0",
    "license": 'OPL-1',
    "depends": ['base', 'mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'reports/task_report.xml',
    ],
    "assets": {
      'web.assets_backend': ['todo_management/static/src/todo_task.css'],
    },
    "application": True,
}
