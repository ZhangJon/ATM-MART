#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Jon Zhang 
@contact: zj.fly100@gmail.com
@site: 
@version: 1.0
@license: 
@file: m_user_main.py
@time: 2017/3/23 20:46

this is the enter of the user
"""
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)
from m_config import setting
from m_afterend.m_db import show_information
from m_afterend.m_logic import m_handle

db_account_file = setting.var_account_info
db_account_info = show_information.f_make_info(db_account_file)
db_commodity_file = setting.var_commodity_info
db_commodity_info = show_information.f_make_info(db_commodity_file)

def f_main(db_account_info,db_account_file):
    """
    this is the enter of the user
    :param db_account_info:
    :param db_account_file:
    :return:
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    loginmart_flag = input(" Logining now ?(y/n)")
    if loginmart_flag == 'y':
        login_name = m_handle.f_login(db_account_info,db_account_file)
        dict_shopping_list = m_handle.f_shopping(db_commodity_info,login_name)
    else:
        dict_shopping_list = m_handle.f_shopping(db_commodity_info)

    payment_flag = m_handle.f_pay_bill(dict_shopping_list)