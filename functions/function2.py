#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

a = input("son kiriting: ")
b = input("son kiriting: ")
c = input("son kiriting: ")

def kattason_qaytaruvchi(a,b,c):
    if b<a>c:
        print(a)
    elif a<b>c:
        print(b)
    elif a<c>b:
        print(c)
    
kattason_qaytaruvchi(a,b,c)