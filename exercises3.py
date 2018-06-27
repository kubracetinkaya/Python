def sayı(liste):
    if len(liste)==4:
        a=liste[0]
        b=liste[1]
        c=liste[2]
        d=liste[3]

        if(d==0 or d==2 or d==4 or d==6 or d==8):
            print("Sayı çift")
        else:
            print("Sayı tek")
        
    elif len(liste)==3:
        a=liste[0]
        b=liste[1]
        c=liste[2]

        if(c==0 or c==2 or c==4 or c==6 or c==8):
            print("Sayı çift")
        else:
            print("Sayı tek")
       

    elif len(liste)==2:
        a=liste[0]
        b=liste[1]

        if(b==0 or b==2 or b==4 or b==6 or b==8):
            print("Sayı çift")
        else:
            print("Sayı tek")
       
    elif len(liste)==1:
        a=liste[0]

        if(a==2 or a==4 or a==6 or a==8):
            print("Sayı çift")
        elif(a==1 or a==3 or a==5 or a==7 or a==9):
            print("Sayı tek")
        else:
            print("Sayı sıfır")

    else:
        print("Max 4 basamaklı sayıları kontrol edebilirsiniz")




while(True):

    basamak_sayisi=int(input("Sayınız kaç basamaklı?"))
    if(basamak_sayisi==4):
        a=int(input("Binler basamağını giriniz:"))
        b=int(input("Yüzler basamağını giriniz:"))
        c=int(input("Onlar basamağını giriniz:"))
        d=int(input("Birler basamağını giriniz:"))
        sayı((a,b,c,d))

    elif(basamak_sayisi==3):
        a=int(input("Yüzler basamağını giriniz:"))
        b=int(input("Onlar basamağını giriniz:"))
        c=int(input("Birler basamağını giriniz:"))
        sayı((a,b,c))

    elif(basamak_sayisi==2):
        a=int(input("Onlar basamağını giriniz:"))
        b=int(input("Birler basamağını giriniz:"))
        sayı((a,b))

    elif(basamak_sayisi==1):
        a=int(input("Birler basamağını giriniz"))
        sayı()

    else:
        print("Max 4 basamaklı sayıları kontrol edebilirsiniz")
        
        

    
                    




























        
       

    
