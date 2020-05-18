# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Stock Matrix",
    'summary': """
       Add variants to your stock picking through an Order Grid Entry.
    """,
    'description': """
        This module allows to fill Purchase Orders rapidly
        by choosing product variants quantity through a Grid Entry.
    """,
    'category': 'Operations/Purchase',
    'version': '1.0',
    'depends': ['stock', 'product_matrix'],
    'data': [
        'views/assets.xml',
        'views/stock_views.xml',
    ],
}
