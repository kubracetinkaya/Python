def merhaba():
    print("Merhaba kubra")

merhaba()


def faktoriyel(sayi):
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel*=i
    print("Faktöriyeli",faktoriyel)

fakt=int(input("Sayıyı giriniz"))

faktoriyel(fakt)


def ad():
    isim=input("Adınız nedir?")
    return isim            

print("Merhaba {} Nasılsın?".format(ad()))

def kokbul(a,b,c):
    delta=(b*b-4*a*c)

    if (delta<0):
        print("Reel kök yoktur")
        return                 #bu return'ü fonksiyonu bitirmek için kullandık

    x1=(-b - delta**0.5)/(2*a)
    x2=(-b + delta**0.5)/(2*a)

    return(x1,x2)                #yani kökbul fonksiyonundan dönen değer x1 ve x2

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

sonuc=kokbul(a,b,c)

print("Denklemin kökleri",sonuc)


