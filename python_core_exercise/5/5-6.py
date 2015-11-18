#!/usr/bin/env python
#coding=utf-8

def jiafa(x,y):
    return x + y
def jianfa(x,y):
    return x - y
def chenfa(x,y):
    return x * y
def chufa(x,y):
    return x / y
def quyu(x,y):
    return x % y
def miyunsuan(x,y):
    return x ** y
operator = {
    "jiafa" : jiafa,
    "jianfa" : jianfa,
    "chenfa" : chenfa,
    "chufa" : chufa,
    "quyu" : quyu,
    "miyunsuan" : miyunsuan,
            }

def yunsuan(x,oper,y):
    if oper in operator:
        return operator[oper](x,y)
    else:
        return "Invanlid operator"
if __name__ == "__main__":
    x = int(raw_input("Input the number: "))
    oper = raw_input("Input the oper: ")
    y = int(raw_input("Input the num: "))
    print yunsuan(x,oper,y)


    

