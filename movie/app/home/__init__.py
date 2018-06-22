# -*- coding:utf-8 -*-
__author__ = 'zhangzhibo'
__date__ = '202018/5/18 9:36'

from flask import Blueprint
home = Blueprint("home", __name__)
import app.home.views