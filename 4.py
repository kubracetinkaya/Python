yas=int(input("Yasinizi Giriniz:\n"))

if yas>=18:
    print("Mekana girebilirsin")

else:
    print("Mekana girememzsin")

puan=int(input("Notunuzu giriniz"))

if puan>=90:
    print("Harf notunuz AA")

elif puan>=80:
    print("Harf notunuz BB")

elif puan>=70:
    print("Harf notunuz CC")

elif puan>=60:
    print("Harf notunuz DD")

else:
    print("Kaldınız")
    
