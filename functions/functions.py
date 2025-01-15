# # Foydalanuvchi kiritgan sonning kub ildizini toping.
# # Berilgan sonning faktorialini hisoblang.

# import math

# a = int(input('Son kiriting'))
# kub = math.pow(a,3)
# faktorial = math.factorial(a)

# print(kub)
# print(faktorial)


# datetime modulidan foydalanib:

# Bugungi sanani va vaqtni ekranga chiqaring.
# Foydalanuvchi kiritgan yildan hozirgi yilgacha necha yil o'tganini hisoblang.

# from datetime import datetime

# hozir = datetime.now()
# print(hozir)
# h_yil = hozir.year
# kyil = int(input("Yil kiriting: "))
# farq_yil = h_yil-kyil
# print(farq_yil)


# # Funksiya yarating, u berilgan sonning kvadratini qaytarsin.

# def kvadrad(a,b):
#     kvadrat = a**b
#     print(kvadrat)
#     return kvadrad
# print(kvadrad(2,3))

# # Funksiya yarating, u berilgan sonni juft yoki toq ekanligini aniqlasin.

# def juft_toq(a):
#     if a%2==0:
#         print("Juft son")
#     else:
#         print("Toq son")
#     return juft_toq
# print(juft_toq(12))


# def tortburchak(a,b):
#     s=a*b
#     p=2*(a+b)
#     return s,p
# print(tortburchak(2,3))
#  *****
#  O‘rtachadarajadagi  masalalar
#  *****
# # Funksiya yarating, u to‘rtburchakning eni va bo'yi berilganida yuzasi va perimetrini hisoblab qaytarsin.

# Funksiya yarating, u foydalanuvchi ismi, familiyasi va yoshi berilganida, to‘liq ma’lumotni matn ko‘rinishida qaytarsin

def malumotlar(ism,familiya,yosh,tjoyi=None):
    return f"Ismi {ism} familiyasi {familiya} yoshi: {yosh}, yug'ilgan joyi {tjoyi}"
malumot1 = malumotlar('Dosron',"Ubaydullayev",18,'Buxoro')
malumot2 = malumotlar('Rustam','Ergashev',28,)
info = [malumot1,malumot2]
print(info)
