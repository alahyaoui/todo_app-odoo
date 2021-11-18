from odoo import models, fields, api, exceptions
import logging


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(string="Task name", required=True)
    is_done = fields.Boolean(string="Is done", default=False)
    active = fields.Boolean(string="Is active", default=True)
    date_deadline = fields.Date(string="Deadline date")

    # Demander au prof
    user_id = fields.Many2one('res.users', string="Responsible")  # Rajouter val par defaut
    team_ids = fields.Many2many('res.partner', string="Team")

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

    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count([('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            copy_name = u"Copy of {}".format(self.name)
        else:
            copy_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = copy_name
        return super(TodoTask, self).copy(default)

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, is_done={self.is_done}, active={self.active}, data_deadline={self.date_deadline}, user_name={self.user_id.name}, team_count={len(self.team_ids)})"
