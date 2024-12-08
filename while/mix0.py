#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

mahsulot = []
n = 1
while True:
  
    savol = f"{n}-mahsulotni kiriting\n>>>"
    narsalar = input(savol)
    mahsulot.append(narsalar)
    javob = input("Yana kiritasizmi?(ha/yo'q)\n>>>")
    if javob == "ha":
        n+=1
        continue
    else:
        break
print("Tanlagan mahsulotlaringiz:")
for narsalar in mahsulot:
    print(narsalar.title())