#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def oraliq(min, max):
    sonlar  = []
    while min<max:
        min += 1
        sonlar.append(min)
    return sonlar
min = float(input("Birinchi sonni kiriting: "))
max = float(input("Oxirgi sonni kiriting: "))

