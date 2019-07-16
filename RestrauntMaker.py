# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:13:23 2019

@author: taged
"""

import numpy as np
import os
import json
import secrets
cwd = r"C:\Users\Pranav Devarinti\Desktop\Restr"
data = dict()
# In[]
#Rest1
def generatevalues():
    return np.random.uniform(low=-1,high=1,size=(100)).tolist()

f1 = {'Name':'French Fries','Id':secrets.randbits(100),'Values':generatevalues()}
f2 = {'Name':'Burger','Id':secrets.randbits(100),'Values':generatevalues()}
f3 = {'Name':'Pizza','Id':secrets.randbits(100),'Values':generatevalues()}
f4 = {'Name':'Hotdog','Id':secrets.randbits(100),'Values':generatevalues()}
f5 = {'Name':'Hamburger','Id':secrets.randbits(100),'Values':generatevalues()}
f6 = {'Name':'Kettle Chips','Id':secrets.randbits(100),'Values':generatevalues()}

R1 = {'Name':'BurgerBoi','Img':'https://i.pinimg.com/originals/56/61/a8/5661a8e8892f4da0804e4f1d00bac9e8.jpg','Foods':[f1,f2,f3,f4,f5,f6],'Adress':'504 burger lane','Hours':'9am-10pm'}
data['BurgerBoi'] = R1

f7 = {'Name':'Rice Noodles','Id':secrets.randbits(100),'Values':generatevalues()}
f8 = {'Name':'Pad Thai','Id':secrets.randbits(100),'Values':generatevalues()}
f9 = {'Name':'Spring Rolls','Id':secrets.randbits(100),'Values':generatevalues()}
f10 = {'Name':'Coconut Soup','Id':secrets.randbits(100),'Values':generatevalues()}
f11 = {'Name':'Curry','Id':secrets.randbits(100),'Values':generatevalues()}
f12 = {'Name':'Fried Rice','Id':secrets.randbits(100),'Values':generatevalues()}

R2 = {'Name':'ThaiTime','Img':'http://static.asiawebdirect.com/m/bangkok/portals/bangkok-com/homepage/food-top10/pagePropertiesImage/thai-som-tum.jpg','Foods':[f7,f8,f9,f10,f11,f12],'Adress':'504 Thai lane','Hours':'9am-10pm'}
data['ThaiTime'] = R2

f13 = {'Name':'Sub','Id':secrets.randbits(100),'Values':generatevalues()}
f14 = {'Name':'Cookie','Id':secrets.randbits(100),'Values':generatevalues()}
f15 = {'Name':'Soup','Id':secrets.randbits(100),'Values':generatevalues()}
f16 = {'Name':'Milkshake','Id':secrets.randbits(100),'Values':generatevalues()}
f17 = {'Name':'Pretzel','Id':secrets.randbits(100),'Values':generatevalues()}
f18 = {'Name':'Deli Meats','Id':secrets.randbits(100),'Values':generatevalues()}

R3 = {'Name':'DalesDeli','Img':'http://www.fortmcdowellcasino.com/sysimg/a-new-york-deli-dining-a-new-york-deli-image.jpg','Foods':[f13,f14,f15,f16,f17,f18],'Adress':'504 Deli lane','Hours':'9am-10pm'}
data['DalesDeli'] = R3

f7 = {'Name':'Rice Noodles','Id':secrets.randbits(100),'Values':generatevalues()}
f8 = {'Name':'Pad Thai','Id':secrets.randbits(100),'Values':generatevalues()}
f9 = {'Name':'Spring Rolls','Id':secrets.randbits(100),'Values':generatevalues()}
f10 = {'Name':'Coconut Soup','Id':secrets.randbits(100),'Values':generatevalues()}
f11 = {'Name':'Curry','Id':secrets.randbits(100),'Values':generatevalues()}
f12 = {'Name':'Fried Rice','Id':secrets.randbits(100),'Values':generatevalues()}

R4 = {'Name':'TemmiThai','Img':'https://www.tripsavvy.com/thmb/u69NPH6GnstXYejIWfatjnmoJa4=/950x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/GettyImages-475991769-591b7d8f5f9b58f4c06dceab.jpg','Foods':[f7,f8,f9,f10,f11,f12],'Adress':'505 burger lane','Hours':'9am-10pm'}
data['TemmiThai'] = R4


# IN[]
with open(os.path.join(cwd,"Restraunt.json"),'a+') as f:
     User_list = json.dump(data,f,indent=5)