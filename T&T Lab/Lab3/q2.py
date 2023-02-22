# WAP to calculate the sum of digits of a given number.

def sum_of_digits(num):
    sum = 0
    while (int(num)>0):
        remainder = num % 10
        sum = sum+int(remainder)
        num = num / 10
    print("Sum of digits is: ",sum)
    
sum_of_digits(123)
    