# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:48:39 2019

@author: Pranav Devarinti
"""
import numpy as np
import tornado.ioloop
import tornado.web as web
import tornado
from tornado.web import Application,RequestHandler,RedirectHandler
from secrets import token_urlsafe,randbits
import codecs
import os
import json
import re
# In[]
n = 10
cwd = r"C:\Users\taged\Desktop\RestaurantProject-Pranav-s-Branch-2"
loop = tornado.ioloop.IOLoop.instance()
User_list = dict()
try:
   with open(os.path.join(cwd,"UAS.json"),'r') as f:
        User_list = json.load(f)
        print(cwd)
except:
    with open(os.path.join(cwd,"UAS.json"),'a+') as f:
        User_list['Pranav'] = {'id':randbits(100),'password':'D','Currentlist':np.random.uniform(low=-1,high=1,size=(n)).tolist(),'History':[['BurgerBoi','']]}
        User_list['Sujit'] = {'id':randbits(100),'password':'I','Currentlist':np.random.uniform(low=-1,high=1,size=(n)).tolist(),'History':[]}
        print('dumped')
        json.dump(User_list,f)
Token_list = dict()
# In[]

    

class MainH(RequestHandler):
    def get(self):
        self.render('index.html')
    def post(self):
        rd = self.get_argument('Redirect')
        if rd == 'Login':
            print(rd)
            self.redirect('/Start')
        else:
            self.redirect('/Signup')
    
    
class StartH(RequestHandler):
    def get(self):
        self.render('startup.html')

class Stop(RequestHandler):
    def get(self):
        global loop
        self.send_error(200)
        loop.stop()
        del loop
class Login(RequestHandler):
    def get(self):
        self.render('login_page.html')
    def post(self):
        
        try:
            User = User_list[self.get_argument("uname")]
            print(User)
            if self.get_argument("psw") == User['password']:
                x = token_urlsafe(16)
                self.set_secure_cookie("Sess",x)
                Token_list[x] = self.get_argument("uname")
                self.redirect('/Home')
                print('accepted')
            else:
                print('Incorrect Username Or Password')
                print(self.get_argument("psw"))
        except:
            print("Bad Request")
            self.redirect('/Login')
            
class Home(RequestHandler):
    def get(self):
        try: 
            Se = str(self.get_secure_cookie("Sess"))[2:-1]
            print(Se)
            User = Token_list[Se]
            cv = str(User_list[User]['Currentlist'])
            message = '''<html>
            <head>
            <style>
            body {
            	background-color:rgb(100, 221, 233)
            	}
            	</style>
            </head>
            <body>
            <h1>Welcome<h1>
            <h1>||<h1>
            <h1>Your current food values are<h1>
            <a href='/Search'>Search</a>
            <p>|\|</p>
            </body>'''
            message = message.replace('||',User)
            message = message.replace('|\|',cv)
            self.write(message)
            
            
        except:
            print('Sending back')
            self.redirect('/Login')
    
class Signup(RequestHandler):
    def get(self):
        self.render('signup_page.html')
    def post(self):
        try:
            User_list[self.get_argument("uname")] = {'Id':randbits(100),'password':self.get_argument("psw"),'Currentlist':np.random.uniform(low=-1,high=1,size=(n)).tolist()}
            x = token_urlsafe(16)
            self.set_secure_cookie("Sess",x)
            Token_list[x] = self.get_argument("uname")
            with open(os.path.join(cwd,"UAS.json"),'w') as f:
                json.dump(User_list,f)
                print('dumped')
            self.redirect('/Home')
            print('accepted')
        except Exception as e: 
            print(e)
            print("Bad Request")
            self.redirect('/')
class Searched(RequestHandler):
    def get(self):
        try:
            print('C1')
            keyword = self.get_cookie('search')
            print('C2')
            with open(os.path.join(cwd,"Restraunt.json"),'r') as f:
                print('C3')
                User_list = json.load(f)
                print('C4')
            keys = list(User_list.keys())
            print('C5')
            keysword = ''
            print('C6')
            for i in keyword:
                print('C7')
                keysword = keysword+'['+i+']'
            print('C8')
            skey = re.findall(keysword+"\w+", ' '.join(keys))
            print('C9')
            returnl = []
            for i in skey:
                returnl.append(User_list[i])
                print('C9')
            print(returnl)
            final = []

            for i in returnl:
                print('C10')
                name = i['Name']  
                img = i['Img']
                link = '/'
                print('C11')
            
                final.append([name,img,link])
            print('C12')
            self.render("searched.html",items=final)
            
        except Exception as e:
            print(e)
            self.send_error(400)
class Search(RequestHandler):
    def get(self):
        self.render('Search.html')
    def post(self):
        self.set_cookie('search',self.get_argument('Search'))
        print('Redirecting')
        self.redirect('/Searched')
application = tornado.web.Application([
    (r"/", MainH),
    (r"/Start", StartH),
    (r"/Stop", Stop),
    (r"/Login", Login),
    (r"/Home", Home),
    (r"/Signup", Signup),
    (r"/Search", Search),
    (r"/Searched", Searched),
    (r'/js/(.*)', web.StaticFileHandler),
    (r'/css/(.*)', web.StaticFileHandler),
    (r'/images/(.*)', web.StaticFileHandler),
], cookie_secret=token_urlsafe(16),)
    
application.listen(8888)
loop.start()
