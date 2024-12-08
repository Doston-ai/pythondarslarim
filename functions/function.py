#Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)


from datetime import datetime

def malumotlar(ism, familiya, tyil, tjoyi, email=None, telefon=None):
    # Hozirgi yilni aniqlash uchun
    hozirgi_yil = datetime.now().year
    yosh = hozirgi_yil - tyil

    # Lug'atni shakllantirish
    malumot = {
        "ism": ism,
        "familiya": familiya,
        "yosh": yosh,
        "tyil": tyil,
        "tjoyi": tjoyi,
        "email": email,
        "telefon": telefon,
    }
    return malumot

# Misol uchun shaxslar malumotlari
shaxs1 = malumotlar('Doston', 'Ubaydullayev', 2006, 'Buxoro', 'ubaydullayevdoston607@gmail.com', 903334275)
shaxs2 = malumotlar('Javohir', 'Ubaydullayev', 2005, 'Buxoro')

# Ma'lumotlarni ro'yxatga olish
info = [shaxs1, shaxs2]

print('Shaxslar ma\'lumotlari:')
for malumot in info:
    email = malumot["email"] if malumot["email"] else "Nomalum"
    telefon = malumot["telefon"] if malumot["telefon"] else "Nomalum"
    print(f"{malumot['ism']} {malumot['familiya']} - Yosh: {malumot['yosh']} yil, Email: {email}, Telefon: {telefon}")
