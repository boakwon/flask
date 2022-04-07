from flask import Flask, request, make_response, redirect, abort, render_template, url_for, session
from flask import Flask, request, make_response, redirect, abort, render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'    # 防止CSPR
bootsrtap = Bootstrap(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')  # 连数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'


# # 动态路由
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s!</h1>' % name


# # 请求上下文
# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent


# 响应
# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400


# # 设置了 cookie
# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response


# # 重定向
# def index():
#     return redirect('http://www.example.com')


# @app.route('/user/<id>')
# def get_user(id):
#     abort(404)


# 渲染
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)


# 表单
# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('index.html', form=form, name=name)


# shell不用导入
# @app.shell_context_processor
# def make_shell_context():
#     return dict( db=db, User=User, Role=Role)
#
# # 数据库
# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role')
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# db.create_all()
#
# admin_role = Role(name='Admin')
# mod_role = Role(name='Moderator')
# user_role = Role(name='User')
# user_john = User(username='john', role=admin_role)
# user_susan = User(username='susan', role=user_role)
# user_david = User(username='david', role=user_role)
#
# db.session.add(admin_role)
# db.session.add(mod_role)
# db.session.add(user_role)
# db.session.add(user_john)
# db.session.add(user_susan)
# db.session.add(user_david)
#
# db.session.rollback()
# db.session.commit()
#
#
# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username = form.name.data)
#             db.session.add(user)
#             db.session.commit()
#             session['known'] = False
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html',
#             form = form, name = session.get('name'),
#             known = session.get('known', False))



if __name__ == '__main__':
    app.run(debug=True)
