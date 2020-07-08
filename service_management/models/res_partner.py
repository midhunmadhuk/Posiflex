# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools

class Respartner(models.Model):
    _inherit = 'res.partner'
    
    is_partner = fields.Boolean('Is Partner')
    partner_type_id = fields.Many2one('partner.type', 'Partner Type')
    customer_type = fields.Many2one('customer.type', 'Customer Type')
    partner_location = fields.Many2one('stock.location', 'Partner Location')
    
class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    is_branch = fields.Boolean('Branch')
    branch_location_id = fields.Many2one('stock.location', 'Branch Location')
    is_service_engineer = fields.Boolean('Service Engineer')
    engineer_location_id = fields.Many2one('stock.location', 'Engineer Location')
    
class StockMove(models.Model):
    _inherit = 'stock.move'
    
    lot_id = fields.Many2one('stock.production.lot', 'Lot')