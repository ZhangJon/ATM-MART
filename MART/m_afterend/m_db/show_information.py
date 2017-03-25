#!usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Jon Zhang 
@contact: zj.fly100@gmail.com
@site: 

@version: 1.0
@license: 
@file: show_information.py
@time: 2017-3-23 12:28

simulation the db
"""

def f_rewrite_account(dict_new_account,account_file):
    """
    change the info.
    :param dict_new_account:
    :param account_file:
    :return:
    """
    with open(account_file,'w') as account_file:
        for i in dict_new_account.keys():
            account_file.writelines(dict_new_account[i])
    return True


def f_make_info(message_file):
    """
    show the info.
    :param message_file:
    :return:
    """
    list_message_info = []
    dict_message_info = {}
    with open(message_file) as message_file_r:
        for i in message_file_r:
            i = i.replace("     ","     -").split("-")
            list_message_info.append(i)
    for j in range(len(list_message_info)):
        dict_message_info[j] = list_message_info[j]
    return dict_message_info
