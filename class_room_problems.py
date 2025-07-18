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

'''  FIND SUBSTRING IN MAIN STRING 
s1=input()# charan
substr=input()#ran
l=len(substr)
found=False
for i in range(len(s1)):
    if(s1[i:i+l]==substr):
        found=True
        break
if(found==True):
    print("substr is there")
else:
    print("no substr")'''


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

# *
# * *
# * * *
# * * * *
# * * * * *
# rows=5
# for i in range(1,rows+1):
#     pat=""
#     for j in range(1,i+1):
#         pat+="*"+" "
#     print(pat)

#         *
#       * *
#     * * *
#   * * * *
# * * * * * 
rows=5
for i in range(1,rows+1):
    pattern=" "
    for j in range(rows,i-1,-1):
        pattern+=" "+" "
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)


# * * * * * 
# *
# * * * * *
#         *
# * * * * * 
# rows=5
# mid=(rows//2)+1
# for i in  range(1,rows+1):
#     pat=""
#     for j in range(1,rows+1):
#         if(i<=mid):
#             if(i==1 or j==1 or i==mid):
#                 pat+="*"+" "
#             else:
#                 pat+=" "+" "
#         else:
#             if(i==rows or j==rows):
#                 pat+="*"+" "
#             else:
#                 pat+=" "+" "
#     print(pat)


    
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


# armstrong number :Armstrong number is a number where the digits, when raised to a power of cnt of digits and added together, give the same number.

# 153=(1**3)+(5**3)+(3**3)=1+125+27=153

# for i in range(1,501):
#     num=i
#     s=str(num)
#     cnt=len(s)
#     total=0
#     while(num>=1):
#         last_digit=num%10
#         total+=pow(last_digit,cnt)
#         num=num//10
#     if(total==i):
#         print("armstrong:",i)
        
    
# conversion






# ------------jun9 problemsolving-----------------
# anagrams
# s1="dosa"
# s2="soda"
# if(len(s1)!=len(s2)):
#     print("not anagrams")
# else:
#     cnt=0# intially taking cnt=0 to count common char
#     for i in s1: # membership function i= l,i,s,t,e,n
#         if(s1.count(i)==s2.count(i)): #l-1 i-1 s-1 t-1 e-1 n-1
#             cnt+=1 #1 2 3 4
#     if(cnt==len(s1)):#4=4
#         print(s1,s2,"are angrams")
#     else:
#         print(s1,s2," are not anaragams")

# '''            jun10 problemsolving'''

# # find longest palindrome in a word
# word="malayalam"
# longest=""
# for i in range(len(word)):
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]
#         if(temp==temp[::-1] and len(longest)<len(temp)):
#             longest=temp
# print(longest)

# # count and print no of palindromes in a word
# word="malayali"
# cnt=0
# for i in range(len(word)):
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]
#         if(temp==temp[::-1] and len(temp)!=1):
#             cnt+=1
#             print(temp)
# print(cnt)

# # shortest palindrome

s="ABBBBB" #output:a5b2c3
i=0
res=""
while(i<len(s)):
    cnt=1
    
    for j in range(i,len(s)-1):
        if(s[j]==s[j+1]):
            cnt+=1
        else:
            break
    res+=s[j]+'-'+str(cnt)+" "
    i+=cnt
    
  

print(res)   









    

