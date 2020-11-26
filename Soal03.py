'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements 
of the list that are less than 5.
'''

# indeks di Python mulai 0
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = len(a)

# dibuat variabel 'i' yang akan bernilai dari 0 hingga 'n - 1'
# range(n)
batas = 5
for i in range(n):
    
    if (a[i] < batas):
        print(a[i], ' < ', batas)  
    
    
# -----
# if (a[0] < 5):
#     print(a[0])

# if (a[1] < 5):
#     print(a[1])

# if (a[2] < 5):
#     print(a[2])
    
# # ...
# if (a[n-1] < 5):
#     print(a[n-1])
    
