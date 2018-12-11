#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/12/10 22:54
# @Author : liaochao
# @File   : csGame.py
import random
import sys
'''CS模拟大战'''
'''元组中第一个字段代表装备名称、第二个字段代表价格，第三个字段代表伤害,第四个代表防御力'''
shop=[
    ("B43",6000,50,0),
    ("AK47",5000,40,0),
    ("沙漠之鹰", 7000, 40, 0),
    ("巴雷特", 12000, 100, 0),
    ("clothes",4000,0,30),
]
class Role(object):
    '''定义名字、角色、武器、初始生命值、初始金钱'''
    def __init__(delf,name,role,life_value=100,money=15000):
        delf.name=name
        delf.role=role
        delf.life_value=life_value
        delf.money=money


    def get_shot(self,damage,clothes=0):
        '''中枪后 ,根据枪的类型,和防弹衣掉血'''
        if int(clothes) >= int(damage):
             print ("渣渣")
             return 0
        else:
             print("ah...,我中枪了")
             self.life_value =self.life_value-(damage-clothes)
             print ("%s剩余生命值:%s" %(self.name,self.life_value))
             if self.life_value <=0:
                 print ("你死了。。,%s全军覆没" %self.role)
                 exit()
        return self.life_value
    def buy_gun(self):
        print("序列","武器/防弹衣","价格","伤害","防御力")
        for index,k in  enumerate(shop):
            print (index,k)
        choose =input("请输入你要买的装备>>:")
        if choose.isdigit():
            choose=int(choose)
            if 0<=choose<=len(shop):
                #枪名
                self.gunname = shop[choose][0]
                #剩余金币
                money = self.money-(shop[choose][1])
                #伤害力
                att = shop[choose][2]
                #防御力
                defense = shop[choose][-1]
            else:
                print("未能识别到的商品")
                sys.exit()
        else:
            print("请输入序列号")
            sys.exit()
        print ("刚刚你买入了%s,花了%s块,剩余：%s" %(self.gunname,shop[choose][1],money))

        return (self.gunname,att,defense,money)
#生成2个对立角色

r1=Role("jack","警察",)
r2=Role("Tom","土匪",)
print ("%s你的身份是%s,请购买装备!!" %(r1.name,r1.role))
result1 = r1.buy_gun()
print ("%s你的身份是%s,请购买装备!!" %(r2.name,r2.role))
result2 = r1.buy_gun()
acc1=int(result1[1])
acc2=int(result2[1])



def shot():
    s = True
    while s:
        shoot = random.randint(1,100)
        if shoot % 2 == 0:
            print("%s 抢先攻击,掏出了%s,就是几枪" % (r1.name,result1[0]))
            print("哒哒哒。。。。。")
            r1.get_shot(acc1)
        else:
            print("%s 抢先攻击,掏出了%s,就是几枪" % (r2.name,result2[0]))
            print("哒哒哒。。。。。")
            r2.get_shot(acc2)

if __name__ == '__main__':
    shot()
