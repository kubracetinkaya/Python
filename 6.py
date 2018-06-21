kayitlikullanıcı="Scatola Nera"
kayitliparola="1234"

while(True):
    kullanıcı=input("Kullanıcı adınızı giriniz")
    parola=input("Parolanızı giriniz")
    if((kayitlikullanıcı==kullanıcı) and (kayitliparola==parola)):
        print("Hoşgeldiniz",kullanıcı)
        break
    elif((kayitlikullanıcı!=kullanıcı) and (kayitliparola==parola)):
        print("Kullanıcı adınız yanlış")
    elif((kayitlikullanıcı==kullanıcı) and (kayitliparola!=parola)):
        print("Parolanızı mı unutuunuz?")
        print("Parolanızı değiştirmek ister misiniz?E/H")
        cevap=input()
        if(cevap=="E"):
            print("Yeni parolanızı giriniz")
            yeni=input()
            print("Şifre başarıyla değiştirildi")
            print("Yeni parolanız:",yeni)
        kayitliparola=yeni
        if(cevap=="H"):
            print("Parolanızı tekrar giriniz")
    else:
        print("Tekrar deneyiniz")
        
            
        
