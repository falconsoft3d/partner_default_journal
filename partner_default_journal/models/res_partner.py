# -*- coding: utf-8 -*-

from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    journal_credit = fields.Many2one(
        'account.journal', 'Forma de cobro', domain=[
            ('type', 'in', ('bank', 'cash'))])

    journal_debit = fields.Many2one(
        'account.journal', 'Forma de pago', domain=[
            ('type', 'in', ('bank', 'cash'))])
