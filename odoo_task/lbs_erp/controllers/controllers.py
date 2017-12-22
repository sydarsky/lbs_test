# -*- coding: utf-8 -*-
from odoo import http

# class LbsErp(http.Controller):
#     @http.route('/lbs_erp/lbs_erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lbs_erp/lbs_erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lbs_erp.listing', {
#             'root': '/lbs_erp/lbs_erp',
#             'objects': http.request.env['lbs_erp.lbs_erp'].search([]),
#         })

#     @http.route('/lbs_erp/lbs_erp/objects/<model("lbs_erp.lbs_erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lbs_erp.object', {
#             'object': obj
#         })