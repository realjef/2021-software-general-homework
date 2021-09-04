def factorial(num):
    if num <= 0:
        return None
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact
print("The factorial of the number that you entered is: ")
print(factorial(-100))
