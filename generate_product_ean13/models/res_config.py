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

from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    gen_ean13 = fields.Boolean("On Product create generate EAN13", config_parameter="generate_product_ean13.gen_ean13")


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
