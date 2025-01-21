# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting 
# (ism, foydalanuvchi ismi, email, va hokazo)


class User:
    def __init__(self,ism,familiya,yosh,foydalanuvchi_ismi=None,email=None):

        self.ism = ism
        self.familiya = familiya
        self.foydalanuvchi_ismi = foydalanuvchi_ismi
        self.email = email
        self.yosh = yosh
    def get_name(self):
        return self.ism
        
    def age(self):
        return self.yosh
    def get_info(self):
        print(f"Foydalunuchi:{self.foydalanuvchi_ismi}, ismi:{self.ism} {self.familiya}, yoshi: {self.yosh}")

user1 = User('Doston','Ubaydullayev',18,'doksbro','ubaydullayevdoston607@gmail.com')
user2 = User('Diyor','Toyirov',20,'toyirov1@gmail.com')

print(user2.get_info())




