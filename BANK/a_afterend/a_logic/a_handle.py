#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Jon Zhang 
@contact: zj.fly100@gmail.com
@site: 
@version: 1.0
@license: 
@file: a_handle.py
@time: 2017/3/26 13:53


there are many operation and showing
"""
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)

from a_afterend.a_db import a_show_info
from a_config import a_setting

def f_login(db_account_info,db_account_file):
    """
    logining function and lock the account.
    :param db_account_info:
    :param db_account_file:
    :return:
    """
    while True:
        PW_input_flag = True
        input_login_name = input("Please input your Card_num:").strip()
        if len(input_login_name) == 0:
            continue
        while PW_input_flag:
            input_login_pw = input("Please input your password:").strip()
            if len(input_login_pw) != 0:
                PW_input_flag = False
        for i in db_account_info.keys():   #advice use the index, when you modify the list in the traverse the list will not go wrong
            #print('11:',db_account_info)
            if db_account_info[i][0].strip() == input_login_name:
                if db_account_info[i][3].strip() == "3":
                    print("Your account is locked!Please to unlock!")
                    a_show_info.f_rewrite_mess(db_account_info,db_account_file)
                    return
                elif db_account_info[i][2].strip() != input_login_pw:
                    db_account_info[i][3] = "%s\n"%(int(db_account_info[i][3]) + 1)
                else:
                    print("You are logining!")
                    db_account_info[i][3] = "0\n"
                    a_show_info.f_rewrite_mess(db_account_info, db_account_file)
                    print(db_account_info[i][1].strip())
                    return db_account_info[i][0].strip(),db_account_info[i][1].strip()
        else:
            print("Your username or password is wrong!!You can to contact email:zj.fly100@gmail.com")
            #print(db_account_info)
            continue

def f_matchInfo(recevier_CID,recevier_name,db_account_info):
    for i in db_account_info.keys():
        if recevier_CID == db_account_info[i][0].strip():
            if recevier_name == db_account_info[i][1].strip():
                return True

def f_compareSize(CID,cash,db_limit_info):
    for i in db_limit_info.keys():
        if CID == db_limit_info[i][0].strip():
            if float(db_limit_info[i][1]) >= cash:
                balance = float(db_limit_info[i][1]) - cash
                return balance,i

def f_enquire(CID,login_name,db_limit_info):
    for i in db_limit_info.keys():
        if CID == db_limit_info[i][0].strip():
            print("%s's account(%s) balance is %s" %(login_name,CID,db_limit_info[i][1].strip()))

def f_withdraw(CID,login_name,db_limit_info,db_limit_file):
    withdraw_num = int(input("Please input cash number:"))
    total_withdraw = withdraw_num*5/100 + withdraw_num
    balance, i = f_compareSize(CID,total_withdraw,db_limit_info)
    if balance:
        db_limit_info[i][1] = "%s\n" % balance
        a_show_info.f_rewrite_mess(db_limit_info, db_limit_file)
        print("%s's account(%s) balance is %s" % (login_name, CID, balance))

def f_deposit(CID,login_name,db_limit_info,db_limit_file,cash=None):
    if not cash:
        cash = int(input("Please input cash number:"))
    for i in db_limit_info.keys():
        if CID == db_limit_info[i][0].strip():
            balance = float(db_limit_info[i][1]) + cash
            db_limit_info[i][1] = "%s\n" % balance
            a_show_info.f_rewrite_mess(db_limit_info, db_limit_file)
            print("%s's account(%s) balance is %s" % (login_name, CID, balance))

def f_transfer(CID,login_name,db_limit_info,db_limit_file,db_account_info):
    recevier_CID = input("Please input receiver's CID:")
    recevier_name = input("Please input receiver's name:")
    trransfer_cash = int(input("Please input cash number:"))
    right_flag = f_matchInfo(recevier_CID,recevier_name,db_account_info)
    balance, i = f_compareSize(CID, trransfer_cash, db_limit_info)
    print('11:',right_flag,balance,i)
    if right_flag and balance:
        db_limit_info[i][1] = "%s\n" % balance
        a_show_info.f_rewrite_mess(db_limit_info, db_limit_file)
        f_deposit(recevier_CID,recevier_name,db_limit_info,db_limit_file,trransfer_cash)

