from odoo import models, fields, api, exceptions
import logging

class TodoTask(models.Model):
    _inherit = 'todo.task'

    effort_estimate = fields.Integer(string="Time Estimation")
    tag_ids = fields.Many2many('todo.task.tag', string="Tags")