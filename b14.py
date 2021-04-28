num1= int(input("enter the first number\n>>"))
num2= int (input("enter the second number\n>>"))
oddSum =0
evenSum=0
evenCount=0
oddCount=0
for i in range(num1, num2+1):
    if i % 2 == 1:
        oddSum+=i
        oddCount+=1
    else:
        evenSum+=i
        evenCount+=1
print("Sum of odds:",oddSum, "Average of odds sum:",oddSum/oddCount)

print("Sum of evens:",evenSum, "Average of odds sum:",evenSum/evenCount)    
