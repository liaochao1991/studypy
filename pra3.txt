三、循环判断练习

练习1
1. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？  1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去  掉不满足条件的排列。
[root@server2 py]# cat su.py
#!/usrl/bin/python

b=range(1,4)
b=range(1,4)

for x in xrange(1,5):
    for y in xrange(1,5):
        for z in xrange(1,5):
            if x !=y and x !=z and y !=z:
		print ("%s%s%s") %(x,y,z),

[root@server2 py]# python su.py
123 124 132 134 142 143 213 214 231 234 241 243 312 314 321 324 341 342 412 413 421 423 431 432
2. 打印出所有的“水仙花数”,所谓“水仙花数”是指一个三位数,其各位数字立方和等于该数本身。例如：153是一个“水仙花数”,因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数,每个数分解出个位,十位,百位。

[root@server2 py]# cat shui.py
#!/usr/bin/python

for i in xrange(100,1000):
    sum=0
    for n in str(i):
      sum += int(n)**3
    if sum == i:
      print sum，

[root@server2 py]# python shui.py
153 370 371 407

3. 两个乒乓球队进行比赛,各出三人。甲队为a,b,c三人,乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比,c说他不和x,z比,请编程序找出三队赛手的名单

[root@server2 py]# cat abc.py
#!/usr/bin/python
import itertools

jia='abc'
yi='xyz'

for i in itertools.permutations(yi):
	if i[0] !='x' and i[2] !='x' and i[2] !='z':
		print ("a VS %s,b VS %s,c VS %s"  %(i[0],i[1],i[2]))

[root@server2 py]# python abc.py
a VS z,b VS x,c VS y

练习2
1. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数,应先找到一个最小的质数i,然后按下述步骤完成：
(1)如果分解后商为1,则说明分解质因数的过程已经结束,打印出即可。
(2)如果商不为1,则应打印出i的值,并用n除以i的商,作为新的正整数进行分解,
　重复执行第一步。
(3)如果n不能被i整除,则i的值加1,重复执行第一步。
[root@server2 py]# cat zhisu.py
def fun(num):
    for i in range(2, num/2+1):
        if num % i == 0:
            print(i),
            print("*"),
            return fun(num/i)
    print(num),

if __name__ == '__main__':
    num = input("Please input a number: ")
    fun(num

2. 猴子吃桃问题：猴子第一天摘下若干个桃子,当即吃了一半,还不瘾,又多吃了一个，第二天早上又将剩下的桃子吃掉一半,又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时,见只剩下一个桃子了。求第一天共摘了多少。
程序分析：采取逆向思维的方法,从后往前推断。

[root@server2 py]# cat taozi.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

sum=1

print ('第10天的时候有1个桃子')
for i in range(9,0,-1):
   sum =(sum+1)*2
   print ('%s天吃之前有%s个桃子' %(i,sum))

print sum

[root@server2 py]# python taozi.py
第10天的时候有1个桃子
9天吃之前有4个桃子
8天吃之前有10个桃子
7天吃之前有22个桃子
6天吃之前有46个桃子
5天吃之前有94个桃子
4天吃之前有190个桃子
3天吃之前有382个桃子
2天吃之前有766个桃子
1天吃之前有1534个桃子
1534



