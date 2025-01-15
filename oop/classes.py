# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting 
# (ism, foydalanuvchi ismi, email, va hokazo)


class User:
    def __init__(self,ism,familiya,foydalanuvchi_ismi,email,):

        self.ism = ism
        self.familiya = familiya
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
    user1 = User(Doston)