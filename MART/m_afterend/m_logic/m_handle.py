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

there are many operation and showwing
"""
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)

from m_afterend.m_db import show_information
from m_config import setting

def f_login(db_account_info,db_account_file):
    """
    logining function and lock the account.
    :param account_info:
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
            if db_account_info[i][1] == input_login_name:
                if db_account_info[i][3] == "3":
                    print("Your account is locked!Please to unlock!")
                    show_information.f_rewrite_account(db_account_info,db_account_file)
                    return
                elif db_account_info[i][2] != input_login_pw:
                    db_account_info[i][3] = str(int(db_account_info[i][3]) + 1)
                else:
                    print("You are logining!")
                    db_account_info[i][3] = "0"
                    show_information.f_rewrite_account(db_account_info, db_account_file)
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
        for j in db_commodity_info.keys():
            if choice_id == db_commodity_info[j][0]:
                if choice_id not in dict_shopping_list.keys():
                    dict_shopping_list[choice_id] = [db_commodity_info[j][1],db_commodity_info[j][2],int(choice_num)]
                else:
                    dict_shopping_list[choice_id] = [db_commodity_info[j][1],db_commodity_info[j][2],db_commodity_info[j][3] + int(choice_num)]
        go_on_flag = input("GO ON?!(y/n)")
        if go_on_flag == 'y':
            continue
        else:
            return dict_shopping_list

def f_pay_bill(dict_shopping_list):
    ATM_limit_info = [1,100000]
    while True:
        total_price = 0
        one_person = f_login_ATM()
        print("one_person_ATM:", one_person)
        print(type(one_person))
        if one_person:
            for j in dict_shopping_list.keys():
                total_price += float(dict_shopping_list[j][1]) * dict_shopping_list[j][2]
            for i in range(len(ATM_limit_info)):
                print('1:', type(ATM_limit_info[i][0]))
                print('2:', ATM_limit_info[i][0])
                if ATM_limit_info[i][0] == one_person:
                    print(type(ATM_limit_info[i][1]))
                    if float(ATM_limit_info[i][1]) >= total_price:
                        ATM_limit_info[i][1] = str(float(float(ATM_limit_info[i][1])) - total_price)
                        rewrite_ATM_limit(ATM_limit_info, ATM_limit_file)
                        print("ATM_limit_info:", ATM_limit_info)
                        return True
                    else:
                        print("You have not much money to pay for:%s" % total_price)
                        flag = input("Change one card!?(y/n)")
                        if flag == "y":
                            break
                        else:
                            return False





