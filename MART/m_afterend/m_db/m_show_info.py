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
    #TODO:error in make the list
    with open(message_file) as message_file_r:
        for i in message_file_r:
            print('0:',i)
            print('0:', type(i))
            i = i.replace("		","		-")
            print('1:', i)
            print('1:', type(i))
            i = i.split("-")
            print('2:',i)
            print('2:', type(i))
            list_message_info.append(i)
    for j in range(len(list_message_info)):
        dict_message_info[str(j)] = list_message_info[j]
    return dict_message_info

# var_commodity_info = r"F:\PycharmProjects\GitHub\BANK_MART\commodity_list.txt"
# f_make_info(var_commodity_info)