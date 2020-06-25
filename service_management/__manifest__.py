# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Service Management",
    'summary': "Service management features",
    'description': """
    Includes Features for service management
    """,
    'category': 'Sales',
    'version': '1.1.3',
    'depends': ['base', 'product', 'hr'],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/service_ticket_view.xml',
        'views/service_configuration_view.xml',
        'views/res_partner_view.xml'
    ],
    'demo': [
    ],
}
