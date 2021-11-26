from odoo import models, fields, api, exceptions
import logging


class TodoTask(models.Model):
    _inherit = 'todo.task'

    effort_estimate = fields.Integer(string="Time Estimation")
    desc = fields.Char(string="Brief Description")
    state = fields.Selection([('draft', 'Not Ready'), ('open', 'Ready'), ('done', 'Ended')], string="State",
                             default='draft')
    docs = fields.Html(string="Detailed Documentation")
    date_created = fields.Datetime(string="Creation Date and Time", default=lambda self: fields.datetime.now())
    image = fields.Binary('Task Image')
    tag_ids = fields.Many2many('todo.task.tag', string="Tags")

    def do_open(self):
        self.state = 'open'

    def do_close(self):
        self.state = 'done'

    def do_reset(self):
        self.state = 'draft'

    @api.onchange('user_id')
    def _on_change_responsible(self):
        self.team_ids = None
        return {
            'warning': {
                'title': 'Responsible User Reset',
                'message': 'Please choose a new Team.',
                'type': 'notification'
            }
        }
