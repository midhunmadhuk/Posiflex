# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools


class CallWiseHistory(models.Model):
    _name = "call.wise.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Char('Serial No.')
    prob_code_id = fields.Many2one('problem.code', 'PROB Code')
    action_code_id = fields.Many2one('action.code', 'Action Code')
    status_id = fields.Many2one('status.info','Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class SerialWiseHistory(models.Model):
    _name = "serial.wise.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Char('Serial No.')
    prob_code_id = fields.Many2one('problem.code', 'PROB Code')
    action_code_id = fields.Many2one('action.code', 'Action Code')
    status_id = fields.Many2one('status.info','Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class ActivityDetails(models.Model):
    _name = "activity.details"
    
    name = fields.Char('Activity Type')
    time = fields.Float(string='Time')
    activity_type_id = fields.Many2one('activity.type', 'Activity Type')
    engineer_id = fields.Many2one('hr.employee', 'Engineer')
    partner_id = fields.Many2one('res.partner', 'Partner')
    action_code = fields.Many2one('action.code', 'Action Code')
    action_desc = fields.Char('Action Desc')
    action_remarks = fields.Char('Action Remarks')
    status_id = fields.Many2one('status.info','Status')
    sub_status_id = fields.Many2one('sub.status.info','Sub Status')
    spares_used = fields.Boolean('Spares Used')
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
    
    name = fields.Char('Call Ticket No.', copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('service.order'))
    company_id =  fields.Many2one('res.company', 'Company',default=lambda self: self.env.user.company_id)
    call_date = fields.Datetime('Call Reg Date')
    call_date_time = fields.Datetime('Call Reg Timestamp',default=lambda self: fields.Datetime.now())
    call_type = fields.Many2one('call.type', 'Call Type')
    status = fields.Many2one('status.info', 'Status')
    sub_status = fields.Many2one('sub.status.info', 'Sub Status')
    serial_no = fields.Char('Serial No.')
    product_id = fields.Many2one('product.template','Product')
    ptav_product_variant_ids = fields.Many2many('product.product', string="Related Variants")
    product_no = fields.Char('Product No.')
    customer_id = fields.Many2one('res.partner', 'Customer')
    customer_type = fields.Many2one('customer.type', 'Customer Type')
    mobile = fields.Char('Mobile')
    email = fields.Char('Email')
    address = fields.Char('Address')
    purchase_date = fields.Date('Purchase Date')
    proof_of_purchase = fields.Boolean('Proof of Purchase Avl')
    war_in_months = fields.Float('WAR/AMC In Months')
    war_balance = fields.Float('WAR Balance')
    war_status = fields.Many2one('warranty.type', 'WAR/AMC Status')
    zone = fields.Selection([('north','North'),('south','South'),('east', 'East'),('west','West')], string='Service Zone')
    state_id = fields.Many2one('res.country.state', 'Service State')
    city = fields.Char('Service City')
    partner_type_id = fields.Many2one('res.partner', 'Partner Type')
    partner_name_id = fields.Many2one('res.partner', 'Partner Name')
    problem_code = fields.Many2one('problem.code', 'Problem Code')
    problem_desc = fields.Char('Problem Description')
    call_remarks = fields.Char('Call Remarks')
    resolved_date = fields.Datetime('Resolved Date')
    closed_date = fields.Datetime('Closed Date')
    closure_desc = fields.Char('Closure Description')
    call_history_ids = fields.One2many('call.wise.history', 'service_id', string='Customer Wise Call History')
    serial_history_ids = fields.One2many('serial.wise.history', 'service_id', string='Serial Wise Call History')
    activity_ids = fields.One2many('activity.details', 'service_id', string='Activities')
    spares_details_ids = fields.One2many('spares.details', 'service_id', string='Spares Info')
    sla_details_ids = fields.One2many('sla.details', 'service_id', string='SLA Info')
    ##
    proof_of_purchase_avl = fields.Binary('Proof of Purchase Doc')
    war_latest_id = fields.Many2one('warranty.type', 'WAR/AMC Latest')
    war_start_date = fields.Datetime('WAR/AMC Start Date')
    war_end_date = fields.Datetime('WAR/AMC End Date')
    service_gm = fields.Many2one('hr.employee', 'Service GM')
    service_rm = fields.Many2one('hr.employee', 'Service RM')
    engineer_id = fields.Many2one('hr.employee', 'Service Engineer')
    product_categ_id = fields.Many2one('product.category', 'Product Category')
    
class SerialHistory(models.Model):
    _name = 'serial.history'
    
    name = fields.Char('Serial No.')
    product_id = fields.Many2one('product.template')
    service_id = fields.Many2one('service.order', 'Call Ticket')
    war_latest = fields.Many2one('warranty.type', 'WAR Latest')
    war_in_months = fields.Float('WAR In Months')
    war_start_dt = fields.Datetime('WAR Start Date')
    war_end_dt = fields.Datetime('WAR End Date')
    war_balance = fields.Float('WAR Balance')
    war_status_id = fields.Many2one('warranty.type', 'WAR Status')
    
    
    
    
    
    
    
    
    