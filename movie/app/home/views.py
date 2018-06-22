# -*- coding:utf-8 -*-
from functools import wraps

from wtforms import ValidationError

__author__ = 'zhangzhibo'
__date__ = '202018/5/18 9:48'

from flask import Response, render_template, redirect, url_for, flash, session, request
from . import home
from werkzeug.security import generate_password_hash, check_password_hash


@home.route("/")
def index():
    # return render_template('home/index.html')
    login_flag = 0
    user_name = ''
    if session.get('user'):
        login_flag = 1
        user_name = session['user']
    return render_template("home/index.html", login_flag=login_flag, username=user_name)

# @home.route("/login/")
# def home_login():
#    return render_template("home/login.html")


# 登陆装饰器
def user_login_req(func):
   @wraps(func)
   def decorated_function(*args, **kwargs):
      if "user" not in session:
         return redirect(url_for("home.login", next=request.url))
      return func(*args, **kwargs)
   return decorated_function

@home.route("/test")
@user_login_req
def test():
    return Response("hello, world")

@home.route("/logout/")
def logout():
   session.pop("user", None)
   session.pop("user_id", None)
   return redirect(url_for("home.home_login"))

# @home.route("/register")
# def register():
#    return render_template("home/register.html")



@home.route("/animation/")
def animation():
   return render_template("home/animation.html")

@home.route("/play/")
def play():
   login_flag = 0
   user_name = ''
   if session.get('user'):
       login_flag = 1
       user_name = session['user']
   return render_template("home/play.html", login_flag=login_flag, username=user_name)


@home.route("/mysql/<string:username>/<string:email>/<string:address>/")
def home_add(username,email,address):
    from app import db
    from app.models import UserInfo
    admin = UserInfo(username, email, address)
    db.session.add(admin)
    db.session.commit()
    return render_template('index.html')


@home.route("/login/", methods=["GET", "POST"])
def home_login():
   from .forms import LoginForm
   from app.models import User
   form = LoginForm()
   if form.validate_on_submit():
       data = form.data
       name = data["name"]
       user = User.query.filter_by(name=name).first()
       # if check_password_hash(use.pwd,data["pwd"]):
       #     # flash("注册成功！", "ok")
       #     return redirect(url_for("home.index"))
       # # else:
       # #     raise ValidationError("用户名或密码错误!!")
       if user:
           if not user.check_pwd(data["pwd"]):
               flash("密码错误！", "err")
               return redirect(url_for("home.home_login"))
       else:
           flash("账户不存在！", "err")
           return redirect(url_for("home.home_login"))
       session["user"] = user.name
       session["user_id"] = user.id
       return redirect(url_for("home.index"))
   return render_template("home/wflogin.html", title = "wtform表单登录", form=form)

@home.route("/register/", methods=["GET", "POST"])
def register():
   from app.home.forms import RegisterForm
   from app.models import User
   from app import db
   form = RegisterForm()
   if form.validate_on_submit():
      data = form.data
      user = User(
         name = data["name"],
         email = data["email"],
         phone = data["phone"],
         pwd = generate_password_hash(data["pwd"]),

      )
      db.session.add(user)
      db.session.commit()
      # flash("注册成功！", "ok")
      return redirect('/home/login')
   return render_template("home/register.html", form = form)