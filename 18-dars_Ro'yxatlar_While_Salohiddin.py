# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 12:12:57 2022

@author: User6
"""

buyurtmalar = []
print("Buyutmalaringizni qabul qilamiz")
n=1
while True:
    f_chi = f"{n}-buyurtmanigizni kiriting>>>"
    buyurtma = input(f_chi)
    buyurtmalar.append(buyurtma)
    yana = input("Yana buyurtma berasizmi? (ha/yo'q)")
    if  yana  =='ha' :
        n+=1
        continue
    else:
        break
    
print("Buyurtmalaringiz ro'yxati")
for buyurtma in buyurtmalar:
    print(buyurtma.title())    





print("e-bozorimizga xush kelibsiz")
mahsulotlar = {}
while True:
    mahsulot = input("Mahsulotning nomini kiritng>>>")
    narx = int(input("Mahsulotning narxini kiritng>>>"))
    mahsulotlar[mahsulot] = int(narx)
    print(mahsulotlar)
    
    market = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if market =="yo'q":
        break
         
for mahsulot , narx  in mahsulotlar.items():
      print(f"{mahsulot.title()} ning narxi {narx} so'm")
     
     
     
     



buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'Olma':20000,
               'Shaftoli':25000,
               'Qovun':18000,
               'Uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
        
        
        

        
        
       







































































