#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def oraliq(min, max):
    sonlar = []
    while min<=max:
        sonlar.append(min)
        min += 1
    for son in sonlar:
        
        return sonlar
son = oraliq(1,10)
print(oraliq(1,10))

tubsonlar = []
for n in son:
    tub = True
    if n == 1:
        tub = False
    for i in range(2,n):
        if n%i == 0:
            tub = False
    if tub:
        tubsonlar.append(n)
print(tubsonlar)



