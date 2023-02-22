# WAP to calculate the factorial of a given number.

def fact(n):
    factorial = 1
    for item in range(1,n+1):
        factorial += item
    return factorial

#num = int(print("Enter a number: "))
print("The factorial is ",fact(n = 10))