# 作者: 大数据 浪哥
# 2025年07月12日01时47分02秒
# 1054074422@qq.com

#1.整数
a=2
b=2
print(id(a))
print(id(b))
print(a is b)
print('-'*50)

#2.浮点数
e=123456789987445556654646.1
f=123456789987445556654646.1
print(id(e))
print(id(f))
print(e is f)
print('-'*50)

#3.字符串
c='hello'
d='hello'
print(id(c))
print(id(d))
print(c is d)
print('-'*50)

#4.列表
g=[1,2,3,4,5]
h=[1,2,3,4,5]
print(id(g))
print(id(h))
print(g is h)
print('-'*50)

#5.元组
i=(1,2,3,4,5)
j=(1,2,3,4,5)
print(id(i))
print(id(j))
print(i is j)
print('-'*50)

#6.字典
k={'name':'zhangsan','age':18}
l={'name':'zhangsan','age':18}
print(id(k))
print(id(l))
print(k is l)    #字典是可变的，所以id不一样
print('-'*50)


#7.集合
m=set([1,2,3,4,5])
n=set([1,2,3,4,5])
print(id(m))
print(id(n))
print(m is n)
print('-'*50)


#8.布尔值
o=True
p=True
print(id(o))
print(id(p))
print(o is p)
print('-'*50)

