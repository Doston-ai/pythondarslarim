# #Create a countdown program that starts at 10 and counts down to 1.
#
# #When it reaches 1, print "Liftoff!".
# def function():
#
#     n = 10
#
#     while n>0:
#         if n==1:
#             print('Liftoff!')
#         else:
#             print(n)
#         n-=1
# function()



# Project: Student Management System (Talabalar Boshqaruv Tizimi)
# Talablar:
#
#     1.Talabalar ro‘yxati – har bir talabaning ismi va bahosi (lug‘atda saqlanadi).
#     2.Asosiy menyu – foydalanuvchi quyidagi amallarni bajara olishi kerak:
#         Talaba qo‘shish
#         Talaba bahosini o‘zgartirish
#         Talabalar ro‘yxatini ko‘rish
#         O‘rtacha bahoni hisoblash
#         Dasturdan chiqish
#     3.Barcha amallar while tsikli orqali takrorlanib turishi kerak.

talabalar = ['olim','ali','vali','hasan']
talaba = {}

while True:
    ism = talabalar.pop()
    baho = input(f'{ism.title()}ning bahosini kiriting\n>>>')
    talaba[ism]=baho
    a = input('Yana talabani baholaysizmi(ha/yo\'q): ')
    if a == 'ha':
        continue
    else:
        #False
        break
for ism,baho in talaba.items():
    print(f"{ism.title()}ning bahosi: {baho}")
print('\n')
baho = list(talaba.values())
print('Baholar: ',baho)
summa = 0
for son in baho:
    summa += int(son)
print('O\'rtacha baho: ',summa/len(baho))
 