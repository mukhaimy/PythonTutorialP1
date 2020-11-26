'''
Ask the user for a number. Depending on whether the number 
is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently 
 when divided by 2?

GT:
Minta nomor pengguna. Bergantung pada apakah 
jumlahnya genap atau ganjil, cetak pesan yang 
sesuai untuk pengguna. 
Petunjuk: bagaimana bilangan genap / ganjil 
bereaksi berbeda ketika dibagi 2?
'''

# x = input("Masukkan Suatu bilangan: ")
# x = int(x)
x = int(input("Masukkan Suatu bilangan: "))

# operasi modulo : sisa hasil bagi
if (x % 2 == 1):   
    print(x, ' adalah bilangan ganjil')
else:
    print(x, ' adalah bilangan genap')

print(' --- dengan operator &')
# bisa menggunakan prinsip bilangan biner untuk integer
if (x & 1 == 1):   
    print(x, ' adalah bilangan ganjil')
else:
    print(x, ' adalah bilangan genap')