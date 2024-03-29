from werkzeug.urls import url_parse
from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Post


@app.route('/')
@app.route('/index')
# @login_required
def index():
    posts =Post.query.all() #帖子
    # result = user_schema.dump(posts)
    # return {"authors": result}
    return render_template('index.html', tltle='home',  posts=posts)



@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for("index"))
        login_user(user, remember=login_form.remember_me.data)
        #重定向到next页面
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netlopc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', tltle='login', form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,)
        user.set_password('form.password.data')
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)