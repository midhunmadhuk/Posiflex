# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools


class CallType(models.Model):
    _name = 'call.type'
    
    name = fields.Char('Call Type', required=True)
    
class StatusInfo(models.Model):
    _name = 'status.info'
    
    name = fields.Char('Status', required=True)
    
class SubStatusInfo(models.Model):
    _name = 'sub.status.info'
    
    name = fields.Char('Sub Status', required=True)
    status_id = fields.Many2one('status.info', 'Status', required=True)
    
class PartnerLevel(models.Model):
    _name = 'partner.level'
    
    name = fields.Char('Name', required=True)
    
class PartnerType(models.Model):
    _name = 'partner.type'
    
    name = fields.Char('Name', required=True)
    partner_level_id = fields.Many2one('partner.level', 'Partner Level', required=True)

class CustomerType(models.Model):
    _name = 'customer.type'
    
    name = fields.Char('Customer Type', required=True)
    
class WarrantyType(models.Model):
    _name = 'warranty.type'
    
    name = fields.Char('Name', required=True)
    
class ProblemCode(models.Model):
    _name = 'problem.code'
    
    name = fields.Char('Name', required=True)
    
class ActionCode(models.Model):
    _name = 'action.code'

    name = fields.Char('Name', required=True)
    
class ActivityType(models.Model):
    _name = 'activity.type'
    
    name = fields.Char('Name', required=True)
    
class SerialNoMaster(models.Model):
    _name = 'serial.no.master'
    
    name = fields.Char('Serial No.')
    product_id = fields.Many2one('product.template', 'Product')
    avail_entity_type = fields.Selection([('partner', 'Partner'), ('customer', 'Customer')], string="Available Entity Type")
    partner_id = fields.Many2one('res.partner', 'Partner')
    customer_id = fields.Many2one('res.partner', 'Customer')
    war_latest = fields.Many2one('warranty.type', 'WAR Latest')
    war_in_months = fields.Float('WAR In Months')
    war_start_dt = fields.Datetime('WAR Start Date')
    war_end_dt = fields.Datetime('WAR End Date')
    war_balance = fields.Float('WAR Balance')
    war_status = fields.Many2one('warranty.type', 'WAR Status')



    
