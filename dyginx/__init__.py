import sys, bottle, gevent, random, sqlite3
from bottle import *
from gevent import *
from jinja2 import *
from gevent.wsgi import WSGIServer
from subprocess import Popen, PIPE, STDOUT
from support import hashtime

db = sqlite3.connect('internals.db')
env = Environment(loader=FileSystemLoader([".","..","./dyginx"]))

def nconfw(env,fname,params):
	fs = open(fname,'w+')
	fs.write(env.get_template("nginx-temp.jinja").render(p=params))
	fs.close()
	del fs

def checknginx():
	cmd = "sh /etc/init.d/nginx check" # or nginx -t
	prompt = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
	answer = prompt.communicate()
	if "failed" in answer[0].replace("\n","").replace("\r","").split(" "):
		return False
	return True

def restartnginx():
	cmd = "sh /etc/init.d/nginx reload"
	prompt = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
	answer = prompt.communicate()
	if "error" in answer[0].replace("\n","").replace("\r","").split(" "):
		hashtime(str("nginx is down! come fix me!!!"))
		return False
	return True

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
def rctrl(action=None, **params):
	#retrieve username
	db.execute("")
	#retrieve loopback settings
	#retrieve loopbackPort
	#retrieve domainName
	conf = env.get_template("nginx-temp.jinja").render(p=params)
	fs = open('/etc/nginx/sites/'+params.upstreamer)
	fs.write(conf)
	fs.close()
	
	pass
	#simplistic controller
	#adjust amount of workers for a section of site
	#create/delete/modify section of site/site (nginx settings & set what worker is aimed at it)

@route("/settings")
def rsettings():
	pass
	#change account settings (password, add users, add groups)
try:
	if dyginx_runner:
		application=bottle.default_app()
		WSGIServer(('', port), application, spawn=None).serve_forever()
except NameError: pass