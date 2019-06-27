from flask import Flask, request, redirect

import cgi
import os
import jinja2
 
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir))

app = Flask(__name__)
app.config['DUBUG'] = True

@app.route("/", methods=['GET', "POST"])
def display_header():
    template = jinja_env.get_template('header.html')
    return template.render()

@app.route("/")
def dis_sign():
    template = jinja_env.get_template('username.html')
    return template.render
@app.route("/welcome")
def welcome():
    template = jinja_env.get_template('complete.html')
    return template.render()


    
