'''
Write a program that asks the user how many Fibonnaci numbers 
to generate and then generates them. Take 
this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of 
numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers 
 where the next number in the sequence is the sum 
 of the previous two numbers in the sequence. 
 The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


Bilangan Fibonnaci :
    - Berapa banyak (n)
    - dua bilangan awal, a0, a1

'''
def Fib(n, a0, a1):
    hsl = [a0, a1]
    
    for i in range(2, n):
        a2 = a0 + a1
        hsl.append(a2)  # diulang sampai diperoleh n bilangan
        a0, a1 = a1, a2
        
    return hsl
# ------------------------

n = 7
a0 = 2
a1 = 4
print(Fib(n, a0, a1))











    
    