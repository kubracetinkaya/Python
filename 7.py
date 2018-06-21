String="kubra"

for i in String:        #Stringi gez
    print(i)
    
liste=[25,98,"cetinkaya"]

for i in liste:
    print(i)
    
for i in range(10):    #range fonksiyonu belirtilen aralığı yazdırır
    print(i)

for i in range(2,5): 
    print(i)

for i in range(2,10,3):  #sondaki parametre artış miktarıdır
    print(i)

print(*range(10))      #print içinde kullanımı bu şekildedir
print(*range(2,5))
print(*range(2,10,3))

for i in range(1,10):
    print(i*"*")

faktoriyel=1

while True:
    sayi=int(input("Bir sayi giriniz"))

    if(sayi<=0):
        print("Lütfen pozitif bir sayi giriniz")
    else:
        for i in range(1,sayi+1):  #range fonksiyonu sondaki aralığı dahil etmediği için sayi+1 yaptık
            faktoriyel*=i

        print("Faktöriyel",faktoriyel)
        break
