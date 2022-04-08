from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    # user = {'username': 'Miguel'}  #用户
    posts = [ #帖子
        {
            'author': {'username':'John'},  # 用户信息
            'body': 'Beautiful day im Portland'  # 发表内容
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avergers movie was so cool'
        }
    ]
    return render_template('index.html', tltle='home',  posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password.')

        login_user(user, remember=login_form.remember_me.data)
        return redirect(url_for("index"))
    return render_template('login.html', tltle='login', form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))