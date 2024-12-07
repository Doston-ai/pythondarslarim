 #Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating


kitob = "Yaxshi ko'rgan kitobingizni kiriting"
kitob += "(Dasturni to'xtatish uchun 'stop' deb yozing): "
qiymat = ''

while qiymat != "stop":
    qiymat = input(kitob)
    if qiymat != "stop":
        print(qiymat)
print("Dastur tugadi")        