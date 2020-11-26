'''
Create a program that asks the user to enter their 
name and their age. Print out a message addressed to 
them that tells them the year that 
they will turn 100 years old.

GT:
Buat program yang meminta pengguna untuk 
memasukkan nama dan usia mereka. 
Cetak pesan yang ditujukan kepada mereka 
yang memberi tahu mereka tahun di mana mereka 
akan menginjak usia 100 tahun.
'''

tahunSekarang = 2040
nama = input('Masukkan Nama Anda: ')
umur = input('Umur Anda: ')  
# karena fungsi [input] menghasilkan variabel bertipe "string"
# maka perlu dikonversi ke integer
umur = int(umur)

menuju100 = 100 - umur
ultah100 = tahunSekarang + menuju100

print("Hallo, ", nama, \
      " akan berulang tahun ke-100 pada tahun:", \
      ultah100)