def Sumupto(n):
    return int(((n+1)*n)/2)

a = int(input("Enter the first number->"))
b = int(input("Enter the second number->"))
print(Sumupto(b) - Sumupto (a-1))
