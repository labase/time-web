#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Time-Web - Teste
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Erica Nogueira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/22
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
import unittest
from main import app
from webtest import TestApp
from webob import Request, Response
import database
ITEM = 'item'
database.DRECORD = dict(admin = dict(name = ITEM, item_id = ITEM))
class TestTime_Web(unittest.TestCase):

    def setUp(self):
        self.app = TestApp(app)
        pass

    def test_qr_code(self):
        "retorna a descricao do qrcode."
        result = self.app.get('/admin')
        assert result.status == '200 OK'
        assert 'item' in result , 'no admin in %s'%result
        pass

    def test_register_record(self):
        "Registra um item."
        result = self.app.get('/record/new')
        assert result.status == '200 OK'
        assert 'Registro' in result , 'no cetoni in %s'%result
        pass

    def test_register_record_save(self):
        "Salva o registro de um item."
        #result = self.app.post('/record/save', dict(name='Teste CTONI', code='ctoni'))
        result = self.app.post('/record/save', {'name':'Teste CTONI', 'item_id':'ctoni'})
        assert result.status == '200 OK'
        assert 'Teste CTONI' in result , 'no cetoni in %s'%result
        assert 'ctoni' in database.DRECORD , 'no cetoni in %s'%database.DRECORD
        result = self.app.get('/ctoni')
        assert 'Teste CTONI' in result , 'did not save cetoni in %s'%result
        pass

if __name__ == '__main__':
    unittest.main()
