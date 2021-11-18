from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(string="Task name", required=True)
    is_done = fields.Boolean(string="Is done")
    active = fields.Boolean(string="Is active", default=True)
    date_deadline = fields.Date(string="Deadline date")

    # Demander au prof
    user_id = fields.Many2one('res.users', string="Responsible")  # Rajouter val par defaut
    teams_ids = fields.Many2many('res.partner', string="Team")

    # description = fields.Text()

    def do_clear_done(self):
        # self.active = False
        # self.is_done = True
        self.write({'active': False})
        self.write({'is_done': True})
