import math

# fizzbuzz function
def fizzbuzz():
    x = 1
    while x <= 100:
        if x%3 == 0 and x%5 == 0:
            print("FizzBuzz")
        elif x%3 == 0:
            print("Buzz")
        elif x%5 == 0:
            print("Fizz")     
        x+=1   

# primes function
n = input("n = ")
def primes():
    p_list = []
    for x in range (1,n+1):
        if x > 1:
            for i in range(2, x):
                if (x%i) == 0:
                    break
            else:
                p_list.append(x)    

print(p_list)

# prime_factorization
n = input("n = ")

def prime_factorization(n):
    while n %2 == 0:
        print(2),
        n = n/2

    for i in range(3,int(math.sqrt(n))+1,2):
        while (n%i) == 0:
            print(i),
            n = n/i 

    if n>2:
        print(n)

# my_sort is insertion sort implementation (runtime O(n^2))
num_list = input("input list (ex: [5, 3, 12, 4]): ")

def my_sort(list):
    for i in range(1, len(num_list)):
        copy = num_list[i]
        j = i-1
        while j >= 0 and copy < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = copy      

