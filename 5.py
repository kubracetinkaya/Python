#Kullanıcı adı ve parola kontrol programı

kayitlikullanıcı="Scatola Nera"
kayitliparola="1234"

kullanıcı=input("Kullanıcı adınızı giriniz")
parola=input("Parolanızı giriniz")

if ((kayitlikullanıcı==kullanıcı) and (kayitliparola==parola)):
    print("Sisteme hoşgeldiniz")

elif((kayitlikullanıcı!=kullanıcı) and (kayitliparola==parola)):
    print("Kullanıcı adınızı yanlış girdniz")

elif((kayitlikullanıcı==kullanıcı) and (kayitliparola!=parola)):
    print("Şifrenizi mi unuttunuz?")

else:
    print("Tekrar deneyiniz")
    
