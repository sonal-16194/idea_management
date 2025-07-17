# -*- coding: utf-8 -*-
# from odoo import http


# class IdeaManagement(http.Controller):
#     @http.route('/idea_management/idea_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/idea_management/idea_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('idea_management.listing', {
#             'root': '/idea_management/idea_management',
#             'objects': http.request.env['idea_management.idea_management'].search([]),
#         })

#     @http.route('/idea_management/idea_management/objects/<model("idea_management.idea_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('idea_management.object', {
#             'object': obj
#         })

