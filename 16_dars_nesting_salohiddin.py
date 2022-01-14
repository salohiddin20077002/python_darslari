# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 10:07:29 2022

@author: User6
"""

alisher_navoiy = {
                  "tugilgan joyi" : "Hirot",
                  'tugilgan yili' : "1441-yil 9-fevral",
                  'Otasining ismi': 'G\'iyosiddin',
                  "asarlari" : "Farhod va Shirin",
                  "asar" : "Layli va Majnun",
                  "roman" : "Hayrat ul-abror"
                  }
                  
                  
                  

imom_al_buxoriy = {
                  "tugilgan joyi" : "Buxoro",
                  "tugilgan yili": "810-yil",
                  "Otasining ismi" : "Ismoil",
                  "asarlari" : "Al-jome as-sahih",
                  "asar" : "At-tarix as sag'ir"
                  }

abdulla_qodiriy = {
                  "tugilgan joyi" : "Toshkent",
                  "tugilgan yili" : "1894-yil",
                  "Otasining ismi" : "Qodirbobo",
                  "asarlari" : "O'tkan kunlar",
                  "asar" : "Mehrobdan chayon"
                  }
erkin_vohidov = {
                "tugilgan joyi" : "Farg\'ona", 
                "tugilgan yili" : "1936",
                "Otasining ismi" : "Cho\'yanbek",
                "asarlari" : "Tong nafasi",
                "asar" : "O'zbegim"
                }

print("Alisher Navoiy", alisher_navoiy['tugilgan yili'] ,  alisher_navoiy["tugilgan joyi"],"da" ,"tavullud topgan." ,"Otasining ismi",alisher_navoiy['Otasining ismi'])
print("Imom al-Buxoriy", imom_al_buxoriy["tugilgan yili"] , imom_al_buxoriy["tugilgan joyi"] , "da", "tavullud topgan." , "Otasining ismi",imom_al_buxoriy["Otasining ismi"] )
print("Abdulla Qodiriy" , abdulla_qodiriy["tugilgan yili"] , abdulla_qodiriy["tugilgan joyi"] , "da" , "tavullud topgan." , "Otasining ismi", abdulla_qodiriy["Otasining ismi"])
print("Erkin Vohidov" , erkin_vohidov["tugilgan yili"] ,erkin_vohidov["tugilgan joyi"], "da" ,"tavullud topgan." , "Otasining ismi", erkin_vohidov["Otasining ismi"])



print("Alisher Navoiyning  asarlari\n",alisher_navoiy["asarlari"],"\n",alisher_navoiy["asar"] , "\n", alisher_navoiy["roman"])
print("Imom al-buxoriyning asarlari \n", imom_al_buxoriy["asarlari"], "\n" , imom_al_buxoriy["asar"])
print("Abdulla Qodiriyning  asarlari\n",abdulla_qodiriy["asarlari"] , "\n" , abdulla_qodiriy["asar"])
print("Erkin Vohidovning asarlarlari\n" , erkin_vohidov["asarlari"], "\n", erkin_vohidov["asar"])











kino = {"k" : "Terminnator",
        "m"  : "Tezlik",
        "s" : "Sevgi"
        }

kinolar = {"l" : "Titanik",
            "j" : "Yurak",
            }

serial = {"q" : "Sevginator",
          "r" : "Armon",
          }




print("Komilning sevimli kinolari\n", kino["k"],"\n",kino["m"],"\n", kino["s"])
print("Akamning yaxshi ko'rgan kinolari\n" , kinolar["l"] , "\n" , kinolar["j"])
print("Do'stimning juda yaxshi ko'rgan filmlari\n", serial["q"], "\n" , serial["r"])









Davlatlar = {"h" : "448978kv.km",
              "a" : "3500000",
              "f" : "Toshkent"
              }

davlat = {"h" : "17098246kv.km",
          "a" : "145678578",
          "f" : "Moskva",
          }
 
dunyo = {"h" : "9631420kv.km",
          "a" : "75375453",
          "p" : "Washinton"
          }

print("O'zbekiston poytaxti", Davlatlar["f"] ,"shahri" ,"\n" ,"hududi" , Davlatlar["h"] ,"\n" , "aholisi", Davlatlar["a"])
print("Rossiya  poytaxti" , davlat["f"] , "\n" , "hududi", davlat["h"] , "\n" , "aholisi" , davlat["a"])
print("Aqshning poytaxti" , dunyo["p"], "\n" , "hududi" , dunyo["h"] , "\n" , "aholisi", dunyo["a"])




davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                    'maydon':448978,
                    'aholi':33_000_000,
                    'pul birligi':"so'm"
                    },
    "rossiya":{'poytaxt':"moskva",
                    'maydon':17_098_246,
                    'aholi':144_000_000,
                    'pul birligi':"rubl"
                    },
    "aqsh":{'poytaxt':"vashington",
                    'maydon':9_631_418,
                    'aholi':327_000_000,
                    'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                    'maydon':329750,
                    'aholi':25_000_000,
                    'pul birligi':"rinngit"}
    }

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")














     