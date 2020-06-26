# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools


class CallWiseHistory(models.Model):
    _name = "call.wise.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Many2one('serial.no.master', 'Serial No.')
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
    serial_no = fields.Many2one('serial.no.master', 'Serial No.')
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
    
    @api.onchange('product_id')
    def onchage_product(self):
        self.product_no = self.product_id.default_code
        
    @api.onchange('customer_id')
    def onchange_customer(self):
        if self.customer_id:
            self.street = self.customer_id.street
            self.street2 = self.customer_id.street2
            self.city = self.customer_id.city
            self.state_id = self.customer_id.state_id  or False
            self.country_id = self.customer_id.country_id  or False
            self.customer_type = self.customer_id.customer_type
            self.mobile = self.customer_id.mobile
            self.email = self.customer_id.email
            self.call_history_ids.unlink()
            customer_orders = self.env['service.order'].search([('customer_id', '=', self.customer_id.id)])
            customer_call_data = []
            for customer_order in customer_orders:
                call_history = {
                        'customer_id': customer_order.customer_id and customer_order.customer_id.id or False,
                        'call_tkt_no': customer_order.name,
                        'product': customer_order.product_id and customer_order.product_id.id or False,
                        'serial_no': customer_order.serial_no and customer_order.serial_no.id or False,
                        'prob_code_id': customer_order.problem_code and customer_order.problem_code.id or False,
                        'action_code_id': customer_order.last_activity_id and customer_order.last_activity_id.action_code and customer_order.last_activity_id.action_code.id or False,
                        'status_id': customer_order.status and customer_order.status.id or False
                    }
                customer_call_data.append((0,0, call_history))
            self.call_history_ids = customer_call_data
        
    @api.onchange('serial_no')
    def onchange_serial(self):
        if self.serial_no:
            self.product_id = self.serial_no.product_id or False
            self.product_no = self.serial_no.product_id and self.serial_no.product_id.default_code or False
            if self.serial_no.avail_entity_type == "customer":
                self.customer_id = self.serial_no.customer_id
            else:
                self.partner_name_id = self.serial_no.partner_id
            self.war_in_months = self.serial_no.war_in_months
            self.war_start_date = self.serial_no.war_start_dt
            self.war_end_date = self.serial_no.war_end_dt
            self.war_balance = self.serial_no.war_balance
            self.war_status = self.serial_no.war_status
            serial_wise_orders = self.env['service.order'].search([('serial_no', '=', self.serial_no.id)])
            serial_wise_data = []
            self.serial_history_ids.unlink()
            for serial_wise_order in serial_wise_orders:
                serial_history = {
                        'customer_id': serial_wise_order.customer_id and serial_wise_order.customer_id.id or False,
                        'call_tkt_no': serial_wise_order.name,
                        'product': serial_wise_order.product_id and serial_wise_order.product_id.id or False,
                        'serial_no': serial_wise_order.serial_no and serial_wise_order.serial_no.id or False,
                        'prob_code_id': serial_wise_order.problem_code and serial_wise_order.problem_code.id or False,
                        'action_code_id': serial_wise_order.last_activity_id and serial_wise_order.last_activity_id.action_code and serial_wise_order.last_activity_id.action_code.id or False,
                        'status_id': serial_wise_order.status and serial_wise_order.status.id or False
                    }
                serial_wise_data.append((0,0, serial_history))
            self.serial_history_ids = serial_wise_data
        
        
    name = fields.Char('Call Ticket No.', copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('service.order'))
    company_id =  fields.Many2one('res.company', 'Company',default=lambda self: self.env.user.company_id)
    call_date = fields.Datetime('Call Received Date')
    call_date_time = fields.Datetime('Call Created Date',default=lambda self: fields.Datetime.now())
    call_type = fields.Many2one('call.type', 'Call Type')
    status = fields.Many2one('status.info', compute='_check_last_activity', string='Status')
    sub_status = fields.Many2one('sub.status.info', compute='_check_last_activity',  string='Sub Status')
    customer_ref_no = fields.Char('Customer Ref No.')
    serial_no = fields.Many2one('serial.no.master', 'Serial No.')
    product_id = fields.Many2one('product.template','Product')
    ptav_product_variant_ids = fields.Many2many('product.product', string="Related Variants")
    product_no = fields.Char('Product No.')
    customer_id = fields.Many2one('res.partner', 'Customer')
    customer_type = fields.Many2one('customer.type', 'Customer Type')
    mobile = fields.Char('Mobile')
    email = fields.Char('Email')
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    purchase_date = fields.Date('Purchase Date')
    proof_of_purchase = fields.Boolean('Proof of Purchase Avl')
    war_in_months = fields.Float('WAR/AMC In Months')
    war_balance = fields.Float('WAR Balance')
    war_status = fields.Many2one('warranty.type', 'WAR/AMC Status')
    zone = fields.Selection([('north','North'),('south','South'),('east', 'East'),('west','West')], string='Service Zone')
    service_state_id = fields.Many2one('res.country.state', 'Service State')
    service_city = fields.Char('Service City')
    partner_type_id = fields.Many2one('partner.type', 'Partner Type')
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
    proof_of_purchase_avl = fields.Binary('Proof of Purchase Doc')
    war_latest_id = fields.Many2one('warranty.type', 'WAR/AMC Latest')
    war_start_date = fields.Datetime('WAR/AMC Start Date')
    war_end_date = fields.Datetime('WAR/AMC End Date')
    service_gm = fields.Many2one('hr.employee', 'Service GM')
    service_rm = fields.Many2one('hr.employee', 'Service RM')
    engineer_id = fields.Many2one('hr.employee', 'Service Engineer')
    product_categ_id = fields.Many2one('product.category', 'Product Category')
    online_support_id = fields.Many2one('res.users', 'Online Support')
    last_activity_id = fields.Many2one('activity.details', compute='_check_last_activity')
    
    @api.depends('activity_ids')
    def _check_last_activity(self):
        for service in self:
            if service.activity_ids:
                activity_recs = service.activity_ids
                service.last_activity_id = activity_recs[-1]
                service.status = activity_recs[-1].status_id
                service.sub_status = activity_recs[-1].sub_status_id
            else:
                service.last_activity_id = False
                service.status = False
                service.sub_status = False
                
    
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
    
    
    
    
    
    
    
    
    