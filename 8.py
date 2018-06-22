kayıtlıkullanıcı="kubra"
kayıtlıparola="1234"

while (True):
    kullanıcı=input("Kullanıcı adını giriniz")
    parola=input("Parolanızı giriniz")

    if((kayıtlıkullanıcı!=kullanıcı) or (kayıtlıparola!=parola)):
        print("Yanlış giriş")
    else:
        print("Hoşgeldiniz")
        break

listeler=[2,3,4]

for i in range(1,10):
    if(i in listeler):
        continue
    print(i)
                
i=0

while(i<10):

    if(i==2):
        continue
    i+=1
    print(i)
    
