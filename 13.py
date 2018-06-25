def topla(liste):
    if(len(liste))==0:
        return 0
    else:
        return liste[0]+(topla(liste[1:]))

"""
recursion fonksiyon.
1. return=1+topla([2,3,4])
2. return=2+topla([3,4])
3. return=3+topla([4])
4. return=4+topla([])
5.return=0
1+(2+(3+(4+0)))

"""

print(topla([1,2,3,4]))
