#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import jinja2
import cgi

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
        self.render("stephw6Page1.html")

class SabHandler(BaseHandler):
    def get(self):
        self.render("stephw6Page2.html")
        word1=cgi.escape(self.request.get("word1"))
        word2=cgi.escape(self.request.get("word2"))
        char1=list(word1)
        char2=list(word2)
        i=0
        result=""
        if len(char1)==len(char2):
            while i < len(char1):
                result+=char1[i]+char2[i]
                i+=1
        elif len(char1)<len(char2):
            while i < len(char1):
                result+=char1[i]+char2[i]
                i+=1
            while i < len(char2):
                result+=char2[i] 
        else:
            while i < len(char2):
                result+=char1[i]+char2[i]
                i+=1
            while i < len(char1):
                result+=char1[i] 
        self.response.out.write(result)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ("/seni", SabHandler)
], debug=True)