#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Jon Zhang 
@contact: zj.fly100@gmail.com
@site: 
@version: 1.0
@license: 
@file: a_user_main.py
@time: 2017/3/26 14:05

this is the enter of the user
"""
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from a_config import a_setting
from a_afterend.a_db import a_show_info
from a_afterend.a_logic import a_handle

db_account_file = a_setting.var_account_info
db_account_info = a_show_info.f_make_info(db_account_file)
db_limit_file = a_setting.var_limit_info
db_limit_info = a_show_info.f_make_info(db_limit_file)

def f_main(db_account_info,db_account_file):
    """
    this is the enter of the user
    :param db_account_info:
    :param db_account_file:
    :return:
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    CID,login_name = a_handle.f_login(db_account_info,db_account_file)
    while True:
        print("""
        operation menu
            1、enquire
            2、withdraw
            3、transfer
            4、deposit
            5、exit
        """)
        choice_function = input("Please choose one function")
        if choice_function == '1':
            a_handle.f_enquire(CID,login_name,db_limit_info)
        elif choice_function == '2':
            a_handle.f_withdraw(CID,login_name,db_limit_info,db_limit_file)
        elif choice_function == '3':
            a_handle.f_transfer(CID, login_name, db_limit_info, db_limit_file, db_account_info)
        elif choice_function == '4':
            a_handle.f_deposit(CID, login_name, db_limit_info, db_limit_file)
        elif choice_function == '5':
            sys.exit()

if __name__ == "__main__":
    f_main(db_account_info,db_account_file)