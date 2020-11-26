'''
Ask the user for a string and print out whether 
this string is a palindrome or not. 
(A palindrome is a string that reads the 
 same forwards and backwards.)

racecar --> Polindrom
'''

w = input("Masukkan kata uji: ")
nw = len(w)
#  apabila huruf besar atau kecil sama saja 
#  w = w.upper()
polindome = True
for i in range(nw):
    if (w[i] != w[nw - 1 - i]):
        polindome = False
        break

print (w, ' -->> Termasuk Polindrome? ', polindome)

        
