import datetime
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, flash, request, render_template, make_response, url_for, redirect
from flask_login import UserMixin, login_user, current_user, logout_user, login_required, LoginManager
from flask_session import Session
from flask_cors import CORS
import os
from werkzeug.security import generate_password_hash, check_password_hash

from forms import LoginForm, RegisterForm

load_dotenv('.env')
db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/assignment"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

Session(app)
db.init_app(app)
CORS(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)

    def is_active(self):
        return self.isActive

    def is_authenticated(self):
        return True

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.password}', {self.isActive})"


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        user = User.query.from_statement(
            db.text("SELECT * FROM user where email=:email and isActive=:is_active")
        ).params(email=email, is_active=True).first()

        if user is None:
            user = User(email=email, password=hashed_password, isActive=True)
            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True)
            flash('Register successful', 'info')
            return redirect(url_for('member'))
        else:
            flash('Email already exists!', 'danger')
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.from_statement(
            db.text("SELECT * FROM user where email=:email and isActive=:is_active")
        ).params(email=email, is_active=True).first()

        is_successful = check_password_hash(user.password, password)
        if user and is_successful:
            login_user(user, remember=True)
            flash('Login successful', 'info')
            return redirect(url_for('member'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', form=form)


@app.route("/member", methods=['GET', 'POST'])
@login_required
def member():
    if current_user.is_authenticated:
        return render_template('member.html', email=current_user.email)
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)
