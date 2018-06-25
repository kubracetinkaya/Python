sozluk={"Python":"Eğlenceli bir dil","Php":"Script dili","Java":"Compile edilen bir dil"}

print(sozluk["Python"])

for i in sozluk.items():
    print(i)



dersler={"Ahmet":["Veri Tabanları","İşletim Sistemleri"],"Mehmet":["Diferansiyel denklemler","Nesne tabanlı programlama"],"Veli":"Lineer cebir"}
isim=input("İsim giriniz")
print("{} in aldığı dersler:".format(isim))
for i in (dersler[isim]):
    print(i)
