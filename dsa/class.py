
#                        slargest
# appr-1
# l=[4,1,2,3,5]
# max=l[0]
# smax=-1
# for i in l:
#     if(i>max):
#         max=i
# for i in l:
#     if(i>smax and i<max):
#         smax=i
# print(smax)
# t.c --3n+2 + 3n+2  ---O(n)
# s.c ---2(max,smax)---O(1)
# ------------------------
# appr-2
# li=[4,4,1,2,3,5,5]
# s=set(li)  #3n+2
# print(s)
# ans=[]
# for i in s:   #3n+2
#     ans.append(i)
# ans.sort()   #nlog(n)
# print(ans)
# print('sec small:',ans[-2])
# t.c -3n+2 +3n+2 +nlog(n) -> O(nlog(n))
# s.c - n+n -- O(n)
# --------------------
# appr-3
# l=[-1,-2,-3]
# maxi=float('-inf')
# slarge=float('-inf')
# for i in l:
#     if(i>maxi):
#         slarge=maxi
#         maxi=i
#     elif(i>slarge and i!=maxi):
#         slarge=i
# print(slarge)
# 3n+2 -O(n)
# s.c-2 -O(1)
# ------------------------
#                   move zeros to last 
# l=[0,1,0,3,12]

# l1=[]
# for i in l:
#     if(i!=0):
#         l1.append(i)
# for i in l:
#     if(i==0):
#         l1.append(i)
# print(l1)
# # t.c=6n+4 steps ->O(n)
# # s.c =n->O(n)
# # -------------------------------
# num=[]
# zero=[]
# for i in l:
#     if(i!=0):
#         num.append(i)
#     elif(i==0):
#         zero.append(i)
# print(num+zero)
# ----------------------------------
# l=[0,1,0,3,12]
# i,j=0,0
# while(i<len(l) and j<len(l)):
#     if(l[i]!=0):
#         temp=l[i]
#         l[i]=l[j]
#         l[j]=temp
#         j+=1
#     i+=1
# print(l)

'''
1) 135=1*1+3*2+5*3=135 (disarium num)
2) {3,1,-1,0} smallest missing pos num =2
3) 123=input find nearest palindrome
'''
# num=135
# s=len(str(num))
# print(s)
# dup=num
# res=0
# while(dup!=0 and s!=0):
#     ld=dup%10
#     res+=ld**s
#     s-=1
#     dup=dup//10
# print("yes") if(num==res) else print("no")

# num=150
# found=False
# while(found==False):
#     s=str(num)
#     if(s==s[::-1]):
#         next=int(s)
#         # print(next)
#         found=True
#     else:
#         num+=1
# n=num
# for i in range(n,0,-1):
#     s=str(i)
#     if(s==s[::-1]):
#         prev=int(s)
#         # print(prev)
#         break
# if(next-n> n-prev):
#     nearest=prev
#     print(nearest)
# else:
#     print(next)
# '''
# 0
# 1 3
# 1 5 13
# 2 8 21 34
# '''
# a=0
# b=1
# l=[]
# for i in range(10):
#     l.append(a)
#     c=a+b
#     a=b
#     b=c
# print(l)
# -----------------------
def isprime(n): # nearest prime
    if(n<2):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True
n=8
if(isprime(n)):
    print(n)
else:
    l=n-1
    r=n+1
    prev_prime=False
    next_prime=False
    while(prev_prime==False):
        if(isprime(l)):
          print(l)
          prev_prime=True
        else:
            l-=1
    
    while(next_prime==False):
        if(isprime(r)):
            print(r)
            next_prime=True
        else:
            r+=1
    if(n-l>r-n):
        print("nearest:",r)
    else:
        print("nearest:",l)
# --------------------------
# check power of 2 
n=512
found=False
for i in range((n//2)+1):
    if(2**i==n):
        found=True
        break
    else:
        found=False
print(i,found)

import math
val=math.log(n,2)
print(isinstance(val,float))

if(n & (n-1)==0):
    print(True)
else:
    print(False)
# sc=O(1)
# tc=O(1)
# --------------
# x power y using recursion
def ps(x,y):
    
    if(y==0):
        return 1
    elif(y<0):
        return (1/ps(x,-y))
    return x*ps(x,y-1)
x,y=2,-3

# x,y=int(input())
print(ps(2,-3))







