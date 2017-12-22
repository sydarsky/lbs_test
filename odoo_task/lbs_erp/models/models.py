# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class Test(models.Model):
    _name = 'test.test'

    name = fields.Char(string='Title', required=True, index=True)
    test_purpose = fields.Text(string='Test purpose')
    tester = fields.Many2one('res.partner', 'Test',
                             required=True, ondelete='cascade')


class TestSession(models.Model):
    _name = 'test.test_session'

    name = fields.Char(string='Title', required=True, index=True)

    test = fields.Many2one('test.test', 'Test', ondelete='cascade',
                           index=True, required=True)
    start_date = fields.Datetime('Start date', required=True)
    end_date = fields.Datetime('End date', required=True)
    duration = fields.Integer(string="Duration", readonly=True,
                              help="Duration in seconds", store=False,
                              compute="_test_duration")


    @api.depends('start_date', 'end_date')
    def _test_duration(self):
        datetime_format = "%Y-%m-%d %H:%M:%S"
        for item in self:
            if item.end_date and item.start_date:
                if fields.Datetime.from_string(item.end_date) < fields.Datetime.from_string(item.start_date):
                    return {
                        'warning': {
                            'title': "Incorrect date values",
                            'message': "Start date can't be later than the end date",
                        },
                    }
                end_date = datetime.strptime(item.end_date, datetime_format)
                start_date = datetime.strptime(item.start_date, datetime_format)
                delta = end_date.timestamp() - start_date.timestamp()
                item.duration = delta
            else:
                item.duration = 0


    @api.onchange('start_date', 'end_date')
    def _verify_valid_dates(self):
        if self.end_date and self.start_date:
            if fields.Datetime.from_string(self.end_date) < fields.Datetime.from_string(self.start_date):
                return {
                    'warning': {
                        'title': "Incorrect date values",
                        'message': "Start date can't be later than the end date",
                    },
                }



class Partner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner']

    is_tester = fields.Boolean("Is Tester", store=False, readonly=True,
                               compute='_is_tester',
    )
    tests_expected = fields.Integer('Tests Expected Within 30 days',
                                    readonly=False,
                                    store=False,
                                    compute='_tests_expected',
    )

    @api.one
    def _is_tester(self):
        self.is_tester = bool(self.env['test.test'].search_count([('tester', '=', self.id)]))

    @api.one
    def _tests_expected(self):
        sessions_number = 0
        datetime_format = "%Y-%m-%d %H:%M:%S"
        month = datetime.timedelta(days=30)
        tests_dict = defaultdict(list)
        sessions = self.env['test.test_session']
        tests = self.env['test.test'].search([('tester', '=', self.id)])
        sessions_of_partner = sessions.search([('test', '=', test.id)])
        for sop in sessions_of_partner:
            sop_start = datetime.strptime(sop.start_date, datetime_format)
            sop_end = datetime.strptime(sop.end_date, datetime_format)
            if fields.Datetime.from_string(sop.start_date) <= datetime.now() <= fields.Datetime.from_string(sop.end_date) or \
                fields.Datetime.from_string(sop.start_date) <= datetime.now() + month <= fields.Datetime.from_string(sop.end_date):
                sessions_number += 1
        # query = '''
        #   SELECT count(tts.id)
        #   FROM test_test_session as tts
        #     INNER JOIN test_test as tt
        #       on tts.test = tt.id
        #     INNER JOIN res_partner as rp
        #       on tt.tester = rp.id
        #   WHERE tt.tester = %s
        #     AND tts.start_date < NOW() + INTERVAL %s
        #     AND tts.end_date > NOW()
        #   '''
        self.env.cr.execute(query, [self.id, '1 month'])
        self.tests_expected = session_number # self.env.cr.fetchone()[0]
