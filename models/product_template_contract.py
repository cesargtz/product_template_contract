# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from openerp.exceptions import ValidationError

class product_template_contract(models.Model):
    _inherit = 'product.template'

    consider_contract = fields.Boolean(help="Suma el total de toneladas en los contratos", string="Para contrato")
    calculate_cost = fields.Boolean(help="Incluye el producto para el calculo de costos.", string="Para costo.")
    sum_tons_cost= fields.Boolean(help="Incluye el producto para el calculo de costos.", string="Considerar toneladas para costo.")
    updated_day = fields.Datetime(readonly=True)
    initial_inventory_tn = fields.Float(readonly=True)
    initial_inventory_import = fields.Float(readonly=True)
    initial_import = fields.Float()
    initial_tons = fields.Float()
    initial_year = fields.Date()

    @api.one
    @api.constrains('sum_tons_cost')
    def _check_field(self):
        exisist = self.env['product.template'].search([('sum_tons_cost', '=', 'True')])
        if len(exisist) > 1:
            raise exceptions.ValidationError("Solo puedes tener un producto para consider el calculo de toneladas")
