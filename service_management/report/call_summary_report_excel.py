# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016-TODAY Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################

from odoo import api, models, _

class ReportXlsx(models.AbstractModel):
    _name = 'report.service_management.call_summary_report'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, wizard):
        data_set = wizard.get_data()
        report_name = 'report.service_management.call_summary_report'
        sheet = workbook.add_worksheet()
        sheet.set_column(0, 15, 25)
        format1 = workbook.add_format({'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True, 'align': 'vcenter', 'bold': True,})
        format12 = workbook.add_format({'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True, 'align': 'vcenter', 'bold': True,})
        format2 = workbook.add_format({'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True, 'align': 'vcenter', })
        format11 = workbook.add_format({'font_size': 12, 'align': 'center', 'right': True, 'left': True, 'bottom': True, 'top': True, 'bold': True})
        format3 = workbook.add_format({'bottom': True, 'top': True, 'font_size': 14, 'num_format': '#,##0.00'})
        format4 = workbook.add_format({'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True, 'align': 'vcenter', })
        format5 = workbook.add_format({'bottom': True, 'top': True, 'font_size': 14, 'num_format': '#,##0.00', 'bold': True})
        format6 = workbook.add_format({'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True, 'align': 'vcenter', })
        format1.set_align('center')
        format2.set_align('center')
        format12.set_align('center')
        format11.set_align('left')
        format6.set_align('center')
        bold = workbook.add_format({'bold': True})

        date_format = format2.set_num_format('dd/mm/yyyy')
        sheet.merge_range('A1:F1', data_set['company'].name,format1)
        sheet.write(1, 0, 'From', format12)
        sheet.write(1,1,data_set['form']['from_date'],format2)
        sheet.write(1, 2, 'To', format12)
        sheet.write(1,3,data_set['form']['to_date'],format2)
        
        w_row_no = 5
        total_amount = 0.0
        if data_set['payments']:
            sheet.write(3,0,'Customer Name', format12)
            sheet.write(3,1,'Payment Number', format12)
            sheet.write(3,2,'Payment Date', format12)
            sheet.write(3,3,'Payment Method', format12)
            sheet.write(3,4,'Invoice Reference', format12)
            sheet.write(3,5,'Payment Amount', format12)
            for payment in data_set['payments']:
                total_amount += payment['amount']
                sheet.write(w_row_no,0,payment['customer_name'],format4)
                sheet.write(w_row_no,1,payment['payment_number'],format4)
                sheet.write(w_row_no,2,payment['payment_date'],format2)
                sheet.write(w_row_no,3,payment['payment_method'],format4)
                sheet.write(w_row_no,4,payment['invoice_reference'],format4)
                sheet.write(w_row_no,5,payment['amount'],format3)
                w_row_no += 1
            sheet.write(w_row_no+1,4,'TOTAL :', format1)
            sheet.write(w_row_no+1,5,total_amount, format5)
