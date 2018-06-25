def topla(liste):
    if len(liste)==4:
        a=liste[0]
        b=liste[1]
        c=liste[2]
        d=liste[3]
        

        toplam=0

        for i in liste:
            
            toplam+=i

        return toplam

    else:
        print("4 eleman giriniz")

        

  
while(True):
    eleman=int(input("Listenin eleman sayısını giriniz\n"))
    if(eleman==4):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        topla((a,b,c,d))

    else:
        print("Lütfen 4 eleman giriniz")


        

    
    
    
