#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/12/1 21:17
# @Author : liaochao
# @File   : server_action.py

import os
from .reload_nginx import reNginx

#项目路径
#dir_path=os.path.dirname(os.getcwd())
dir_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#配置文件路径
nginx_path="\conf\\nginx.conf"
tmp_nginx_path="\conf\\nginx.conf_tmp"
conf_dir=dir_path+nginx_path
tmp_conf_dir=dir_path+tmp_nginx_path


def aServer(group,status):
    #将从nginx.conf读取到的配置拿出来
    with open(conf_dir,'r', encoding='utf-8') as fd,open(tmp_conf_dir,'w', encoding='utf-8')as fd1:
        for items in fd:
            #根据传进来的ip组遍历ip
            for ip in group:
                #如果ip在该列表中
                if ip in items:
                    if status == 1: # 1为切上
                        #print ("准备切上去的服务器：%s" %ip)
                        if items.startswith("#"):
                            items=items.replace("#","",1)
                        else:
                            print("当前服务已经在线了,请勿再次操作")
                            exit()
                    if status == 0: # 0为切下
                        #print("准备切下去的服务器：%s" %ip)
                        if items.startswith("#"):
                            print("当前服务已经被切下了,请勿再次操作！")
                            exit()
                        else:
                            lines="#"+items
                            items=items.replace(items,lines)
            fd1.write(items)
    os.remove(conf_dir)
    os.renames(tmp_conf_dir,conf_dir)
    reNginx()






