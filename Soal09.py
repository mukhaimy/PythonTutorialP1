'''
Generate a random number between 1 and 9 (including 1 and 9).
 Ask the user to guess the number, then tell them whether
 they guessed too low, too high, or exactly right. 
 (Hint: remember to use the user input lessons 
  from the very first exercise)
'''
import random

angkaRandom = random.randint(1, 9)
tebakan = int(input('Masukkan tebakan 1 s/d 9 : '))

if (tebakan == angkaRandom):
    print("-- tebakan anda benar --")
elif(tebakan > angkaRandom):
    print("tebankan anda TERLALU TINGGI")
else:
    print("tebankan anda TERLALU rendah")
        
while (tebakan != angkaRandom):
    tebakan = int(input('Masukkan tebakan lagi: '))
    if (tebakan == angkaRandom):
        print("-- tebakan anda benar --")
    elif(tebakan > angkaRandom):
        print("tebankan anda TERLALU TINGGI")
    else:
        print("tebankan anda TERLALU rendah")

print('angka random pada komputer = ', tebakan)

# mau paksa proses behenti, tekan Ctrl+C