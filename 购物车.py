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

