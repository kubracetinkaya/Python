a=input("Birinci sayi:")
b=input("İkinci sayi:")
c=input("Üçüncü sayi:")

print ("Sayilarin toplami:",a+b+c)  #a b ve cyi uçuca ekler

print("Sayilarin toplami:",int(a)+int(b)+int(c))  #bu şekilde sayilari toplar

ad=input("Kisinin adı:")
soyad=input("Kisinin soyadı:")
yas=input("Kisinin yasi:")

bilgiler=[ad,soyad,yas]

print(bilgiler)
print("Kisinin adi:",ad,"Kisinin soyadi:",soyad,"Kisinin yasi:",yas)

print("Kisinin adi:{}\n Kisinin soyadi:{}\n Kisinin yasi:{}" .format(bilgiler[0],bilgiler[1],bilgiler[2]))
#format metodu aldığı parametreyi {} arasına koyar

