a=10

def fonksiyon():
    a=2
    print(a)

fonksiyon()
print(a)

#fonksiyonun içindeki değer dışarıyı etkilemez

a=10

def fonksiyon():
    global a
    a=2
    print(a)

fonksiyon()
print(a)

#global olarak tanımlandığı için dışarıyı da etkiler
