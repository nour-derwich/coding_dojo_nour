from flask_app import app
from flask import render_template,redirect,request , session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=['post'])
def create():
    if User.validate_user(request.form) == False:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data ={
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':pw_hash
    }
    return_form_db=User.create(data)
    session['user_id']=return_form_db
    print("-"*20, return_form_db ,"-"*20)
    return  redirect('/')
    