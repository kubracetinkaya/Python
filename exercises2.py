def yükseklik():
    g=10
    h= (hız*süre)-(1/2*g*süre**2)
    return h




while(True):
    
    hız=int(input("Cismin ilk hızını giriniz"))
    
    süre=int(input("Cismin yüksekliğe çıkma süresini giriniz"))

    if(hız!=0 and süre!=0):
        print(yükseklik())
        
    elif(hız==0 and süre!=0):
        print("Hız sıfır olamaz")
        
    elif(süre==0 and hız!=0):
        print("Süre sıfır olamaz")

    else:
        print("Hız ve süre sıfır olamaz")
        break


def periyot():
    pi=3.14
    g=10
    T=2*pi*(l/g)**0.5
    return T

while(True):
    l=int(input("Sarkacın uzunluğunu giriniz"))

    if(l>0 and l!=0):
        print(periyot())
    else:
        print("Uzunluk negatif ya da sıfır olamaz")
        break









    
    
    
             
            
