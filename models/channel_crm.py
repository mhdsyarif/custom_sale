# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ChannelQuotatios(models.Model):
    _inherit = 'sale.order'

    channel = fields.Many2one('utm.source', string="Channel", required="required")
