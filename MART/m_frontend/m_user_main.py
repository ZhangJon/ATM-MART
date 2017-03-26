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
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from m_config import m_setting
from m_afterend.m_db import m_show_info
from m_afterend.m_logic import m_handle

db_account_file = m_setting.var_account_info
db_account_info = m_show_info.f_make_info(db_account_file)
db_commodity_file = m_setting.var_commodity_info
db_commodity_info = m_show_info.f_make_info(db_commodity_file)

def f_main(db_account_info,db_account_file):
    """
    this is the enter of the user
    :param db_account_info:
    :param db_account_file:
    :return:
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    loginmart_flag = input(" Log in now ?(y/n)")
    if loginmart_flag == 'y':
        login_name = m_handle.f_login(db_account_info,db_account_file)
        dict_shopping_list = m_handle.f_shopping(db_commodity_info,login_name)
    else:
        dict_shopping_list = m_handle.f_shopping(db_commodity_info)
        login_name = m_handle.f_login(db_account_info, db_account_file)
    while True:
        payment_flag = m_handle.f_pay_bill(dict_shopping_list,login_name)
        if payment_flag:
            sys.exit("Welcome back again!")
        else:
            continue

if __name__ == "__main__":
    f_main(db_account_info,db_account_file)