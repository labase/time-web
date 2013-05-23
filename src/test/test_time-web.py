#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Tiem-Web - Teste
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

class TestTime_Web(unittest.TestCase):

    def setUp(self):
        self.app = TestApp(app)
        pass

    def test_qr_code(self):
        "retorna a descricao do qrcode."
        result = self.app.get('/admin')
        assert result.status == '200 OK'
        assert 'admin' in result , 'no admin in %s'%result
        pass

if __name__ == '__main__':
    unittest.main()
