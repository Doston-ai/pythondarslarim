# #Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def kopaytma(*sonlar):
#     yigindi = 1
#     for son in sonlar:
#         yigindi = son*yigindi
#     return yigindi
# print(kopaytma(5,6,10))


#Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
#Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def malumotlar(ism,familiya,**additional):
    additional['ism'] = ism
    additional['familiya'] = familiya
    return additional
talaba1 = malumotlar('Doston','Ubaydullayev',kursi=1,yoshi=18)
talaba2 = malumotlar("Javohir","Ubaydullayev",kursi=3)


for kalit,qiymat in talaba1.items():
    print(f"{kalit.title()}: {qiymat}")
print("\n******")
for kalit,qiymat in talaba2.items():
    print(f"{kalit.title()}: {qiymat}")
