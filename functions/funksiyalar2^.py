# #Funksiyaga ro'yxat uzating va undagi barcha elementlarni 2 ga ko'paytirib yangi ro'yxat qaytaring.
# son1 = [1,2,3,4]
# def yangi_list(sonlar):
#     yangi_sonlar = [son * 2 for son in sonlar]
#     return yangi_sonlar
    
# print(yangi_list(son1))
# print(son1)


#Ro'yxatni funksiyaga uzatib, undagi toq sonlarni qaytaruvchi funksiya yozing.


# def toqsonlar():
#     sonlar = [1,2,3,4,5,15,18]
#     sonlar1 = []
#     for son in sonlar:
#         if son%2!=0:
#             sonlar1.append(son)
#         # else:
#         #     break
#     return sonlar1
# print(toqsonlar())






# def info(ism,familiya,tyil,tjoy,email,tel_raqam=None):
#   bio_info = {'ism':ism,
#               'familiya':familiya,
#               "tugilgan yili":tyil,
#               'tugilgan joyi':tjoy,
#               'elektron manzili':email,
#               'telefon raqami':tel_raqam}
#   return bio_info
# shaxs1 = info('doston','ubaydullayev',2006,'Buxoro',"ubaydullayevdoston607@gmail.com")
# shaxs2 = info('javohir','ubaydullayev',2005,'Buxoro','ubaydulloyevjavohir7@gmail.com',+903334275)
# shaxslar = [shaxs1,shaxs2]
# for bio_info in shaxslar:
#   if bio_info['telefon raqami']:
#     tel_raqam = bio_info['telefon raqami']
#   else:
#     tel_raqam = 'Nomalum'
#   print(f"{bio_info['ism'].title()} {bio_info['familiya'].title()} {bio_info['tugilgan yili']} {bio_info['tugilgan joyi']} tug'ilgan, elektron manzili:{bio_info['elektron manzili']} va telefon raqami:{bio_info['telefon raqami']}")







# def info(ism,familiya,tyil,tjoy,email,tel_raqam=None):
#   bio_info = {'ism':ism,
#               'familiya':familiya,
#               "yosh":2025-tyil,
#               'tugilgan joyi':tjoy,
#               'elektron manzili':email,
#               'telefon raqami':tel_raqam}
#   return bio_info
# malumotlar = []
# a = True
# while a:
#   print('\nQuyidagi malumotlarni kiriting',end=': ')
#   ism = input('Ismingizni kiriting: ')
#   familiya = input('Familiyangizni kiriting: ')
#   tyil = int(input('Qaysi yilda tug\'ilgansiz'))
#   tjoy = input('Tug\'lgan joyingizni kiriting: ')
#   email = input('Emailingizni kirititing: ')
#   tel_raqam = input('Telefon raqamingizni kiriting: ')

#   malumotlar.append(info(ism,familiya,tyil,tjoy,email,tel_raqam))

#   javob = input("Yana shaxs kirtasizmi?(yes/no)")
#   if javob == 'no':
#     a = False
#     break
 
     
# print("Mijozlar:")
# for bio_info in malumotlar:
#     print(f"{bio_info['ism'].title()} {bio_info['familiya'].title()},"
#           f"{bio_info['yosh']} yoshda, telefoni: {bio_info['telefon raqami']}")









# a = float(input('Birorta son kiriting'))
# b = float(input('Birorta son kiriting'))
# c = float(input('Birorta son kiriting'))
# if a>b>c:
#     print(a)
# elif b>a>c:
#     print(b)
# else:
#     print(c)





# import math

# def aylana(radius,diametr,yuza,peremetr):
#     info = {'radius':radius,
#             'diametr':diametr,
#             'yuzi':yuza,
#             'perimetr':peremetr
#             }
#     return info
  
  
# malumotlar = []  
  
# if True:  
  
#   radius = float(input('Radius; '))
#   yuza = (radius**2)*math.pi
#   diametr = 2*radius
#   peremetr = 2*math.pi*radius

#   malumotlar.append(aylana(radius,diametr,yuza,peremetr))

#   False
# print(malumotlar)
# for ayl in malumotlar:
#    print(f"Radius: {ayl['radius']}, Diametr: {ayl['diametr']},",
#          f" Perimetri: {ayl['perimetr']}, Yaza: {ayl['yuzi']}")
    




# n = int(input('Oraliqdagi eng kichgina sonni kiriting: '))
# i = int(input('Oraliqdagi eng kkata sonni kiriting: '))
# a =  list(range(n,i))
# for c in a:
#     if c%c!=0 and c%1!=0:
#         print('Tub son')
#     else:
#         print('tubdon emas')




# def fibanachi(n):
#     sonlar = []
#     for x in range(n):
#         if x==1 or x==0:
#             sonlar.append(x)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# print(fibanachi(10))



# def tubson_qaytar(min,max):
#     tub_sonlar = []
#     for n in range(min,max):
#         tub = True
#         if n==1:
#             tub=False
#         elif n==2:
#             tub=True
#         else:
#             for x in range(2,n):
#                 if n%x==0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# a = tubson_qaytar(15,25)
# print(a)











# AMALIYOT
# - Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning 
# birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 

# def katta_harf(obj):
#     while obj:
#         malumot = obj.pop()
#         a = print(f"{malumot.title()}")
#     return a
# info = ['ali','vali','hasan','husan']
# b = katta_harf(info[:])
# print(b)
# print(info)



# def bosh_harf(matnlar):
#     malumotlar = []
#     while matnlar:
#         matn = matnlar.pop()
#         malumotlar.append(matn.title())
#         a = malumotlar
#     return a
# ls = ['ali','vali','hasan','husan']
# b = bosh_harf(ls[:])
# print(b)
# print(ls)

# print('\n')
# mohirdev

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)






# Mohirdev

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)



# # mine
# - Darsimiz davomida yozgan `bahola` funksiyasini `.pop()` metodidan foydalanmasdan
#  va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"{ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholangan = bahola(talabalar)
# print(baholangan)
# print(talabalar)

# *args and **kwargs

# AMALIYOT
# 1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# 2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

# def kupaytir(*sonlar):
#     kupaytma = 1
#     for son in sonlar:
#         kupaytma *= son
#     return kupaytma
# a = kupaytir(1,2,6,7)
# print(a)



# def info(ism,familiya,**malumotlar):
#     malumotlar['ism']=ism
#     malumotlar['familiya']=familiya


#     return malumotlar
# user1 = info("doston","ubaydullayev", yoshi = '18', yunalishi = 'suniy intellekt')
# print(user1)








# ********************************** MODULLAR ****************************************

# import info_mod
# avto1 = info_mod.avto_info('Toyota','Toyota supra','metal','avtomat',2023,30000)
# info_mod.info_print(avto1)


# import math
# a = math.pow(2,2)
# print(int(a))




# ************************lambda, map() va filter()**************************************

# x = lambda x,y:x**y
# print(x(5,4))


# def daraja(n):
#     return lambda x:x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f'4 ning kvadrati {kvadrat(4)}, kubi esa {kub(4)}')



# from math import sqrt
# sonlar = list(range(15))
# a = list(map(sqrt,sonlar))
# print(a)






# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

# mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
# print(mevalar_b)

# a = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
# print(a)