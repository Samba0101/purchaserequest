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

from odoo import models, api, _
from datetime import datetime


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model_create_multi
    def create(self, vals):
        res = super(ProductTemplate, self).create(vals)
        for rec in res:
            if rec:
                if not rec.barcode and self.env[
                    "ir.config_parameter"
                ].sudo().get_param("generate_product_ean13.gen_ean13"):
                    barcode_str = self.env["barcode.nomenclature"].sanitize_ean(
                        "%s%s" % (rec.id, datetime.now().strftime("%d%m%y%H%M"))
                    )
                    rec.write({"barcode": barcode_str})
        return res


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model_create_multi
    def create(self, vals):
        res = super(ProductProduct, self).create(vals)
        for rec in res:
            if rec:
                if not rec.barcode and self.env[
                    "ir.config_parameter"
                ].sudo().get_param("generate_product_ean13.gen_ean13"):
                    barcode_str = self.env["barcode.nomenclature"].sanitize_ean(
                        "%s%s" % (rec.id, datetime.now().strftime("%d%m%y%H%M"))
                    )
                    rec.write({"barcode": barcode_str})
        return res


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
