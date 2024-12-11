#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini 
# lug'at ko'rinishida qaytaruvchi funksiya yozing
import math
R = float(input("Radiusni kiriting: "))
def ayalana_malumot(R):
    perimetr = 2*math.pi*R
    yuzasi = math.pi*(R**2)
    diametr = 2*R  
    
    return perimetr, yuzasi, diametr
aylana = {"radius":None,
        "perimetr":None,
          'yuzasi':None,
          "diametr":None,
          }    

perimetr, yuzasi, diametr = ayalana_malumot(R)

aylana["perimetr"] = perimetr
aylana['yuzasi'] = yuzasi
aylana['diametr'] = diametr
aylana['radius'] = R


print("Malumotlar\n")
print(aylana)