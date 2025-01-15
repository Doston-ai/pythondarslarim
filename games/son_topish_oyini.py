import random as r
a = r.sample(range(10),1)

print("O'ylagan sonni topish o'ynaymiz!!!")
while True:
    b = int(input("1 dan 10 gacha son o'yladim topaolasizmi?\n>>>"))
    print(b)
    
    if b==a[0]:
        print("O'ylagan sonimni topdingiz")
    elif True:
        
        if a[0]>b:
            print("men o'ylagan son bundan kattaroq(+)")
        else:
            print("men o'ylagan son bundan kichikroq(-)")


# sonlar = list(range(1,11))

      