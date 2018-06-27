pi=3.14
yaricap=2
cevre=2*pi*yaricap

print("Dairenin cevresi",cevre)

alan=pi*yaricap**2

print("Dairenin alanı",alan)

print(('6'+'5')*4)

print(4**(-1/2))

print(4*str(4))

def f(x):
    """bu bir açıklamadır"""
    y=x+5
    return y

print(3*str(f(1-3)))

help(f)

def kareAl(x):
    y=x**2
    return y

print(kareAl(5))

def kokAl(x):
    y=x**0.5
    return y

print(kokAl(25))

girilen=input("Bir sayı giriniz")
print(2*girilen)

def ortalama(x,y):
    ort=(x+y)/2
    return ort

print(ortalama(5,3))





