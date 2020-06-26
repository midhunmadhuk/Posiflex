# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016-TODAY Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, date

class CallSummary(models.TransientModel):
    _name = "call.summary"
    _description = "Collection Summary Report"

    @api.model
    def get_default_from_date(self):
        current_year = datetime.now().year
        return str(datetime.strptime('%s-01-01' % (current_year),'%Y-%m-%d'))

    from_date = fields.Date(required=True, default=get_default_from_date)
    to_date = fields.Date(required=True, default=date.today())
#     company_id = fields.Many2one('res.company', required=True, 
#         default=lambda self: self.env.user.company_id.id)


    def print_collection_report(self):
        data = {}
        data['form'] = {}
        return self._print_report(data)

    def get_data(self):
        data_list  = []
        domain = []
        context = self._context
         
        datas = {'ids': context.get('active_ids', [])}
        datas['model'] = 'collection.summary'
        datas['form'] = self.read()[0]
        for field in datas['form'].keys():
            if isinstance(datas['form'][field], tuple):
                datas['form'][field] = datas['form'][field][0]
        datas['company'] = self.company_id
        type_list = ['inbound']
        
        domain = [('payment_type','in',type_list),('state','not in',['draft','cancel']),
            ('company_id','=',self.company_id.id)]
        if self.from_date:
            domain.append(('payment_date','>=',self.from_date))
        if self.to_date:
            domain.append(('payment_date','<=',self.to_date))
        
        payment_obj = self.env['account.payment']
        payments  = payment_obj.search(domain, order='payment_date,name')
        data = []
        if payments:
            payment_data_dict = {}
            for payment in payments:
                payment_data_dict = {
                    'customer_name': payment.partner_id.name,
                    'payment_number': payment.name,
                    'payment_date': payment.payment_date,
                    'payment_method': payment.journal_id.name,
                    'invoice_reference': payment.communication and payment.communication or '',
                    'amount': payment.amount,
                    }
                data.append(payment_data_dict)
        datas['payments'] = data
        return datas


    def _print_report(self, data):
        return self.env.ref('service_management.call_summary_report_xlsx').report_action(self, config=False)