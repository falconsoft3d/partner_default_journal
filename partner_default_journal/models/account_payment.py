# -*- coding: utf-8 -*-

from odoo import models, api


class account_payment(models.Model):
    _inherit = 'account.payment'

    @api.multi
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id:
            if self._context.get('default_payment_type') == 'inbound' or \
                    self._context.get('type') == 'out_invoice':

                self.journal_id = self.partner_id.journal_credit

            if self._context.get('default_payment_type') == 'outbound' or \
                    self._context.get('type') == 'in_invoice':

                self.journal_id = self.partner_id.journal_debit
        else:
            self.journal_id = False
