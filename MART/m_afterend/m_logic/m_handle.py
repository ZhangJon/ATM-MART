#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Jon Zhang 
@contact: zj.fly100@gmail.com
@site: 
@version: 1.0
@license: 
@file: m_handle.py
@time: 2017/3/23 20:14

there are many operation and showing
"""
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)

from m_afterend.m_db import m_show_info
from m_config import m_setting

def f_login(db_account_info,db_account_file):
    """
    logining function and lock the account.
    :param db_account_info:
    :param db_account_file:
    :return:
    """
    while True:
        PW_input_flag = True
        input_login_name = input("Please input your login_name:").strip()
        if len(input_login_name) == 0:
            continue
        while PW_input_flag:
            input_login_pw = input("Please input your password:").strip()
            if len(input_login_pw) != 0:
                PW_input_flag = False
        for i in db_account_info.keys():   #advice use the index, when you modify the list in the traverse the list will not go wrong
            print('11:',db_account_info)
            if db_account_info[i][1].strip() == input_login_name:
                if db_account_info[i][3].strip() == "3":
                    print("Your account is locked!Please to unlock!")
                    m_show_info.f_rewrite_account(db_account_info,db_account_file)
                    return
                elif db_account_info[i][2].strip() != input_login_pw:
                    db_account_info[i][3] = "%s\n"%(int(db_account_info[i][3]) + 1)
                else:
                    print("You are logining!")
                    db_account_info[i][3] = "0\n"
                    m_show_info.f_rewrite_account(db_account_info, db_account_file)
                    print(db_account_info[i][1])
                    return db_account_info[i][1]
        else:
            print("Your username or password is wrong!!You can to contact email:zj.fly100@gmail.com")
            print(db_account_info)
            continue

def f_shopping(db_commodity_info,one_person=None):
    """
    function of shopping
    :param db_commodity_info:
    :param one_person:
    :return:
    """
    dict_shopping_list = {}
    print("-------------------------------------------------")
    print("+               +")
    print("+               +")
    print("+           hello,%s                 +" % one_person)
    print("+   welcome to the ***** supermart   +")
    print("+               +")
    print("+               +")
    print("-------------------------------------------------")
    while True:
        for i in db_commodity_info.keys():
            for j in db_commodity_info[i]:
                print(j, end='')
        choice_id = input("Please input one product's id:")
        choice_num = input("Please input the number(default 1):")
        for k in db_commodity_info.keys():
            print('choice_id:',choice_id)
            print('k:',k)
            print('db_commodity_info:',db_commodity_info)
            print('db_commodity_info[k][0]:',len(db_commodity_info[k][0]))
            if choice_id == db_commodity_info[k][0].strip():
                if choice_id not in dict_shopping_list.keys():
                    print('1:',choice_id)
                    dict_shopping_list[choice_id] = [db_commodity_info[k][1].strip(),db_commodity_info[k][2].strip(),int(choice_num)]
                    print('2:',dict_shopping_list)
                else:
                    dict_shopping_list[choice_id] = [dict_shopping_list[choice_id][0],dict_shopping_list[choice_id][1],dict_shopping_list[choice_id][2] + int(choice_num)]
                    print('3:', dict_shopping_list)
        print("f_shopping(db_commodity_info,one_person=None):",dict_shopping_list)
        go_on_flag = input("GO ON?!(y/n)")
        if go_on_flag == 'y':
            continue
        else:
            return dict_shopping_list

def f_pay_bill(dict_shopping_list,login_name):
    total_price = 0
    print("f_pay_bill(dict_shopping_list):",dict_shopping_list)
    for i in dict_shopping_list.keys():
        total_price += float(dict_shopping_list[i][1]) * dict_shopping_list[i][2]
    print("%s's commodities Total prices:%s"%(login_name,total_price))
    payment_flag = 'ATM_function(total_price)'
    return payment_flag



