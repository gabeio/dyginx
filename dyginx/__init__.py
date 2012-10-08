import sys, bottle, gevent, random
from bottle import *
from gevent import *
from jinja2 import *
from gevent.wsgi import WSGIServer

env = Environment(loader=FileSystemLoader([dynamic_,static_]))

@route("/")
def rindex():
	pass
	#login goes here

@post("/")
def pindex():
	pass
	#retrieve credentials

@route("/monitor")
def rmon():
	pass
	#displays current worker statuses

@route("/controler")
def rctrl(action=None, params**):
	pass
	#simplistic controller
	#adjust amount of workers for a section of site
	#create/delete/modify section of site/site (nginx settings & set what worker is aimed at it)

application=bottle.default_app()
WSGIServer(('', port), application, spawn=None).serve_forever()