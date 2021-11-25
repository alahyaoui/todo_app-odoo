from odoo import models, fields, api, exceptions
import logging


class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'

    name = fields.Char(string="Tag name")
    task_ids = fields.Many2many('todo.task', string='Task')
