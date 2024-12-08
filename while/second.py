#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
#Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
#Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

yosh = 'Yoshingizni kiriting'
yosh += '(chiqish uchun stop deb kiriting)\n>>>'
qiymat = True
while qiymat:    
    kirit_yosh = input(yosh)
    if kirit_yosh == "exit" or kirit_yosh == 'stop':
        qiymat = False
    else:
        if int(kirit_yosh) <= 7:
            print("Sizga kirish 2000 so'm")
        elif int(kirit_yosh) >= 8 and int(kirit_yosh) < 18:
            print("Sizga kirish 3000 so'm")
        elif int(kirit_yosh) >=18 and int(kirit_yosh) <= 65:
            print("Sizga kirish 10000 so'm")    

        else:
            print("Sizga kirish bepul")
print("Dastur tugadi!")