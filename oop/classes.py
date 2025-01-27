# # Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
# # Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting 
# # (ism, foydalanuvchi ismi, email, va hokazo)

#*****
# def see_methods(klass):
#     """Dunder metodlarisiz obyektlarimiz ko'rinadi"""
# return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))
#*****
# class User:
#     def __init__(self,ism,familiya,yosh,foydalanuvchi_ismi=None,email=None):

#         self.ism = ism
#         self.familiya = familiya
#         self.foydalanuvchi_ismi = foydalanuvchi_ismi
#         self.email = email
#         self.yosh = yosh
#     def get_name(self):
#         return self.ism
        
#     def age(self):
#         return self.yosh
#     def get_info(self):
#         print(f"Foydalunuchi:{self.foydalanuvchi_ismi}, ismi:{self.ism} {self.familiya}, yoshi: {self.yosh}")

# user1 = User('Doston','Ubaydullayev',18,'doksbro','ubaydullayevdoston607@gmail.com')
# user2 = User('Diyor','Toyirov',20,'toyirov1@gmail.com')

# print(user2.get_info())



# ********
# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta
# xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. 
# Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

# class Avto:
#     def __init__(self,model,rang,karobka,narh):
#         self.model = model
#         self.color = rang
#         self.distance = 10000
#         self.karobka = karobka
#         self.narh = narh
#     def update_dist(self):
#         self.distance +=500
#         return self.distance
#     def get_model(self):
#         return self.model
#     def get_info(self):
#         return f"Mashina modeli:{self.model.upper()}, rangi: {self.color}, karobkasi: {self.karobka}, Bosib o'tgan masofasi: {self.distance} va narhi: {self.narh}"

# avto1 = Avto('mercedes','oq','avtomat',60000)
# avto2 = Avto('tesla','qora','avtomat',30000)

# print(avto1.update_dist())
        
        
# # ***********
#   *   Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)  

#   *  Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

#   *  Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

#   *  Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

#   *  dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avtolar):
        self.name = salon_nomi
        self.manzili =manzili
        self.sotuvdagi_avtolar = sotuvdagi_avtolar
        self.elektr = 5
        self.benzin = 13
        self.yangi_mashina = []
    def update_elek(self):
        self.elektr += 1
        return self.elektr
    def set_yang_mashina(self,yang_mashina):
        while True:
            a = input("Mashinalar modelini qo'shing")
            self.yangi_mashina.append(a)
        return self.yangi_mashina
avto



        