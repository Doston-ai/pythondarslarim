#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

mahsulotlar = {}
nom = "mahsulot nomini kiritng\n>>>"
narh = "narh"
something = True
while something:
    mahsulot = input(nom)
    m_narhi = input(narh)
    mahsulotlar[mahsulot] = float(m_narhi)

    javob = input("Yana mahsulot kiritasizmi?(ha/yo'q):")
    if javob == "ha":
        something = True
    if javob == "yo'q":
        something= False

for nom,narh in mahsulotlar.items():
    print(f"mahsulot nomi {nom.title()}, narhi {narh}")
