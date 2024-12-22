#    Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.
#   Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
#   Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

n = int(input("Son kiriting\n>>>"))
ketmaketlik = [1,1]

def fibanachi(n):
    while n>ketmaketlik[-1]:
        ketmaketlik.append(ketmaketlik[-1]+ketmaketlik[-2])    
        return fibanachi(n)

fibanachi(n)
print(ketmaketlik)
