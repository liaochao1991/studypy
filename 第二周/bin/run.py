#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/12/1 21:13
# @Author : liaochao
# @File   : run.py

from bin import server_action


Agroup=["10.0.0.1:8080","10.0.0.2:8080"]
Bgroup=["192.168.0.1:8080","192.168.0.2:8080"]

'''0代表切下,1代表切上去,2代表维持现状'''
choose = [
    ("切上A组服务器",server_action.aServer,Agroup,1),
    ("切下A组服务器", server_action.aServer,Agroup,0),
    ("切上B组服务器",server_action.aServer,Bgroup,1),
    ("切下B组服务器",server_action.aServer,Bgroup,0),
]

s=True
def entrance():
    '''发布程序交互入口'''
    for index,i in enumerate(choose):
        print (index,i[0])
    while s:
        yunwei=input("天王盖地虎，请选择 >>: ")
        if yunwei.isdigit():
            yunwei=int(yunwei)
            if yunwei >= 0 and yunwei <= len(choose):
                #运行操作配置文件函数
                choose[yunwei][1](choose[yunwei][2],choose[yunwei][-1])
                break
            else:
                print("未知的选择，0|1|2|3")
                continue

        else:
            print("请输入选择的序号是数字")
            continue

