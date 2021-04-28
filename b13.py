def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
num = int(input("enter a number to get it's factorial\n>>"))
print(factorial(num))
    
