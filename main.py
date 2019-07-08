from flask import Flask, request, redirect, url_for, render_template

import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True
 
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir))

app = Flask(__name__)
app.config['DUBUG'] = True

@app.route('/')
def base():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def sign_up():
    

    user_pass = request.form['password']
    verify_pass = request.form['verify_password']
    username = request.form['username']
    email_verify = request.form['email']

    password_error = ""
    verifypass_error = ""
    username_error = ""
    email_error = ""

            
    if user_pass == "":
        password_error = "Password cannot be left blank"
    if len(user_pass) <= 3 or len(user_pass) >= 20:
        password_error = "Password must contain more than 3 characters and less than 20 characters"
    if user_pass.count(" ") >= 1:
        password_error = "Password cannot contain a space"
        

    if verify_pass == "" or verify_pass != user_pass:
        password_error = "Passwords do not match"    
    if len(verify_pass) <= 3 and len(verify_pass) >= 20:
        verifypass_error = "Password must contain more than 3 characters and less than 20 characters"
    if verify_pass.count(" ") >= 1:
        verifypass_error = "Password cannot contain a space"  
    
    
    if username == "":
        username_error = "Username cannot be blank"
    if len(username) >=20 or len(username) <= 3:
        username_error = "Username must contain more than 3 characters and less than 20 characters"
    if username.count(" ") >= 1:
        username_error = "Username cannot contain a space"
    
    if len(email_verify) >= 1:
        if email_verify.count("@") != 1 or email_verify.count(".") != 1:
            email_error = "Email is invalid"
        
        


    if not username_error and not password_error and not verifypass_error and not email_error:
        #template = jinja_env.get_template("welcome.html")
        return render_template('welcome.html', username=username)
    # use count method for email. 
    else:
        #template = jinja_env.get_template('signup.html')
        return render_template('signup.html', username_error=username_error, password_error=password_error, verifypass_error = verifypass_error, email_error=email_error)


    #email if statement
app.run()