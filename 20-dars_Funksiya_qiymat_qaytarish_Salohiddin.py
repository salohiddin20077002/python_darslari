# # -*- coding: utf-8 -*-
# """
# Created on Fri Jan 21 09:57:11 2022

# @author: User6
# """





# def malumot_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumot = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return malumot


# print("O'zingiz haqida ma'lumotlarni kiriting.")
# malumotlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     malumotlar.append(malumot_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break

# print("Mijozlar:")
# for malumot in malumotlar:
#     print(
#         f"{malumot['ism'].title()} {malumot['familiya'].title()},"
#         f"{malumot['yoshi']} yoshda, telefoni: {malumot['telefon']}"
#     )



# def malumot(ism, familiya, shahar, yosh):
#     f_chi = {'ism' : ism,
#           'familiya': familiya,
#           'shahar': shahar,
#           'yosh': yosh}
#     return f_chi

          

# print("Malumot saqlaymiz")
# malumotlar = []

# while True:
#     print("\nQuyidagi malumotlarni kiriting:")
#     ism = input("Ismingizni kiriting:")
#     familiya = input("Famliyangizni kiriting:")
#     shahar = input("Shahringizni kiriting:")
#     yosh = input("Yoshingizni kiriting:")
#     malumotlar.append(malumot(ism,familiya,shahar,yosh))
    
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break


# print("Sizning malumotlaringiz:")
# for f_chi in malumotlar:
#         print(f"Sizning ismingiz {f_chi['ism'].title()} Familiyangiz {f_chi['familiya'].title()} {f_chi['shahar']} viloyatida tug'ilgansiz. Yoshingiz {f_chi['yosh']}")    

 





# def eng_kattasi(a, b, c):
#     max = a
#     if b >= max:
#         max = b
#     if c >= max:
#         max = c
#     return max



# def aylana_info(radius, pi=3.14159):
#     aylana = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2,
#     }
#     return aylana

             





# def tub_son(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar







# def fibonachi(a):
#     sonlar = []
#     for x in range(a):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonachi(15))