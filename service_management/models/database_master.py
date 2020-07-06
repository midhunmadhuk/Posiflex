# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools

class PurchaseDatabase(models.Model):
    _name = 'purchase.database'
    
    name = fields.Char('Serial No.')
    product_categ_id = fields.Many2one('product.category', 'Product/Comp')
    product_id = fields.Many2one('product.template', 'Product No.')
    product_desc = fields.Char('Product Desc')
    product_variant_id = fields.Many2one('product.product', string="Variant")
    war_in_months = fields.Float('War In Months')
    war_start_dt = fields.Date('War Start Date')
    war_end_dt = fields.Date('War End Date')
    from_entity_type = fields.Selection([('vendor', 'Vendor'), ('warehouse', 'Warehouse'), ('partner', 'Partner'), ('customer', 'Customer')], string="From Entity Type")
    partner_id_1 = fields.Many2one('res.partner', 'From Entity Name')
    partner_id_2 = fields.Many2one('res.partner', 'From Entity Name')
    partner_id_3 = fields.Many2one('res.partner', 'From Entity Name')
    location_id = fields.Many2one('stock.location', 'Warehouse')
    to_entity_type = fields.Selection([('vendor', 'Vendor'), ('warehouse', 'Warehouse'), ('partner', 'Partner'), ('customer', 'Customer')], string="To Entity Type")
    to_partner_id_1 = fields.Many2one('res.partner', 'To Entity Name')
    to_partner_id_2 = fields.Many2one('res.partner', 'To Entity Name')
    to_partner_id_3 = fields.Many2one('res.partner', 'To Entity Name')
    to_location_id = fields.Many2one('stock.location', 'Warehouse')
    reference_id = fields.Char('Reference ID')
    reference_date = fields.Date('Reference Date')
    inv_trans_name = fields.Char('Inv Trans Name')
    inv_trans_id = fields.Char('Inv Trans ID')
    inv_trans_created_date = fields.Date('Inv Trans Created Date')
    inv_logged_date = fields.Date('Inv Trans Logged Date')

class SalesDatabase(models.Model):
    _name = 'sales.database'
    
    name = fields.Char('Serial No.')
    product_categ_id = fields.Many2one('product.category', 'Product/Comp')
    product_id = fields.Many2one('product.template', 'Product No.')
    product_desc = fields.Char('Product Desc')
    product_variant_id = fields.Many2one('product.product', string="Variant")
    war_in_months = fields.Float('War In Months')
    war_start_dt = fields.Date('War Start Date')
    war_end_dt = fields.Date('War End Date')
    from_entity_type = fields.Selection([('vendor', 'Vendor'), ('warehouse', 'Warehouse'), ('partner', 'Partner'), ('customer', 'Customer')], string="From Entity Type")
    partner_id_1 = fields.Many2one('res.partner', 'Vendor')
    partner_id_2 = fields.Many2one('res.partner', 'Customer')
    partner_id_3 = fields.Many2one('res.partner', 'Partner')
    location_id = fields.Many2one('stock.location', 'Warehouse')
    to_entity_type = fields.Selection([('vendor', 'Vendor'), ('warehouse', 'Warehouse'), ('partner', 'Partner'), ('customer', 'Customer')], string="To Entity Type")
    to_partner_id_1 = fields.Many2one('res.partner', 'Vendor')
    to_partner_id_2 = fields.Many2one('res.partner', 'Customer')
    to_partner_id_3 = fields.Many2one('res.partner', 'Partner')
    to_location_id = fields.Many2one('stock.location', 'Warehouse')
    reference_id = fields.Char('Reference ID')
    reference_date = fields.Date('Reference Date')
    inv_trans_name = fields.Char('Inv Trans Name')
    inv_trans_id = fields.Char('Inv Trans ID')
    inv_trans_created_date = fields.Date('Inv Trans Created Date')
    inv_logged_date = fields.Date('Inv Trans Logged Date')
    
class AmcDatabase(models.Model):
    _name = 'amc.database'
    
    name = fields.Char('Serial No.')
    product_categ_id = fields.Many2one('product.category', 'Product/Comp')
    product_id = fields.Many2one('product.template','Product No.')
    product_desc = fields.Char('Product Desc')
    product_variant_id = fields.Many2one('product.product', string="Variant")
    from_entity_type = fields.Selection([('vendor', 'Vendor'), ('warehouse', 'Warehouse'), ('partner', 'Partner'), ('customer', 'Customer')], string="From Entity Type")
    partner_id_1 = fields.Many2one('res.partner', 'From Entity Name')
    partner_id_2 = fields.Many2one('res.partner', 'From Entity Name')
    partner_id_3 = fields.Many2one('res.partner', 'From Entity Name')
    location_id = fields.Many2one('stock.location', 'Warehouse')
    to_entity_type = fields.Selection([('vendor', 'Vendor'), ('warehouse', 'Warehouse'), ('partner', 'Partner'), ('customer', 'Customer')], default='customer', string="To Entity Type")
    to_partner_id_1 = fields.Many2one('res.partner', 'To Entity Name')
    to_partner_id_2 = fields.Many2one('res.partner', 'To Entity Name')
    to_partner_id_3 = fields.Many2one('res.partner', 'To Entity Name')
    to_location_id = fields.Many2one('stock.location', 'Warehouse')
#     partner_id = fields.Many2one('res.partner', 'Customer')
    amc_inv_no = fields.Char('AMC Invoice No.')
    amc_inv_date = fields.Date('AMC Invoice Date')
    amc_duration = fields.Float('AMC Duration')
    amc_start_date = fields.Date('AMC Start Date')
    amc_end_date = fields.Date('AMC End Date')
    amc_active = fields.Char('AMC Active')
    amc_type = fields.Char('AMC Type')
    amc_agreement_no = fields.Char('AMC Agreement No.')
    amc_notes = fields.Char('AMC Notes')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    