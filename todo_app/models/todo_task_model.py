from odoo import models, fields, api, exceptions
import logging


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(string="Task name", required=True)
    is_done = fields.Boolean(string="Is done")
    active = fields.Boolean(string="Is active", default=True)
    date_deadline = fields.Date(string="Deadline date")

    # Demander au prof
    user_id = fields.Many2one('res.users', string="Responsible")  # Rajouter val par defaut
    teams_ids = fields.Many2many('res.partner', string="Team")

    _logger = logging.getLogger(__name__)

    def do_clear_done(self):
        for task in self:
            if task.active:
                self._logger.debug("Set active to False.")
                task.active = False
            else:
                raise exceptions.Warning("Task already inactive cannot be set to inactive.")

    def write(self, values):
        if 'active' not in values:
            self._logger.debug("Set active to True.")
            values['active'] = True
        return super(TodoTask, self).write(values)
