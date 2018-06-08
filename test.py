#!/usr/bin/python
# -*- coding: UTF-8 -*-

def func(a,b,*args,**kw):
	print 'a=',a,'b=',b,'args=',args,'kw=',kw

args=(1,2,3)

func(4,5,*args,key='value')

g = (x*x for x in range(10))

for n in g:
    print(n)

print("++++++++++++++++++")

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
	a,b = b,a+b
	n=n+1
    return 'done'

fib(6)
