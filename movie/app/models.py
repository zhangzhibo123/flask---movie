# -*- coding:utf-8 -*-
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

__author__ = 'zhangzhibo'
__date__ = '202018/5/18 10:36'

from app import db

class UserInfo(db.Model):
    tablename__ = "userinfo"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(100))

    def __init__(self, username, email,address):
        self.username = username
        self.email = email
        self.address = address

    def __repr__(self):
        return '<User %r>' % self.username


#会员
class User(db.Model):
   __tablename__ = "user"
   id = db.Column(db.Integer, primary_key=True)  #编号
   name = db.Column(db.String(100), unique=True)
   pwd = db.Column(db.String(100))
   email = db.Column(db.String(100), unique=True)
   phone = db.Column(db.String(11), unique=True)
   info = db.Column(db.Text)
   face = db.Column(db.String(255))
   addtime = db.Column(db.DateTime, index=True, default=datetime.now)

   def __repr__(self):
      return "<User %r>" % self.name

   #验证密码，采用hash256加密算法保存密码
   def check_pwd(self, pwd):
      from werkzeug.security import check_password_hash
      return check_password_hash(self.pwd, pwd)

#管理员
class Admin(db.Model):
    tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<User %r>" % self.name


    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)

class Tag(db.Model):
   __tablename__ = "tag"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), unique=True)
   addtime = db.Column(db.DateTime, index=True, default=datetime.now)

   def __repr__(self):
      return "<Tag %r>" % self.name


if __name__ == '__main__':
    db.create_all()
