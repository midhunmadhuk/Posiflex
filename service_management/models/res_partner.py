# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools

class Respartner(models.Model):
    _inherit = 'res.partner'
    
    is_partner = fields.Boolean('Is Partner')
    partner_type_id = fields.Many2one('partner.type', 'Partner Type')
    customer_type = fields.Many2one('customer.type', 'Customer Type')
    partner_location = fields.Many2one('stock.location', 'Partner Location')