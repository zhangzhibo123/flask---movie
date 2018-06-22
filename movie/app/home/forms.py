# -*- coding:utf-8 -*-
__author__ = 'zhangzhibo'
__date__ = '202018/5/18 9:47'

from flask_wtf import  FlaskForm
from wtforms import  StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Regexp
from app.models import User

"""
登陆表单
1. 账号  name
2. 密码  pwd
3. 登陆按钮
"""

class LoginForm(FlaskForm):
   name = StringField(label="账号",
                  validators=[DataRequired("麻烦请输入账号信息")],
                  description="账号",
                  render_kw={
                   "class":"form-control",
                     "placeholder":"请输入账号",
                    }
   )
   pwd = PasswordField(
                  label="密码",
                  validators=[DataRequired("麻烦请输入密码")],
                      description="密码",
                      render_kw={
                     "class":"form-control",
                     "placeholder":"请输入密码！"
                  }
   )
   submit = SubmitField(
                      "登录",
                      render_kw={
                     "class":"btn btn-primary"
                  }
   )


'''
注册表单
1. 昵称  name
2. 邮箱  email
3. 手机   phone
4. 密码  pwd
5. 重置密码 repwd
6. 注册按钮
'''
class  RegisterForm(FlaskForm):

   name = StringField(label="昵称",
                  validators=[DataRequired("麻烦请输入昵称信息")],
                  description="昵称",
                  render_kw={
                     "class": "form-control input-lg",
                     "placeholder": "请输入昵称",
                  }
   )
   email = StringField(label="邮箱",
                  validators=[
                             DataRequired("麻烦请输入邮箱信息"),
                             Email("邮箱格式不正确！")
                           ],
                  description="邮箱",
                  render_kw={
                     "class": "form-control input-lg",
                     "placeholder": "请输入邮箱",
                  }
   )
   phone = StringField(label="手机",
                  validators=[
                             DataRequired("麻烦请输入手机号码信息"),
                             Regexp("1[3458]\\d{9}", message="手机格式不正确")
                           ],
                  description="手机",
                  render_kw={
                     "class": "form-control input-lg",
                     "placeholder": "请输入手机号码",
                  }
   )
   pwd = PasswordField(label="密码",
                  validators=[
                     DataRequired("请输入密码信息"),

                  ],
                  description="密码",
                  render_kw={
                     "class": "form-control",
                     "placeholder": "请输入密码",
                  }
                  )
   repwd = PasswordField(label="确认密码",
                  validators=[
                     DataRequired("请输入确认密码信息"),
                      EqualTo('pwd', message="两次密码输入不一致！")
                  ],
                  description="密码",
                  render_kw={
                     "class": "form-control",
                     "placeholder": "请输入确认密码",
                  }
                  )
   submit = SubmitField(
      "注册",
      render_kw={
         "class": "btn btn-lg btn-success",
      }
   )

   def  validate_name(self, field):
      name = field.data
      user = User.query.filter_by(name=name).count()
      if user == 1:
         raise ValidationError("昵称已经存在!")

   def  validate_email(self, field):
      email = field.data
      user = User.query.filter_by(email=email).count()
      if user == 1:
         raise ValidationError("邮箱已经存在!")

   def validate_phone(self, field):
      phone = field.data
      user = User.query.filter_by(phone=phone).count()
      if user == 1:
         raise ValidationError("手机已经存在!")


