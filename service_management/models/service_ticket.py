# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from dateutil import relativedelta

class SerialNoDB(models.Model):
    _name = 'serial.no.db'
     
    name = fields.Char('Serial No.')
    db_type = fields.Char('DB')
    entity_type = fields.Selection([('partner', 'Partner'), ('vendor', 'Vendor'), ('customer', 'Customer'), ('warehouse', 'Warehouse')], string="From Type")
    from_name = fields.Char('From Name')
    to_entity_type = fields.Selection([('partner', 'Partner'), ('vendor', 'Vendor'), ('customer', 'Customer'), ('warehouse', 'Warehouse')], string="From Type")
    to_name = fields.Char('To Name')
    sale_inv_no = fields.Char('Sale Invoice No.')
    sale_inv_date = fields.Date('Sale Invoice Date')
    war_in_months = fields.Float('WAR In Months')
    war_start_dt = fields.Datetime('WAR Start Date')
    war_end_dt = fields.Datetime('WAR End Date')
    service_id = fields.Many2one('service.order', 'Service Order')

class OpencallHistoy(models.Model):
    _name = "open.call.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Many2one('serial.no.master', 'Serial No.')
    prob_code_id = fields.Many2one('problem.code', 'PROB Code')
    action_code_id = fields.Many2one('action.code', 'Action Code')
    status_id = fields.Many2one('status.info','Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
class RepeatcallHistoy(models.Model):
    _name = "repeat.call.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Many2one('serial.no.master', 'Serial No.')
    prob_code_id = fields.Many2one('problem.code', 'PROB Code')
    action_code_id = fields.Many2one('action.code', 'Action Code')
    status_id = fields.Many2one('status.info','Status')
    service_id = fields.Many2one('service.order', 'Service Order')
    
    
class ReopenedCallHistory(models.Model):
    _name = "reopened.call.history"
    
    name = fields.Char('Name')
    customer_id = fields.Many2one('res.partner', 'Customer')
    call_tkt_no = fields.Char('Call Ticket No.')
    product = fields.Many2one('product.template', 'Product')
    serial_no = fields.Many2one('serial.no.master', 'Serial No.')
    prob_code_id = fields.Many2one('problem.code', 'PROB Code')
    action_code_id = fields.Many2one('action.code', 'Action Code')
    status_id = fields.Many2one('status.info','Status')
    service_id = fields.Many2one('service.order', 'Service Order')


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
    
    @api.onchange('user_type')
    def onchange_many2onefield(self):
        users = self.user_type.users.ids
        return {'domain': {'user_id': [('id', 'in', users)]}}
    
    name = fields.Many2one('activity.type','Activity Type')
    date = fields.Datetime('Activity Created Date')
    time = fields.Datetime(string='Activity Logged Date')
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
    diagnostic_id = fields.Many2one('diagnosis.code', 'Diagnostic Code')
    diagnostic_desc = fields.Char('Diagnostic Desc')
    user_type = fields.Many2one('res.groups', string='User Type')
    user_id = fields.Many2one('res.users', 'User Name')
    location_filter_id = fields.Many2one('stock.location', 'Location')
    serial_no_filter = fields.Many2one('stock.production.lot', 'Serial Number')
    spare_detail_ids = fields.One2many('spares.detail.info', 'parent_id', 'Spares Info')
    spare_used_ids = fields.One2many('spares.used', 'parent_id', 'Spares Used')
    product_filter = fields.Many2one('product.template', 'Product')
    
    
    @api.onchange('location_filter_id','serial_no_filter','product_filter')
    def apply_filter(self):
        domain = [('inventory_quantity','>',0)]
        if self.location_filter_id:
            domain += [('location_id','=', self.location_filter_id.id)]
        if self.serial_no_filter:
            domain += [('lot_id','=', self.serial_no_filter.id)]
        if self.product_filter:
            product_ids = self.env['product.product'].search([('parent_product','=', self.product_filter.id)])
            domain += [('product_id','in', product_ids)]
        quants = self.env['stock.quant'].search(domain)
        self.spare_detail_ids.unlink()
        if quants:
            spares_list = []
            for quant in quants:
                spares_data = {
                    'name': quant.product_id.name,
                    'item_no': quant.product_id.default_code,
                    'serial_no': quant.lot_id.name,
                    'product_id': quant.product_id.id,
                    'parent_id' : self.id
                    }
                spares_list.append((0,0, spares_data))
            self.spare_detail_ids = spares_list
                
    def consume_parts(self):
        dest_loc = self.env['stock.location'].search([('usage', '=', 'customer')], limit=1)
        if not dest_loc:
            raise UserError(_('Customer Location Missing. Please configure'))
        source_loc = self.location_filter_id.id
        if not source_loc:
            raise UserError(_('Source Location Missing.'))
        if dest_loc:
            move_list  = []
            used_list = []
            for parts_data in self.spare_detail_ids:
                if parts_data.select == True:
                    lot_id = self.env['stock.production.lot'].search([('name', '=', parts_data.serial_no)])
                    if  lot_id:
                        lot_id = lot_id.id
                    else:
                        lot_id = False
                    move_data = {
                        'name': self.service_id.name,
                        'location_id': source_loc,
                        'location_dest_id': dest_loc.id,
                        'product_id': parts_data.product_id.id,
                        'quantity_done': 1,
                        'product_uom': parts_data.product_id.uom_id and parts_data.product_id.uom_id.id or  False,
                        'product_uom_qty': 1,
                        'lot_id': lot_id
                        }
                    move_list.append(move_data)
                    used_data = {
                        'name': parts_data.name,
                        'item_no': parts_data.item_no,
                        'serial_no': parts_data.serial_no,
                        'parent_id' : self.id
                        }
                    used_list.append(used_data)
            if not used_list:
                raise UserError(_('Please select parts consumed!'))
            if used_list:
                spares_used = self.env['spares.used'].create(used_list)
            if move_list:
                moves = self.env['stock.move'].create(move_list)
                for move in moves:
                    move._action_confirm()
                    move._action_assign()
                    move.move_line_ids.write({'qty_done': 1, 'lot_id': move.lot_id and move.lot_id.id or False}) 
                    move._action_done()
        return True
    
    
    def show_spare_used(self):
        self.ensure_one()
        view = self.env.ref('service_management.activity_spare_used_popup')
        return {
            'name': _('Spares Used'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'activity.details',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
        }
    
    def show_spare_info(self):
        self.ensure_one()
        view = self.env.ref('service_management.activity_popup')
        new_lines = []
        location = False
        self.spare_detail_ids.unlink()
        if self.service_id.engineer_id:
            location = self.service_id.engineer_id.engineer_location_id
        elif self.service_id.service_gm:
            location = self.service_id.engineer_id.branch_location_id
        elif self.service_id.partner_name_id:
            location = self.service_id.partner_name_id.partner_location
        if location:
            self.location_filter_id = location
            quants = self.env['stock.quant'].search([('location_id','=', location.id), ('inventory_quantity','>',0)])
            self.spare_detail_ids.unlink()
            if quants:
                spares_list = []
                for quant in quants:
                    spares_data = {
                        'name': quant.product_id.name,
                        'item_no': quant.product_id.default_code,
                        'product_id': quant.product_id.id,
                        'serial_no': quant.lot_id.name,
                        'parent_id' : self.id
                        }
                    spares_list.append((0,0, spares_data))
                self.spare_detail_ids = spares_list
        return {
            'name': _('Spares Info'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'activity.details',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
        }
    
class SparesDetailInfo(models.Model):
    _name = 'spares.detail.info'
    
    name = fields.Char('Description')
    select = fields.Boolean()
    item_no = fields.Char('Item No.')
    product_id = fields.Many2one('product.product', 'Product')
    serial_no = fields.Char('Serial No.')
    billable = fields.Boolean('Billable')
    war_in_months = fields.Float('Warranty In Months')
    parent_id = fields.Many2one('activity.details', 'Parent')
    
class SparesUsed(models.Model):
    _name = 'spares.used'
    
    name = fields.Char('Description')
    item_no = fields.Char('Item No.')
    serial_no = fields.Char('Serial No.')
    billable = fields.Boolean('Billable')
    war_in_months = fields.Float('Warranty In Months')
    parent_id = fields.Many2one('activity.details', 'Parent')
    
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
        
    def set_customer(self, customer):
        if customer:
            self.street = customer.street
            self.street2 = customer.street2
            self.city = customer.city
            self.state_id = customer.state_id  or False
            self.country_id = customer.country_id  or False
            self.customer_type = customer.customer_type
            self.mobile = customer.mobile
            self.email = customer.email
            self.call_history_ids.unlink()
            customer_orders = self.env['service.order'].search([('customer_id', '=', customer.id)])
            customer_call_data = []
            for customer_order in customer_orders:
                serial_id = self.env['serial.no.master'].search([('name', '=', customer_order.serial_no)], limit=1)
                call_history = {
                        'customer_id': customer_order.customer_id and customer_order.customer_id.id or False,
                        'call_tkt_no': customer_order.name,
                        'product': customer_order.product_id and customer_order.product_id.id or False,
                        'serial_no': serial_id and serial_id.id  or False,
                        'prob_code_id': customer_order.problem_code and customer_order.problem_code.id or False,
                        'action_code_id': customer_order.last_activity_id and customer_order.last_activity_id.action_code and customer_order.last_activity_id.action_code.id or False,
                        'status_id': customer_order.status and customer_order.status.id or False
                    }
                customer_call_data.append((0,0, call_history))
            self.call_history_ids = customer_call_data
        else:
            self.street = ''
            self.street2 = ''
            self.city = ''
            self.state_id =  False
            self.country_id =  False
            self.customer_type = ''
            self.mobile = ''
            self.email = ''
            self.call_history_ids.unlink()
            
    def load_spares(self):
        location = False
        if self.engineer_id:
            location = self.service_gm.engineer_location_id
        if self.service_gm:
            location = self.service_gm.branch_location_id
        if self.partner_name_id:
            location = self.partner_name_id.partner_location
        if location:
            self.spares_details_ids.unlink()
            quants = self.env['stock.quant'].search([('location_id','=', location.id), ('inventory_quantity','>',0)])
            if quants:
                spares_list = []
                self.spares_details_ids.unlink()
                for quant in quants:
                    spares_data = {
                        'name': quant.product_id.name,
                        'item_no': quant.product_id.default_code,
                        'serial_no': quant.lot_id.name,
                        'service_id' : self.id
                        }
                    spares_list.append((0,0, spares_data))
                self.spares_details_ids = spares_list
                        
        
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
                serial_id = self.env['serial.no.master'].search([('name', '=', customer_order.serial_no)], limit=1)
                call_history = {
                        'customer_id': customer_order.customer_id and customer_order.customer_id.id or False,
                        'call_tkt_no': customer_order.name,
                        'product': customer_order.product_id and customer_order.product_id.id or False,
                        'serial_no': serial_id and serial_id.id  or False,
                        'prob_code_id': customer_order.problem_code and customer_order.problem_code.id or False,
                        'action_code_id': customer_order.last_activity_id and customer_order.last_activity_id.action_code and customer_order.last_activity_id.action_code.id or False,
                        'status_id': customer_order.status and customer_order.status.id or False
                    }
                customer_call_data.append((0,0, call_history))
            self.call_history_ids = customer_call_data
        else:
            self.street = ''
            self.street2 = ''
            self.city = ''
            self.state_id =  False
            self.country_id =  False
            self.customer_type = ''
            self.mobile = ''
            self.email = ''
            self.call_history_ids.unlink()
            
    def check_warranty_duration(self, end_date):
        if end_date:
            r = relativedelta.relativedelta(end_date, fields.Date.today())
            service_months_remaining = r.months
            return service_months_remaining
    
    def check_amc_warranty_status(self, end_date):
        if end_date:
            if fields.Date.today() <= end_date:
                warranty_rec = self.env['warranty.type'].search([('name','=', 'AMC')])
                if warranty_rec:
                    return warranty_rec
            else:
                warranty_rec = self.env['warranty.type'].search([('name','=', 'OOW Warranty')])
                if warranty_rec:
                    return warranty_rec
            
    def check_service_warranty_status(self, end_date):
        if end_date:
            if fields.Date.today() <= end_date:
                warranty_rec = self.env['warranty.type'].search([('name','=', 'In Warranty')])
                if warranty_rec:
                    return warranty_rec
            else:
                warranty_rec = self.env['warranty.type'].search([('name','=', 'OOW Warranty')])
                if warranty_rec:
                    return warranty_rec
            
    
    def change_serial(self):
        if not self.serial_no:
            return True
        serial_id = self.env['serial.no.master'].search([('name', '=', self.serial_no)], limit=1)
        if serial_id:
            serial_orders = self.env['service.order'].search([('serial_no', '=', self.serial_no),  ('id', '<', self.id), ('id', '!=', self.id)], order="id desc")
            amc_db_datas = self.env['amc.database'].search([('name', '=', serial_id.name)], order="id desc")
            sales_datas = self.env['sales.database'].search([('name', '=', serial_id.name)], order="id desc")
            if serial_orders:
                serial_orders
                for serial_wise_order in serial_orders:
                    self.customer_id = serial_wise_order.customer_id
                    self.set_customer(serial_wise_order.customer_id)
                    self.product_categ_id = serial_wise_order.product_categ_id
                    self.product_id = serial_wise_order.product_id
                    self.product_no = serial_wise_order.product_no
                    self.war_in_months = self.check_warranty_duration(serial_wise_order.war_end_date)
                    self.war_start_date = serial_wise_order.war_start_date
                    self.war_end_date = serial_wise_order.war_end_date
                    self.war_status = self.check_service_warranty_status(serial_wise_order.war_end_date)
                    
            if not serial_orders:
                if amc_db_datas:
                    customer = amc_db_datas[0].to_partner_id_1 or amc_db_datas[0].to_partner_id_2  or  amc_db_datas[0].to_partner_id_3
                    self.customer_id = customer
                    self.set_customer(customer)
                    self.product_categ_id = amc_db_datas[0].product_categ_id
                    self.product_id = amc_db_datas[0].product_id
                    self.product_no = amc_db_datas[0].product_id and amc_db_datas[0].product_id.default_code or ''
                    self.war_in_months = self.check_warranty_duration(amc_db_datas[0].amc_end_date)
                    self.war_start_date = amc_db_datas[0].amc_start_date
                    self.war_end_date = amc_db_datas[0].amc_end_date
                    self.war_status = self.check_amc_warranty_status(amc_db_datas[0].amc_end_date)
                    
            if not serial_orders and not amc_db_datas:
                if sales_datas:
                    if sales_datas[0].to_entity_type == "customer":
                        customer = sales_datas[0].to_partner_id_1 or sales_datas[0].to_partner_id_2  or  sales_datas[0].to_partner_id_3
                        self.customer_id = customer
                        self.set_customer(customer)
                    self.product_id = sales_datas[0].product_id or False
                    self.product_categ_id = sales_datas[0].product_categ_id or False
                    self.product_no = sales_datas[0].product_id and sales_datas[0].product_id.default_code or ''
                    self.war_in_months = self.check_warranty_duration(sales_datas[0].war_end_dt)
                    self.war_start_date = sales_datas[0].war_start_dt
                    self.war_end_date = sales_datas[0].war_end_dt
                    self.war_status = self.check_service_warranty_status(sales_datas[0].war_end_dt)
                    
                    if  sales_datas[0].from_entity_type == "customer":
                        self.customer_id = sales_datas[0].to_partner_id_2
                        
            if not serial_orders and not amc_db_datas and not sales_datas:
                raise UserError(_('There is no sales record belong  to this serial No.'))
            
            self.sale_db_ids.unlink()
            if amc_db_datas:
                amc_db_list = []
                for amc_db_data in amc_db_datas:
                    amc_data = {
                        'name': amc_db_data.name,
                        'db_type': 'AMC DB',
                        'entity_type': amc_db_data.from_entity_type,
                        'from_name':  amc_db_data.partner_id_1 and amc_db_data.partner_id_1.name or amc_db_data.partner_id_2 and amc_db_data.partner_id_2.name  or  amc_db_data.partner_id_3 and amc_db_data.partner_id_3.name or amc_db_data.location_id and amc_db_data.location_id.name,
                        'to_entity_type': amc_db_data.to_entity_type,
                        'to_name': amc_db_data.to_partner_id_1 and amc_db_data.to_partner_id_1.name or amc_db_data.to_partner_id_2 and amc_db_data.to_partner_id_2.name  or  amc_db_data.to_partner_id_3 and amc_db_data.to_partner_id_3.name or amc_db_data.to_location_id and amc_db_data.to_location_id.name,
                        'sale_inv_no': amc_db_data.amc_inv_no,
                        'sale_inv_date': amc_db_data.amc_inv_date,
                        'war_in_months': amc_db_data.amc_duration,
                        'war_start_dt': amc_db_data.amc_start_date,
                        'war_end_dt' : amc_db_data.amc_end_date
                        }
                    amc_db_list.append((0,0, amc_data))
                self.sale_db_ids = amc_db_list
            if sales_datas:
                sales_db_list = []
                for saledb_data in sales_datas:
                    sale_data = {
                        'name': saledb_data.name,
                        'db_type': 'Sale DB',
                        'entity_type': saledb_data.from_entity_type,
                        'from_name':  saledb_data.partner_id_1 and saledb_data.partner_id_1.name or saledb_data.partner_id_2 and saledb_data.partner_id_2.name  or  saledb_data.partner_id_3 and saledb_data.partner_id_3.name or saledb_data.location_id and saledb_data.location_id.name,
                        'to_entity_type': saledb_data.to_entity_type,
                        'to_name': saledb_data.to_partner_id_1 and saledb_data.to_partner_id_1.name or saledb_data.to_partner_id_2 and saledb_data.to_partner_id_2.name  or  saledb_data.to_partner_id_3 and saledb_data.to_partner_id_3.name or saledb_data.to_location_id and saledb_data.to_location_id.name,
                        'sale_inv_no': saledb_data.inv_trans_id,
                        'sale_inv_date': saledb_data.inv_trans_created_date,
                        'war_in_months': saledb_data.war_in_months,
                        'war_start_dt': saledb_data.war_start_dt,
                        'war_end_dt' : saledb_data.war_end_dt
                        }
                    sales_db_list.append((0,0, sale_data))
                self.sale_db_ids = sales_db_list
            
            purchase_datas = self.env['purchase.database'].search([('name', '=', serial_id.name)], order="id desc")
            purchase_db_list = []
            for purchase_db_data in purchase_datas:
                purchas_data = {
                    'name': purchase_db_data.name,
                    'db_type': 'Purchase DB',
                    'entity_type': purchase_db_data.from_entity_type,
                    'from_name':  purchase_db_data.partner_id_1 and purchase_db_data.partner_id_1.name or purchase_db_data.partner_id_2 and purchase_db_data.partner_id_2.name  or  purchase_db_data.partner_id_3 and purchase_db_data.partner_id_3.name or purchase_db_data.location_id and purchase_db_data.location_id.name,
                    'to_entity_type': purchase_db_data.to_entity_type,
                    'to_name': purchase_db_data.to_partner_id_1 and purchase_db_data.to_partner_id_1.name or purchase_db_data.to_partner_id_2 and purchase_db_data.to_partner_id_2.name  or  purchase_db_data.to_partner_id_3 and purchase_db_data.to_partner_id_3.name or purchase_db_data.to_location_id and purchase_db_data.to_location_id.name,
                    'sale_inv_no':  purchase_db_data.inv_trans_id,
                    'sale_inv_date': purchase_db_data.inv_trans_created_date,
                    'war_in_months': purchase_db_data.war_in_months,
                    'war_start_dt': purchase_db_data.war_start_dt,
                    'war_end_dt' : purchase_db_data.war_end_dt
                    }
                purchase_db_list.append((0,0, purchas_data))
            self.sale_db_ids = purchase_db_list
            serial_wise_orders = self.env['service.order'].search([('serial_no', '=', self.serial_no), ('id', '!=', self.id)], order="id desc")
            if serial_wise_orders:
                self.serial_history_ids.unlink()
                serial_wise_data = []
                for serial_wise_order in serial_wise_orders:
                    serial_id = self.env['serial.no.master'].search([('name', '=', serial_wise_order.serial_no)], limit=1)
                    serial_history = {
                            'customer_id': serial_wise_order.customer_id and serial_wise_order.customer_id.id or False,
                            'call_tkt_no': serial_wise_order.name,
                            'product': serial_wise_order.product_id and serial_wise_order.product_id.id or False,
                            'serial_no': serial_id and serial_id.id  or False,
                            'prob_code_id': serial_wise_order.problem_code and serial_wise_order.problem_code.id or False,
                            'action_code_id': serial_wise_order.last_activity_id and serial_wise_order.last_activity_id.action_code and serial_wise_order.last_activity_id.action_code.id or False,
                            'status_id': serial_wise_order.status and serial_wise_order.status.id or False
                        }
                    serial_wise_data.append((0,0, serial_history))
                self.serial_history_ids = serial_wise_data
        else:
            raise UserError(_('Serial No. Does not exist'))
        
    name = fields.Char('Call Ticket No.', copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('service.order'))
    company_id =  fields.Many2one('res.company', 'Company',default=lambda self: self.env.user.company_id)
    call_date = fields.Datetime('Call Received Date')
    call_date_time = fields.Datetime('Call Created Date',default=lambda self: fields.Datetime.now())
    call_type = fields.Many2one('call.type', 'Call Type')
    status = fields.Many2one('status.info', compute='_check_last_activity', string='Status')
    sub_status = fields.Many2one('sub.status.info', compute='_check_last_activity',  string='Sub Status')
    customer_ref_no = fields.Char('Customer Ref No.')
    serial_no = fields.Char('Serial No.')
    product_id = fields.Many2one('product.template','Product')
    ptav_product_variant_id = fields.Many2one('product.product', string="Related Variant")
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
    open_call_ids = fields.One2many('open.call.history', 'service_id', string='Open Calls')
    repeat_call_ids = fields.One2many('repeat.call.history', 'service_id', string='Repeat Calls')
    reopened_call_history = fields.One2many('reopened.call.history', 'service_id', string='Re-Opened Calls')
    sale_db_ids = fields.One2many('serial.no.db', 'service_id', string="Serial No. DB")
    activity_ids = fields.One2many('activity.details', 'service_id', string='Activities')
    spares_details_ids = fields.One2many('spares.details', 'service_id', string='Spares Info')
    sla_details_ids = fields.One2many('sla.details', 'service_id', string='SLA Info')
    proof_of_purchase_avl = fields.Binary('Proof of Purchase Doc')
    war_latest_id = fields.Many2one('warranty.type', 'WAR/AMC Latest')
    war_start_date = fields.Date('WAR/AMC Start Date')
    war_end_date = fields.Date('WAR/AMC End Date')
    service_gm = fields.Many2one('hr.employee', 'Service Branch')
    service_rm = fields.Many2one('hr.employee', 'Service RM')
    engineer_id = fields.Many2one('hr.employee', 'Service Engineer')
    product_categ_id = fields.Many2one('product.category', 'Product Category')
    online_support_id = fields.Many2one('res.users', 'Online Support')
    last_activity_id = fields.Many2one('activity.details', compute='_check_last_activity')
    
#     def check_serial(self):
#         return True
    
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
    
    
    
    
    
    
    
    
    