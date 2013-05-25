#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Time-Web - Main
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Erica Nogueira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/24
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from bottle import route, view, run, get, post, static_file, template, request
import bottle
import os
from couchdb import Server
import database
DIR = os.path.dirname(__file__)+'/'

@route('/<request:re:\w\w\w\w\w>')
@view(DIR+'templates/record_get')
def record_from_code(request):
    try:
        item = database.DRECORD[request]
        return item
    except Exception:
        return "Registro não encontrado"
        pass

@route('/record/new')
@view(DIR+'templates/record_new')
def record_register():
    return {}

@post('/record/save')
def record_save():
    try:
        key = request.forms.item_id
        item = database.DRECORD[key] = dict(
            name=request.forms.name, item_id=key)
        return template (DIR+'templates/record_get', item)
        return item
    except Exception:
        return "Registro não foi gravado"


if __name__ == "__main__":
    run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()
