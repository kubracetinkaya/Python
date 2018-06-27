i=1
while(i<6):
    j=1
    while(j<6):
        print(i,j,i*j*"*")
        j=j+1
    i=i+1

while(True):
    sayi1=int(input("İlk sayiyi giriniz"))
    sayi2=int(input("İkinci sayıyı giriniz"))
    if(sayi1>sayi2):
        print("Büyük olan",sayi1)
        break
    elif(sayi2>sayi1):
        print("Büyük olan",sayi2)
        break


def harf_notu(sınav):
    if(sınav>0 and sınav<54):
        x="FF"
    elif(sınav>55 and sınav<59):
        x="FD"
    elif(sınav>60 and sınav<69):
        x="DD"
    elif(sınav>70 and sınav<74):
        x="CC"
    elif(sınav>75 and sınav<79):
        x="CB"
    elif(sınav>80 and sınav<84):
        x="BB"
    elif(sınav>85 and sınav<89):
        x="BA"
    else:
        x="AA"
    return x

while(True):
    sınav=int(input("Sınav notunuzu giriniz"))

    z=harf_notu(sınav)
    print(z)
    break


def indeks():
    bki=(kilo)/(boy**2)
    
    if(bki>40.0):
        x="Obez"
    elif(bki>30.0 and bki<39.9):
        x="Şişman"
    elif(bki>25.0 and bki<29.9):
        x="Fazla kilolu"
    elif(bki>18.5 and bki<24.9):
        x="Normal"
    elif(bki<18.5):
        x="Zayıf"
    return x


while(True):
    boy=float(input("Lütfen boyunuzu giriniz"))
    kilo=float(input("Lütfen kilonuzu giriniz"))

    z=indeks()
    print(z)
    break



























