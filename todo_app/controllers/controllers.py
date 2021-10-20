# -*- coding: utf-8 -*-
# from odoo import http


# class .\odoo-dev\todoApp(http.Controller):
#     @http.route('/.\odoo-dev\todo_app/.\odoo-dev\todo_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\odoo-dev\todo_app/.\odoo-dev\todo_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\odoo-dev\todo_app.listing', {
#             'root': '/.\odoo-dev\todo_app/.\odoo-dev\todo_app',
#             'objects': http.request.env['.\odoo-dev\todo_app..\odoo-dev\todo_app'].search([]),
#         })

#     @http.route('/.\odoo-dev\todo_app/.\odoo-dev\todo_app/objects/<model(".\odoo-dev\todo_app..\odoo-dev\todo_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\odoo-dev\todo_app.object', {
#             'object': obj
#         })
