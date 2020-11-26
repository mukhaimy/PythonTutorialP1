'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains 
only the elements that are common 
between the lists (without duplicates). 
Make sure your program works on two lists 
of different sizes.
'''

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c_a = list(set(a))
c_b = list(set(b))

hasil = []
# cek dari c_a ke c_b
for x in c_a:
    if (x in c_b):
        hasil.append(x)

# cek dari c_b ke c_a
# for x in c_b:
#     if ((x in c_a) and (not (x in hasil))):
#         hasil.append(x)

print("nilai yang sama : ", hasil)
        