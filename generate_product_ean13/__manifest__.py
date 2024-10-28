# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    "name": "Generate Product EAN13 (Community)",
    "version": "17.0.1.0.0",
    "price": 30,
    "summary": "Generate automatic and manual barcode for products",
    "category": "Sales Management",
    "currency": "EUR",
    "description": """Generate automatic and manual barcode for products""",
    "author": "Acespritech Solutions Pvt. Ltd.",
    "website": "http://www.acespritech.com",
    "depends": ["base", "product", "sale_management", "barcodes"],
    "data": [
        "security/ir.model.access.csv",
        "views/generate_product_ean13_view.xml",
        "views/res_config_view.xml",
    ],
    "images": ["static/description/main_screenshot.jpg"],
    "installable": True,
    "auto_install": False,
    "license": 'LGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
