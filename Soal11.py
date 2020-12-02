'''
Ask the user for a number and determine 
whether the number is prime or not.

https://stackoverflow.com/questions/453793/which-is-the-fastest-algorithm-to-find-prime-numbers

Tutorial Fungsi:
    https://www.youtube.com/watch?v=WjM68icSw3s


Contoh Bilangan Prima:
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, ...
    
Bilangan Prima x:
    - harus integer
    - x > 1
    - x tidak termasuk bilangan genap
    - untuk pengujian bilangan dibagi dengan nilai mulai dari 3 
      hingga setangah bilangan tersebut

'''
def ApakahPrima(x):
    if (x <= 1):
        return False
    if (n <= 3) : 
        return True
    if (x & 1 == 0): # apakah bilangan genap?
        return False

    
    for i in list(range(2, (x + 3) // 2)):
        if (x % i == 0):
            return False
    return True
# ----------------------   
 
def isPrime(n) : 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True
# This code is contributed 
# by Nikita Tiwari. 
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
#--------------------------------
    
    
x = int(input('Masukkan bilangan: '))
p = ApakahPrima(x)
print(x, ' Apakah Prima?', p)

# for x in range(1, 80):
#     p = ApakahPrima(x)
#     if (p == True):
#         print(x, ' Prima')


