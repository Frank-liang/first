#!/usr/bin/env python

def leijia(x,y):
    a = 0
    for i in xrange(x,y+1):
        a += i
    return a

def jiecheng(x,y):
    a = x
    for i in xrange(x,y+1):
        a *= i
    return a    

def jiafa(x,y):
    return x + y

def jianfa(x,y):
    return x - y 

matrix = {
    "leijia":leijia,
    "jiecheng":jiecheng,
    "jiafa":jiafa,
    "jianfa":jianfa
}

def sizeyunsuan(x,oper,y):
    if oper in matrix:
        return matrix[oper](x,y)
    else:
        return "Invalid operator"
if __name__ == '__main__':
    x = int(raw_input("Input x: "))
    oper = raw_input("Input operator: ")
    y = int(raw_input("Input y: "))
    print sizeyunsuan(x,oper,y)
