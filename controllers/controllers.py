# -*- coding: utf-8 -*-
from odoo import http

# class ProductTemplateContract(http.Controller):
#     @http.route('/product_template_contract/product_template_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_template_contract/product_template_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_template_contract.listing', {
#             'root': '/product_template_contract/product_template_contract',
#             'objects': http.request.env['product_template_contract.product_template_contract'].search([]),
#         })

#     @http.route('/product_template_contract/product_template_contract/objects/<model("product_template_contract.product_template_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_template_contract.object', {
#             'object': obj
#         })