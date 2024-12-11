#Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

def malumotlar(ism, familiya, yosh, tjoyi, email=None, telefon=None):
    
    malumot = {
        "ism": ism,
        "familiya": familiya,
        "yosh": yosh,
        "tjoyi": tjoyi,
        "email": email,
        "telefon": telefon,
    }
    return malumot
print("Kompaniyamiz mijozlari: ")
mijozlar = []
while True:
    print("\nQuyidagi malumotlarni kiriting: ",end = '')
    ism = input("\nIsmingizni kiriting: ")
    familiya = input("Familiyanigizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    tjoyi = input("Qayerda tug'ilgansiz?: ")
    email = input("Elektron manzilingizni kiriting: ")
    telefon = int(input("Telefon raqamingizni  kiriting:+998"))
    
    mijozlar.append(malumotlar(ism, familiya, yosh, tjoyi, email, telefon))
    
    javob = input("Yana malumot kiritasizmi?(Y/n)")
    if javob == 'n':
        break
for malumot in mijozlar:
    email = malumot["email"] if malumot["email"] else "Nomalum"
    telefon = malumot["telefon"] if malumot["telefon"] else "Nomalum"
    print(f"{malumot['ism']} {malumot['familiya']} - Yosh: {malumot['yosh']} , Email: {email}, Telefon: {telefon}")

    


