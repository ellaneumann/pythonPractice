
x = 1
while x <= 100:
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Buzz")
    elif x%5 == 0:
        print("Fizz")     
    x+=1    