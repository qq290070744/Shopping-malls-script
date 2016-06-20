#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
a={'iphone':5000,'macpc':8000,'kafei':20,'paoche':500000,'q':'退出'}
hua=0
g=open('goods.txt','w')
g.write('购买的商品列表--------------')
g.close()


print ("---------------商品列表-------------------")
for i in a:print (i,a[i])
while True:
        with open('rmb.txt') as f:
                for x in f:
                        rmb=int(x.strip().lstrip().rstrip(','))#从文件读取余额
                if rmb:
                        print ('你有%s元' % rmb)
                        pass
                        break

                else:
                    try:
                        rmb=int(input('帐号没有钱，请充钱，单位/元:'))

                    except ValueError:
                        print ("价钱只能输入数字")
                    else:
                        pass

                        break

while True:
        goods=input('请输入你要买的东西:')
        if goods=='q':
                with open('goods.txt') as gs:
                        for goods_list in gs:
                                if goods_list.strip() in a.keys():
                                    print ('-------------%s,%s rmb-----' % (goods_list,a[goods_list.strip()]))

                print ("你本次买了如上商品花了%s元钱,你 %s 了,还剩下 %s元钱" % (hua,a[goods],rmb))
                f=open('rmb.txt','w')#把余额写入文件
                f.write('%s' % rmb )
                sys.exit()
        elif goods not in a.keys():
                print ("不存在你要买的东西,请重新输入要购买的东西")
                continue
        elif a[goods]>rmb:
                print ("余额不足,购买失败")
                rm1b=rmb
                try:
                    rmb=int(input('帐号没有钱，请充钱，单位/元:'))
                except ValueError:
                        print ("价钱只能输入数字")
                else:

                    rmb=rmb+rm1b
                continue
        elif goods in a.keys():
                rmb=rmb - a[goods]
                print ("你买了 %s,还剩下 %s元钱" % (goods,rmb))
                hua=hua+a[goods]
                g=open('goods.txt','a')#把购买的商品追加到文件
                g.write('\n %s' %goods)
                g.close()



#与mysql交互的代码：
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

import MySQLdb,prettytable
import userlogin
user=userlogin.loginuser()
print ('user:',user)
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='jiang')
# cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
cur = conn.cursor()

reCount = cur.execute('select * from goods')

nRet = cur.fetchall()



a={'q':'退出'}

hua=0
with open('goods.txt','w') as g:
    g.write('购买的商品列表--------------')
    g.close()
#定义充钱函数
def chongqian():
    try:
        rmb=float (raw_input('帐号没有钱，请充钱，单位/元:'))

    except ValueError:
        print ("价钱只能输入数字")
    else:
        return rmb


print ("---------------商品列表-------------------")
x = prettytable.PrettyTable(["\033[32mgoods_名称\033[0m","\033[33mprice\033[0m"])
for i in nRet:
    x.add_row([i[0],i[1]])
    a[i[0]]=i[1]
    #print i[0], i[1]
x.add_row(['q',a['q']])
print (x
       )
#print a
'''
while True:
        with open('rmb.txt') as f:
                for x in f:
                        rmb=float(x.strip().lstrip().rstrip(','))#从文件读取余额
                try:

                    if rmb:
                            print ('你有%s元' % rmb)
                            pass
                            break

                    else:
                        rmb=chongqian()

                        break
                except NameError:
                    rmb=chongqian()
                    break
'''
cur = conn.cursor()
reCount = cur.execute("select * from userpass where username='%s'"%user)
rmb=cur.fetchall()[0][3]
print ('rmb:',rmb)
while True:
        goods=raw_input('请输入你要买的东西:')
        if goods=='q':#如果退出打印商品列表和余额
                with open('goods.txt') as gs:
                        y = prettytable.PrettyTable(["\033[32mgoods_名称\033[0m", "\033[33mprice\033[0m"])
                        for goods_list in gs:
                                if goods_list.strip() in a.keys():
                                    y.add_row([goods_list,a[goods_list.strip()]])
                                    #print ('---------%s,%s rmb-----' % (goods_list,a[goods_list.strip()]))
                        print (y)


                print ("你本次买了如上商品花了%s元钱,你 %s 了,还剩下 %s元钱" % (hua,a[goods],rmb))
                #with open('rmb.txt','w') as f:#把余额写入文件
                 #   f.write('%s' % rmb )
                reCount = cur.execute("update userpass set rmb =%s where username='%s' " % (rmb,user))
                conn.commit()
                sys.exit()
        elif goods not in a.keys():
                print ("不存在你要买的东西,请重新输入要购买的东西")
                continue
        elif a[goods]>rmb:
                print ("余额不足,购买失败")
                rmb=chongqian()+rmb
                continue
        elif goods in a.keys():
                rmb=rmb - a[goods]
                print ("你买了 %s,还剩下 %s元钱" % (goods,rmb))
                hua=hua+a[goods]
                with open('goods.txt','a') as g:#把购买的商品追加到文件
                    g.write('\n %s' %goods)
                    g.close()



cur.close()
conn.close()
