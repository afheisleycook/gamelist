from turtle import home
from flask import( Flask, request, render_template)
from  .View import home
app = Flask(__name__)

@app.route('/')
def home():
    render_template('home.html')

#Make sure that flask_login and bcrypt are installed
from flask_login import login_user,logout_user,current_user,UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

#Position all of this after the db and app have been initialised
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
h
@login_manager.user_loader
def user_loader(user_id):
    #TODO change here
    return User.query.get(user_id)
