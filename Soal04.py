'''
Create a program that asks the user for a number and 
then prints out 
a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number 
 that divides evenly into another number. 
 For example, 13 is a divisor of 26 because 26 / 13 has 
 no remainder.


Misal angka 9
9 / 1 = 9 * 1 + 0  --> 1 ADALAH PEMBAGI 9
9 / 2 = 4 * 2 + 1  --> 2 bukan pembagai 9
9 / 3 = 3 * 3 + 0  --> 3 ADALAH PEMBAGI 9   
9 / 4 = 2 * 4 + 1  --> 4 bukan pembagai 9

MENGGUNAKAN MODULO-NYA
''' 
x = int(input('Masukkan bilangan: '))

# kode sebelum optimasi
# --------------------------
# for i in range(1, x + 1):
#     if (x % i == 0):
#         print(i, ' adalah pembagi ', x)


# optimasi ke-1
# --------------------------

# suatu bilangan sudah pasti bisa di bagi 1 dan bilanan tersebut
# kita akan singkirkan 1 dan bilangan tersebut
# -----
# suatu bilangan genap pasti bisa dibagi 2
# -----
# suatu bilangan tidak akan bisa dibagi dengan 
# bilangan > (1/2) dari bilangan tersebut
# 9 / 2 = 4.5
# 9 tidak akan bisa dibagi dengan 5, 6, 7, dan 8

# kalau jelas bilangan tersebut bilangan ganjil
# pasti tidak akan bisa dibagi 2, 4, 6, 8, 10


if (x & 1 == 1):
    for i in range(3, (x + 2) // 2, 2):
        #print(i, end=' -->> ')
        if (x % i == 0):
            print(i, ' adalah pembagi ', x)
        #else:
        #    print()

else:
    for i in range(2, x // 2):
        #print(i, end=' -->> ')
        if (x % i == 0):
            print(i, ' adalah pembagi ', x)
        #else:
        #    print()