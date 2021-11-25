from odoo import models, fields, api, exceptions
import logging


class Tag(models.Model):
    _name = 'todo.task.tag'
    _inherit = 'todo.task'
    _description = 'To-do Tag'

    name = fields.Char(string="Tag name")
