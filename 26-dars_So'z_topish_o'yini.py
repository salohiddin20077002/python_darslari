# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:40:22 2022

@author: User6
"""

import uzwords_mod
from soz import sozlar


def get_soz():
    soz = random.choice(sozlar)
    
    while "-" in soz or ' ' in soz:
        soz = random.choice(sozlar)
        return soz.upper()
    
    

def display(f_chi, soz):
    display_chi=""
    for chi in soz:
        if chi in f_chi.upper():
            display_chi +=chi
        else:
            display_chi += "-"
            return display_chi  

def play_soz():
    soz = get_soz()
    soz_chilar = set(soz)
    f_chi_chi = ' '
    print(f"Meн {len(soz)} xoнали су'з  уйладим. Топа оласизми")
    while len(soz_chilar)>0:
        print(display(f_chi_chi,soz))
        if len(f_chi_chi)>0:
            print(f"Шу вактгача киритган харфларингиз:{f_chi_chi}")


        chi = input("Харф киритинг: ").upper()
        if chi in f_chi_chi:
            print("Бу харфни аввал киритгансиз. Бошка харф киритинг.")
            continue
        elif chi in soz:
            soz_chilar.remove(chi)    
            print(f"Харф {chi} харф туг'ри.")
        else:
            print("Бундай харф йук.")
        f_chi_chi+=chi
        print(f"Табриклайман. {soz} сузини {len(f_chi_chi)} та уриниш топдингиз.") 