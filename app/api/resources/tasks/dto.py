from flask_restx import Namespace, fields
from . import ns

class TaskDto:

    post_task = ns.model('post_task', {
        'title': fields.String(description = "Task title", required = True),
        'description': fields.String(description = "Task description", required = False),
        'user_id': fields.Integer(description = "User who the task belongs", required = True),
        'expiration_date': fields.Date(description = "Task expiration date", required = True),
        'status': fields.String(description = "Task current status", required = True),
        'priority': fields.String(description = "Task current priority", required = True),
        'active': fields.Boolean(description = "Task active status", required = True)
    })

    get_task = ns.model('get_task',{
        'title': fields.String(description = "Task title", required = True),
        'description': fields.String(description = "Task description", required = False),
        'user_id': fields.Integer(description = "User who the task belongs", required = True),
        'expiration_date': fields.Date(description = "Task expiration date", required = True),
        'status': fields.String(description = "Task current status", required = True),
        'priority': fields.String(description = "Task current priority", required = True),
        'active': fields.Boolean(description = "Task active status", required = True)
    })