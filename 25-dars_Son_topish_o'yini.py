# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:50:32 2022

@author: User6
"""

import random

def son_topish(x=10):
    tasodif_son = random.randint(1,x)
    print(f"Men  1 dan {x} gacha son o'ylayman. Topa olasizmi?")
    
    
    while True:
        taxmin_son = int(input(">>>"))
        if taxmin_son<tasodif_son:
            print("XATO. MEN O'YLAGAN SON BUNDAN KATTTAROQ . Yana harakat qiling.")
        elif taxmin_son>tasodif_son:
            print("XATO. MEN O'YLAGAN SON BUNDAN KICHIKROQ . Yana harakat qiling.")
        else:
            break
    print("TABRIKLAYMAN . SIZ MEN O'YLAGAN SONNI TOPDINGIZ.")

son_topish()                



import random

def son_topaman(x=10):
    print(f"Siz 1 dan {x}  gacha son o'ylang . Men topishga harakat qilaman.")
    past = 1
    tepa = x
    taxminlarimiz = 0
 
    while True: 
        taxminlarimiz+=1
        if past != tepa:
            taxmin = random.randint(past,tepa)
        else:
            taxmin = past
        javobingiz = input(f"Endi Siz {taxmin} sonini o'yladingiz  To'g'ri bo'lsa (T) , kichik bo'lsa(-) , katta bo'lsa(+)".lower())
        if javobingiz == "-":
            tepa = taxmin - 1
        elif javobingiz == "+":
            past = taxmin + 1
        else:
            break
    print(f"Men {taxminlarimiz} ta taxmin bilan topdim") 
    return taxminlarimiz
  
     
son_topaman()     


def play(x=10):
    takror = True
    while  takror:
        taxminlar_f_chi = son_topish(x)
        taxminlar_top = son_topaman(x)
        if taxminlar_f_chi<taxminlar_top:
            print("Men {taxminlar_f_chi} ta taxmin bilan topdim va Yutdim")
        elif  taxminlar_f_chi>taxminlar_top:
            print("Siz [taxminlar_top} ta taxmin bilan topdingiz va Yutdingiz")
        else:
            print("Durrang")
        takror = int(input("Yana o'ynaymizmi Ha(1)/Yo'q yetadi(0)"))
        print(takror)        
play()   


















































   

            



            
       
    
    


  