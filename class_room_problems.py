'''                longest word in astring           '''
# i love python language     output: language
'''
def longest_word(s):
    s=s.split(" ")
    longest=""
    for i in range(len(s)):
        if(len(longest)<len(s[i])):
            longest=s[i]
    print("lonest word:",longest)
s=input()
longest_word(s)'''


'''               alternate strings combine in a string'''
# s1="13579" 0,1,2,3,4
# s2="2468"  0,1,2,3
'''
s1=input()
s2=input()
itr=""
if(len(s1)<len(s2)):
    itr=s2
else:
    itr=s1
new=""
for i in range(len(itr)):
    if(i<len(s1) and i<len(s2)):
        new+=s1[i]+s2[i] #0,1,2,3
    else:
        new+=itr[i]
print(new)'''


# * * * * * 
# *
# * * * * *
#         *
# * * * * * 


 
    
# rfind()->return last ouccurance of index

# word="siva karthik"
# print(word.rfind(""))

# ch='i'
# index=0
# for i in range(len(word)):
#     if(word[i]==ch):
#         index=i
# print(index)

#                    number methods
#              abs->convets neg values to positive values
# print(abs(-9))

# num=-565
# if(num<0):
#     print(num *(-1))
# else:
#     print(num)


# round()-> it round off nearest value
# print(round(6.46678,3))

# power(base,power)->return exponetial value
# print(pow(3,-20))

# divmod()-> performs div op and it returns two values in a tuple one is quo and other remainder(quo,rem)

# print(divmod(10,7))

# print(round(float("6.8999999"),1))
#  bin()->converts value into binary

# print(bin("7"))
# oct()-> converts int vlaues octal reprasentation
# print(oct(62))

# hexadecimal->converts int values int hexa decimal 16(0-9 a-f)
# print(hex(100))

# isinstance()->return true if it matches the type of value that we mentioned
# print(isinstance("5.3",float))

# print(type("ghojrhgojr"))

#     fibonacii seies 0 1 1 2 3 5 8 13 21 34 55 89 144

# a=0
# b=1
# for i in range(1,6):
#     c=a+b 
#     a=b 
#     b=c 
# print(a)


# armstrong
# '''
# n=407
# dup=n
# s=str(n)
# cnt=len(s)

# print(cnt)
# total=0
# while(n>0):
#     last=n%10 #3
#     total+=last**cnt  #3**3
#     n=n//10
# print(total)
# if(total==dup):
#     print("armstrong")
# else:
#     print("not armstrong")
# '''

for i in range(1,1000):
    num=i
    dup=i
    s=str(i)
    cnt=len(s)
    total=0
    while(num!=0):
        last_digit=num%10
        total+=pow(last_digit,cnt)
        num//=10
    if(total==dup):
        print("armstrong",i)

# conversion









