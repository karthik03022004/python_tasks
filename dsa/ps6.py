'''
Problem: Write a function that takes two numbers as arguments and returns their sum.
Explanation: The function should accept two inputs and return the result of their addition.
Input:
Enter first number: 10
Enter second number: 20
Output:
'''
def add2num(a,b):
    return a+b
print(f"sum = {add2num(10,20)}")

'''
Problem: Write a function that determines whether a number is even or odd.
Explanation: Even numbers are divisible by 2. The function should return “Even” or “Odd”.
Input:
Enter number: 15
Output:
15 is Odd
'''
def even_odd(num):
    if(num&1==1):
        return "odd"
    return "even"
n=10
print(f"{n} is {even_odd(n)}")

'''
Problem: Write a function that checks if a given year is a leap year.
Explanation: A leap year is divisible by 4 but not by 100 unless also divisible by 400.
Input:
Enter year: 2020
Output:
2020 is a Leap Year
'''
def leap(year):
    return (year%400==0 or year%4==0 and year%100!=0)
year=2021
if(leap(year)):
    print(f"{year} is leap year")
else:
    print(f"{year} not a leap year")

'''
Problem: Write a function that checks whether a given number is prime.
Explanation: A prime number has only two factors: 1 and itself.
Input:
Enter number: 13
Output:
13 is a Prime Number
'''
def prime(num):
    factors=0
    for i in range(2,(num//2)+1):
        if(num%i==0):
            factors+=1
            break
    if(factors==0 and num!=1):
        return "prime"
    return "not prime"
num=13
print(f"{num} is a {prime(num)}")

'''
Problem: Write a function that prints all Armstrong numbers in a given range from m to n.
Explanation: Armstrong number = sum of digits raised to the power of number of digits.
Input:
m = 100
n = 500
Output:
Armstrong Numbers between 100 and 500: 153 370 371 407
'''
def armstrong(num):
    s=str(num)
    l=len(s)
    sum=0
    for i in s:
        sum+=int(i)**l
    return sum==num
m=100
n=500
for j in range(m,n+1):
    if(armstrong(j)):
        print(j,end=", ")
        
print()
'''
Problem: Write a recursive function to calculate the factorial of a number.
Explanation: factorial(n) = n * factorial(n - 1), with base case factorial(0) = 1.
Input:
Enter number: 5
Output:
Factorial = 120
'''
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
print(fact(6))

'''
Problem: Print the Fibonacci series up to n terms using recursion.
Explanation: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) with base cases fibonacci(0)=0, fibonacci(1)=1.
Input:
Enter terms: 5
Output:
Fibonacci Series: 0 1 1 2 3

'''
def fib(n):
    if(n==1 or n==0):
        return 0
    elif(n==2):
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))

'''
Problem: Write a recursive function to find the sum of digits of a number.
Explanation: sum(n) = n % 10 + sum(n // 10)
Input:
Enter number: 123
Output:
Sum of digits = 6
'''
def sum_digits(n):
    if(n<=0):
        return 0
    return n%10+sum_digits(n//10)
print("sum:",sum_digits(1237))

'''
Problem: Write a recursive function to reverse the digits of a number.
Explanation: Keep multiplying result by 10 and adding the current digit.
Input:
Enter number: 1234
Output:
Reversed Number = 4321
'''

def reverse(n,rev):
    if rev==0:
        return s[rev]
    return s[rev]+reverse(n,rev-1)


n=1234
s=str(n)
rev=len(s)-1
ans=reverse(s,rev)
print(type(int(ans)))
'''
Problem: Write a recursive function to check if a string is a palindrome.
Explanation: Compare first and last characters and recurse on the substring.
Input:
Enter string: madam
Output:
The string is a palindrome.
'''

def p(s,i):
    if(i==0):
        return s[i]
    return s[i]+p(s,i-1)

s="malayalam"
i=len(s)-1
print(p(s,i)==s)


