# -*- coding:utf-8 -*-
__author__ = 'zhangzhibo'
__date__ = '202018/5/18 9:41'


from flask import Blueprint
admin = Blueprint("admin", __name__)



import app.admin.views