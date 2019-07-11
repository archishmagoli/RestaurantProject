import tornado.ioloop
import tornado.web
import tornado
from tornado.web import Application,RequestHandler
import hashlib
import datetime
from secrets import *
import codecs
import os
loop = tornado.ioloop.IOLoop.current()

class MainH(RequestHandler):
    def get(self):
        self.render('index.html')
        self.render_embed_css('home_style.css')
    def post(self):
        self.redirect('/login')
class LoginH(RequestHandler):
    def get(self):
        self.render('startup.html')
        self.render_embed_css('background_animation.css')
class Stop(RequestHandler):
    def get(self):
        global loop
        self.send_error(200)
        loop.stop()
        del loop
# In[]
application = tornado.web.Application([
    (r"/", MainH),
    (r"/login", LoginH),
    (r"/Stop", Stop),
], cookie_secret=token_urlsafe(16))
    
application.listen(8888)
loop.start()