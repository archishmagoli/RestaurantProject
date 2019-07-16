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
import re
import json
# In[]
n = 10
cwd = r"C:\Users\taged\Desktop\RestaurantProject-Pranav-s-Branch"
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
            keyword = self.get_cookie('search')
            with open(os.path.join(cwd,"Restraunt.json"),'r') as f:
                User_list = json.load(f)
            keys = list(User_list.keys())
            keysword = ''
            for i in keyword:
                keysword = keysword+'['+i+']'
            skey = re.findall(keysword+"\w+", ' '.join(keys))
            returnl = []
            for i in skey:
                print(i)
                returnl.append(User_list[i])
                print(User_list[i]['Name'])
            final = []

            for i in returnl:
                name = i['Name']  
                img = i['Img']
                link = i['Name']
                print(name)
                print(img)
                final.append([name,img,link])

            
            
            message = '''
                 <head>
                
                <style>
                body {
                	width: 100wh;
                	height: 90vh;
                	color: #fff;
                	background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);
                	background-size: 400% 400%;
                	-webkit-animation: Gradient 10s ease infinite;
                	animation: Gradient 10s ease infinite;
                }
                
                @-webkit-keyframes Gradient {
                	0% {
                		background-position: 0% 50%
                	}
                	50% {
                		background-position: 100% 50%
                	}
                	100% {
                		background-position: 0% 50%
                	}
                }
                
                
                @keyframes Gradient {
                	0% {
                		background-position: 0% 50%
                	}
                	50% {
                		background-position: 100% 50%
                	}
                	100% {
                		background-position: 0% 50%
                	}
                }
                
                h1,
                h6 {
                	font-family: 'Open Sans';
                	font-weight: 300;
                	text-align: center;
                	padding-top: 200px;
                	top: 45%;
                	right: 0;
                	left: 0;
                }
                
                #welcome_text {
                	color: white;
                	font-family: Open Sans;
                	font-size: 70px;
                }
                
                #login_btn {
                	margin-top: 100px;
                	margin-left: 48%;
                	font-size: 30px;
                	
                }
                
                #signup_btn {
                	margin-top: 75px;
                	margin-left: 47%;
                	font-size: 30px;
                	
                .img {
                	
                	visibility:hidden;
                	
                	display: block;
                	margin-left: auto;
                	margin-right: auto;
                
                }
                </style>
                
                </head>
                
                <h1 id='welcome_text'>Search Results:</h1>
                
                <br>
                <center>
                |||
                
                </center>
                
                </body>
                '''
        
        

            fm = []
            for i in range(len(final)):
                li = final[i]
                fillin = '''
                        
                <h2>|||<h2>
                <img style="width:512px;height:512px;" class='img' src="|/|" alt="HTML5 Icon" />
                <form action="" method="post">
                    <input type="submit" name="Poster" value="|\|" />
                </form>
                '''
                fillin = fillin.replace("|||",str(li[0]))
                fillin = fillin.replace("|/|",str(li[1]))
                fillin = fillin.replace("|\|",str(li[2]))
                fm.append(fillin)        
            message = message.replace('|||',' '.join(fm))
            self.write(message)
        except Exception as e:
            print(e)
            self.send_error(400)
    def post(self):
        print(self.get_argument('Poster'))
        self.set_cookie('PageVisit',self.get_argument('Poster'))
        self.redirect('/Rpage')
class Search(RequestHandler):
    def get(self):
        self.render('Search.html')
    def post(self):
        self.set_cookie('search',self.get_argument('Search'))
        print('Redirecting')
        self.redirect('/Searched')

class Rpage(RequestHandler):
    def get(self):
        message = '''
                         <head>
                
                <style>
                body {
                	width: 100wh;
                	height: 90vh;
                	color: #fff;
                	background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);
                	background-size: 400% 400%;
                	-webkit-animation: Gradient 10s ease infinite;
                	animation: Gradient 10s ease infinite;
                }
                
                @-webkit-keyframes Gradient {
                	0% {
                		background-position: 0% 50%
                	}
                	50% {
                		background-position: 100% 50%
                	}
                	100% {
                		background-position: 0% 50%
                	}
                }
                
                
                @keyframes Gradient {
                	0% {
                		background-position: 0% 50%
                	}
                	50% {
                		background-position: 100% 50%
                	}
                	100% {
                		background-position: 0% 50%
                	}
                }
                
                h1,
                h6 {
                	font-family: 'Open Sans';
                	font-weight: 300;
                	text-align: center;
                	padding-top: 200px;
                	top: 45%;
                	right: 0;
                	left: 0;
                }
                
                #welcome_text {
                	color: white;
                	font-family: Open Sans;
                	font-size: 70px;
                }
                
                #login_btn {
                	margin-top: 100px;
                	margin-left: 48%;
                	font-size: 30px;
                	
                }
                
                #signup_btn {
                	margin-top: 75px;
                	margin-left: 47%;
                	font-size: 30px;
                	
                .img {
                	
                	visibility:hidden;
                	
                	display: block;
                	margin-left: auto;
                	margin-right: auto;
                
                }
                </style>
                
                </head>
                
                <h1 id='welcome_text'>Restraunt Details:</h1>
                
                <br>
                <center>
                <h2>NameOfRest<h2>
                <img style="width:512px;height:512px;" class='img' src="|/|" alt="Image" />
                <br>
				<h2>Menu:</h2>
                <form action="" method="post">
    				|||
                </form>
                <br>
				<h2>Address:</h2>
				<h2>|\|</h2>
                <br>
				<h2>Hours:</h2>
				<h2>|?|</h2>
                
                </center>
                
                </body>
                '''
        keyword = self.get_cookie('PageVisit')
        with open(os.path.join(cwd,"Restraunt.json"),'r') as f:
            Rlist = json.load(f)
        item = Rlist[keyword]
        Name = item['Name']
        Img = item['Img']
        Menu_items = []
        Foods = item['Foods']
        base = ''' <input type="submit" name="food" value="|||" /> '''
        for i in Foods:
            Menu_items.append(base.replace('|||',i['Name']))
            
        Address = item['Adress']
        Hours = item['Hours']
        message = message.replace('NameOfRest',Name)
        message = message.replace('|/|',Img)
        
        message = message.replace('|||',''.join(Menu_items))
        message = message.replace('|\|',Address)
        message = message.replace('|?|',Hours)
        self.write(message)
        
    def post(self):
        print(self.get_argument('food'))
        self.set_cookie('getfood',self.get_argument('food').replace(' ','_'))
        self.redirect('/RatePage')
class RatePage(RequestHandler):
    def get(self):
        try:
            print("C")
            food = self.get_cookie('getfood').replace('_',' ')
            rst = self.get_cookie('PageVisit')
            with open(os.path.join(cwd,"Restraunt.json"),'r') as f:
                Rlist = json.load(f)
                
            rst = Rlist[rst]
            foods = rst['Foods']
            Name = rst['Name']
            Img = rst['Img']
            Address = rst['Adress']
        
            food_val = list()
            fvl = list()
            for i in foods:
                if i["Name"] == food:
                    food_val = i['Values']
                fvl.append(i['Values'])

            Se = str(self.get_secure_cookie("Sess"))[2:-1]
            print("C")
            User = Token_list[Se]
            cur_val = User_list[User]['Currentlist']
            print("C")
            fil = []
            for i in fvl:
                fil.append(np.linalg.norm([i,cur_val]))
            mean = np.mean(fil)
            sd = np.std(fil)
            print(food_val)
            print(cur_val)
            type(food_val)
            type(cur_val)
            print("C")
            val = np.linalg.norm([food_val,cur_val])
            print("C")
            val2 = (mean-val)/sd
            print(val2)
            m = ''
            if val2 <= -1.5:
                m='Terrible Choice'
            if val2 > -1.5:
                m='Bad Choice'
            if val2 >= -.5:
                m='Ok Choice'
            if val2 >= .5:
                m='Good Choice'
            if val2 >= 1.5:
                m='Great Choice'
            
            message = '''<!DOCTYPE html>
            <html>
            	<head>
            		<title>My Slander</title>
            		<link href="https://fonts.googleapis.com/css?family=Open+Sans:300,800&display=swap" rel="stylesheet">
            	</head>
            	<body>
            		<style>
                		body {
                		margin-left: 325px;
                		margin-right: 325px;
                		width: 100wh;
                		height: 90vh;
                		color: white; 
                		font-family: Open Sans;
                		background: linear-gradient(-45deg, #F3DC32, #64A8AE, #C1ED87, #F0A52B);
                		background-size: 400% 400%;
                		-webkit-animation: Gradient 10s ease infinite;
                		animation: Gradient 10s ease infinite;
                		}
                		@-webkit-keyframes Gradient {
                			0% {
                				background-position: 0% 50%
                			}
                			50% {
                				background-position: 100% 50%
                			}
                			100% {
                				background-position: 0% 50%
                			}
                		}
                		@keyframes Gradient {
                			0% {
                				background-position: 0% 50%
                			}
                			50% {
                				background-position: 100% 50%
                			}
                			100% {
                				background-position: 0% 50%
                			}
                		}
                		#info {
                			float: left;
                		}
                		h2 {
                			font-weight: 300;
                		}
                		#food {
                			width: 350px;
                			height: auto;
                		}
                		h1 {
                			text-align: center;
                			font-weight: 700;
                			font-size: 40px;
                		}
                		#rater {
                			float: right;
                			margin-right: 200px;
                		}
                		.slider {
                			width: 100%;
                			-webkit-appearance: none;
                			appearance: none;
                			height: 25px;
                			background: #ADD8E6;
                			outline: none;
                			opacity: 0.7;
                			-webkit-transition: .2s; 
                			transition: opacity .2s;
                			border-radius: 10px;
                			margin-bottom: 15px;
                		}
                		.slider:hover {
                			opacity: 1;
                		}
                		.slider::-webkit-slider-thumb {
                			-webkit-appearance: none;
                			appearance: none;
                		    width: 50px;
                		    height: 50px;
                		    border-radius: 50%; 
                		    background: url('https://image.flaticon.com/icons/svg/143/143515.svg');
                		    cursor: pointer;
                		}
                		#submit {
                			width: 75px;
                			height: 25px;
                			border-radius: 5px;
                			background: #C1ED87;
                			box-shadow: none;
                			outline: none;
                			border: 2px solid #64A8AE;
                		}
                		#submit:hover {
                			background: #F3DC32;
                		}
                		h3 {
                			font-size: 20px;
                		}
                		#demo {
                			font-size: 25px;
                			font-weight: 600;
                			color: green;
                		}
                	</style>

            		<h1>Food Settings</h1>
            		<div id = "info">
            			<img src = "|||" id = "food">
            			<h2>|?|<br>Address: 5|\|<br></h2>
            		</div>
            		<div id = "rater">
                        <h1>|M|</h1>
            			<form action = "" method="post">
            			<input type = "range" min = "1" max = "100" value = "50" class = "slider" id = "myRange">
            			<input type = submit id = "submit">
            			</form>
            			<p>Current value: <span id = demo></span></p>
            		</div>
                <script>
            		var slider = document.getElementById("myRange");
            		var output = document.getElementById("demo");
            		output.innerHTML = slider.value;
            
            		slider.oninput = function() {
            		  output.innerHTML = this.value;
            		}
                    
            	</script>
            	</body>
            </html>
            '''
            
            message = message.replace('|M|',m)
            message = message.replace('|||',Img)
            message = message.replace('|?|',Name)
            message = message.replace('|\|',Address)
            
            
            
            
            
            self.write(message)
        except Exception as e:
            print(e)
            self.send_error(400)
application = tornado.web.Application([
    (r"/", MainH),
    (r"/Start", StartH),
    (r"/Stop", Stop),
    (r"/Login", Login),
    (r"/Home", Home),
    (r"/Signup", Signup),
    (r"/Search", Search),
    (r"/Searched", Searched),
    (r"/Rpage", Rpage),
    (r"/RatePage", RatePage),
    (r'/js/(.*)', web.StaticFileHandler),
    (r'/css/(.*)', web.StaticFileHandler),
    (r'/images/(.*)', web.StaticFileHandler),
], cookie_secret=token_urlsafe(16),)
application.listen(8888)
loop.start()