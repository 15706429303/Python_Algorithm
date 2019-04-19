# -*- coding:UTF-8 -*-
import threading
from time import sleep

import bottle

@bottle.route('/')
# @bottle.route('/hello')
# @bottle.route('/hello/<name>')
# @bottle.route('/<action>/<name>')
# @bottle.route('/hello/<name:int>')
# @bottle.route('/hello/<name:float>')
# @bottle.route('/hello/<name:path>')
# @bottle.route('/hello/<name:re:[0-9]>')
def hello(action='hello', name='world'):
    return '%s %s!' % (action, name)


@bottle.route('/login')
def login():
    # return bottle.request.GET.get('name')
    # return bottle.request.query['name']
    # return bottle.request.query.name
    return bottle.request.query_string


@bottle.route('/login', method='POST')
def login():
    # chulian luanma
    # return bottle.request.forms.get['name']
    return bottle.request.POST.decode('utf-8')
    return bottle.request.POST.get('name')

bottle.debug(True)
bottle.run(host='localhost', port=8989)
