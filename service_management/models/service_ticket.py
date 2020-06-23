# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import threading

from odoo import api, fields, models, tools

_logger = logging.getLogger(__name__)

class CallWiseHistory(models.Model):
    _name = "call.wise.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Char('Serial No.')
    prob_code = fields.Char('PROB Code')
    action_code = fields.Char('Action Code')
    status = fields.Char('Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class SerialWiseHistory(models.Model):
    _name = "serial.wise.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Char('Serial No.')
    prob_code = fields.Char('PROB Code')
    action_code = fields.Char('Action Code')
    status = fields.Char('Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class ActivityDetails(models.Model):
    _name = "activity.details"
    
    name = fields.Char('Activity Type')
    time = fields.Float(string='Time')
    engineer_id = fields.Many2one('res.partner', 'Engineer')
    action_code = fields.Char('Action Code')
    action_desc = fields.Char('Action Description')
    status = fields.Char('Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class SparesDetails(models.Model):
    _name = "spares.details"
    
    name = fields.Char('Description')
    item_no = fields.Char('Item No.')
    serial_no = fields.Char('Serial No.')
    billable = fields.Boolean('Billable')
    war_in_months = fields.Float('Warranty In Months')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class SlaDetails(models.Model):
    _name = "sla.details"

    name = fields.Char('Call Type')
    customer_loc = fields.Char('Customer Location')
    tat_in_hours = fields.Float('TAT(Hr)')
    tat_achieved = fields.Float('Tat Achieved(Hr)')
    sla_met = fields.Selection([('yes','Yes'), ('no', 'No')], string="SLA Met")
    service_id = fields.Many2one('service.order', 'Service Order')
    
    

class ServiceOrder(models.Model):
    _name = 'service.order'
    _description = 'Service Order'
    _rec_name = 'name'
    _order = 'id DESC'
    
    name = fields.Char('Call Ticket No.')
    company_id =  fields.Many2one('res.company', 'Company')
    call_date = fields.Datetime('Call Date')
    call_type = fields.Char('Call Type')
    status = fields.Char('Status')
    sub_status = fields.Char('Sub Status')
    serial_no = fields.Char('Serial No.')
    product_id = fields.Many2one('product.template','Product')
    ptav_product_variant_ids = fields.Many2many('product.product', string="Related Variants")
    product_no = fields.Char('Product No.')
    customer_id = fields.Many2one('res.partner', 'Customer')
    customer_type = fields.Char('Customer Type')
    mobile = fields.Char('Mobile')
    email = fields.Char('Email')
    address = fields.Char('Address')
    purchase_date = fields.Date('Purchase Date')
    proof_of_purchase = fields.Char('Proof of Purchase')
    war_in_months = fields.Float('WAR In Months')
    war_balance = fields.Float('WAR Balance')
    war_status = fields.Char('WAR Status')
    amc_status = fields.Char('AMC Status')
    zone = fields.Selection([('north','North'),('south','South'),('east', 'East'),('west','West')], string='Zone')
    state_id = fields.Many2one('res.country.state', 'State')
    rm = fields.Char('RM')
    engineer_id = fields.Many2one('res.partner', 'Engineer')
    partner_group_id = fields.Many2one('res.partner', 'Partner Group')
    partner_name_id = fields.Many2one('res.partner', 'Partner Name')
    problem_code = fields.Char('Problem Code')
    problem_desc = fields.Char('Problem Description')
    closed_date = fields.Date('Closed Date')
    closure_desc = fields.Char('Closure Description')
    call_history_ids = fields.One2many('call.wise.history', 'service_id', string='Customer Wise Call History')
    serial_history_ids = fields.One2many('serial.wise.history', 'service_id', string='Serial Wise Call History')
    activity_ids = fields.One2many('activity.details', 'service_id', string='Activities')
    spares_details_ids = fields.One2many('spares.details', 'service_id', string='Spares Info')
    sla_details_ids = fields.One2many('sla.details', 'service_id', string='SLA Info')
    

    
    
    
    
    
    
    