# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_template_contract(models.Model):
    _inherit = 'product.template'
    consider_contract = fields.Boolean(help="Suma el total de toneladas en los contratos", string="Considerar para contrato")
