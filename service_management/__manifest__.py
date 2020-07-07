# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Service Management",
    'summary': "Service management features",
    'description': """
    Includes Features for service management
    """,
    'category': 'Sales',
    'version': '1.1.9',
    'depends': ['base', 'product', 'hr', 'stock', 'report_xlsx'],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'security/service_security.xml',
        'views/service_report_excel_view.xml',
        'views/service_ticket_view.xml',
        'views/database_master_view.xml',
        'wizard/call_summary_view.xml',
        'views/service_configuration_view.xml',
        'views/res_partner_view.xml'
    ],
    'demo': [
    ],
}
