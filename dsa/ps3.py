'''problem solving 3'''
'''
. Print Numbers from 1 to n
Question: Write a program to prime numbers from 1 to n. Explanation: Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5

'''
n=20
for i in range(1,n+1):
    factors=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            factors+=1
            break
    if(factors==0 and i!=1):
        print(i)
# -------------------------------------------
'''
2. Print Numbers from m to n
Question: Write a program to prime numbers from m to n. Explanation: Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7

'''
m=3
n=7
for i in range(m,n+1):
    factors=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            factors+=1
            break
    if(factors==0 and i!=1):
        print(i)
# -----------------------------------------
'''
Print Numbers from n to 1 in Reverse
Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1

'''
n=5
for i in range(n,0,-1):
    factors=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            factors+=1
            break
    if(factors==0 and i!=1):
        print(i)
print("-----------------------------------")
# ----------------------------------------
'''
Print Numbers from n to m in Reverse
Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6

'''
def prime(n):
    factors=0
    for i in range(1,n+1):
        if(n%i==0):
            factors+=1
    if(factors==2 and i!=1):
        return True
    return False
a=10
b=1
for j in range(a,b-1,-1):
    if(prime(j)):
        print(j)
print("-----------------------------------")
'''
Question: Write a program to calculate the sum of first n natural numbers. Explanation: Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15
'''
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("sum:",sum)
print("-----------------------------------")
'''
Factorial of a Number
Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120

'''
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial:",fact)
print("-----------------------------------")

'''
Sum of m to n Numbers
Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18
'''
m=3
n=6
sum=0
for i in range(m,n+1):
    sum+=i
print("sum in a range",sum)
print("-----------------------------------")
'''
Product of m to n Numbers
Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24
'''
def product(m,n):
    pro=1
    for i in range(m,n+1):
        pro=pro*i
    return pro

print("product:",product(2,4))
print("-----------------------------------")

'''
Question: Write a program to print all factors of a given number. Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6
'''
n=6
for i in range(1,n+1):
    if(n%i==0):
        print(i)
'''
Question: Write a program to count how many factors a number has. Explanation: Increment count when divisible. - Input: n = 6 - Output: 4
'''
num=6
cnt=0
for i in range(1,num+1):
    if(num%i==0):
        cnt+=1
print("cnt of factors:",cnt)
print("-----------------------------------")

'''
Question: Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime
'''
def prime(num):
    factors=0
    for i in range(2,(num//2)+1):
        if(num%i==0):
            factors+=1
            break
    if(factors==0 and num!=1):
        print("prime")
    else:
        print("not prime")
prime(1)
print("---------------------------------")
'''
Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10
'''
for i in range(3,11):
    if(i%2==0):
        print(i)
print("-------------------")
'''
Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9
'''
for i in range(3,11):
    if(i%2!=0):
        print(i)
print('------------------------')

'''
Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3
'''
cnt_even=0
cnt_odd=0
for i in range(3,8):
    if(i%2==0):
        cnt_even+=1
    elif(i%2==1):
        cnt_odd+=1
print(cnt_odd,cnt_even)
print('------------------------------')
'''
15. Reverse a String
Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”
'''
inp="hello"
# print('reverse:',inp[::-1])
rev=""
for i in inp[::-1]:
    rev+=i
print(rev)
'''
16. Check for Palindrome String
Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome
'''
s="madam"
palidrome=""
for i in s:
    palidrome=i+palidrome
print(palidrome)
'''
Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6
'''
num=123
snum=str(num)
sum=0
for i in snum:
    sum+=int(i)
print("sum",sum)

# product of digits
a=1234
pro=1
while(a!=0):
    last=a%10
    pro*=last
    a=a//10
print("product:",pro)

# armstrong
a=153
dup=a
l=len(str(a))
arm=0
while(a!=0):
    last=a%10
    arm+=last**l
    a=a//10
print(arm==dup)
print('------------------------')
'''
Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321
'''
num=123
rev=0
while(num!=0):
    last=num%10
    rev=rev*10+last
    num=num//10
print("reverse:",rev)
'''
Question: Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome
'''
num=121
nu=num
rev=0
while(num!=0):
    last=num%10
    rev=rev*10+last
    num=num//10
print('it is plaindrome')if(nu==rev) else print("not palindrome")
# ------------
'''
Question: Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2
'''
string="apple"
cnt_vowel=0
for i in string:
    if i in "aeiou":
        cnt_vowel+=1
print(cnt_vowel)

'''
Question: Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 3
'''
s="apple"
cnt_cons=0
for i in s:
    if i not in 'aeiou':
        cnt_cons+=1
print(cnt_cons)

'''
Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3
'''
s="apple"
cnt_cons=0
cnt_vowel=0
for i in s:
    if i not in 'aeiou':
        cnt_cons+=1
    if i in 'aeiou':
        cnt_vowel+=1
print(cnt_cons)
'''
Question: Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number
'''
num=28
sum_factors=0
for i in range(1,(num//2)+1):
    if(num%i==0):
        sum_factors+=i
print("perfect") if(num==sum_factors) else print("not perfect")

'''neon number'''
num=9
sq=num*num
s=str(sq)
sum_digits=0
for i in s:
    sum_digits+=int(i)
print("neon") if(sum_digits==num) else print("not neon")\
# perfect number- sum of factorial of each digit ==number
def factorial(num):
    p=1
    for i in range(num,0,-1):
        p=p*i
    return p
sum=0
n=145
n1=n
while(n!=0):
    ld=n%10
    sum+=factorial(ld)
    n=n//10
print("strong") if(sum==n1) else print("not strong")
# --------------------
num=18
sum_dig=0
string=str(num)
for i in string:
    sum_dig+=(int(i))
print("harshad num") if((num%sum_dig==0)) else print("not harshad")
# fibonacii seies
a=0
b=1
num=7
for i in range(1,num+1):
    print(a)
    c=a+b
    a=b
    b=c
