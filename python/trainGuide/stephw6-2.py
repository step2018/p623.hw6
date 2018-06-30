#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2
import json,codecs
import os
import jinja2
import cgi
#from bs4 import BeautifulSoup

#with open("traindata2.xml") as traindata:
    #soup =BeautifulSoup(traindata, "xml")
#print(soup)

# read json file
f=codecs.open("trainData.json","r","utf-8")
json_dict=json.load(f)
print("json_dict:{}".format(type(json_dict)))
print(json_dict)
#json dict -> json String
print("json dict -> json String")
json_str = json.dumps(json_dict)
print("json_str:{}".format(type(json_str)))
print(json_str)
print("json String -> json dict")
json_dict2=json.loads(json_str)
print("json_dict2:{}".format(type(json_dict2)))
print(json_dict2)

        
    
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainHandler(BaseHandler):
    def get(self):
        self.render("stephw6-2Page1.html")

class SabHandler(BaseHandler):
    def get(self):
        self.render("stephw6-2Page2.html")
    

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/seni", SabHandler)
], debug=True)