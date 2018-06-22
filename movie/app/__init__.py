# -*- coding:utf-8 -*-
__author__ = 'zhangzhibo'
__date__ = '202018/5/18 9:36'

from flask import Flask, render_template, session
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint,url_prefix="/home")
app.register_blueprint(admin_blueprint,url_prefix="/admin")

# @app.route("/")
# def index():
#     return render_template('home/index.html')
@app.route("/")
def index():
    login_flag = 0
    user_name = ''
    if session.get('user'):
        login_flag = 1
        user_name = session['user']
    return render_template("home/index.html", login_flag=login_flag, username=user_name)

################### mysql control ################################

import pymysql
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] =\
	"mysql+pymysql://root:123456@127.0.0.1:3306/flask?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True
app.config['SECRET_KEY'] = "12345678"

db = SQLAlchemy(app)    #实例化db对象


################### mysql control ################################
