# r=5
# n=7 #output: 11 13 17 19 23
# i=1
# while(i<=r):
#     n+=1
#     for j in range(2,(n//2)+1):
#         factors=0
#         if(n%j)==0:
#             factors+=1
#             break
#     if(factors==0):
#         print(n)
#         i+=1
# '''---------------------------------------------'''
# s="vivekananda"
# l=[]
# for i in range(len(s)):
#     cnt=0
#     for j in range(i,len(s)):
#         if(s[i]==s[j]):
#             cnt+=1
#     if(s[i] not in l):
#         l.append(s[i])
#         l.append(cnt)
# print(l)
# # ------------------------------------------
# #                          class room problems
# def add2num(a,b):
#     return a+b
# print(f"sum of 2 numbers using function:{add2num(2,3)}")
# # ---------------------------------
# def even_or_odd(n):
#     if(n&1==0):
#         return "even"
#     return "odd"
# print(even_or_odd(9))
# # --------------------------------
# def leap_year(year):
#     if(year%400==0 or (year%4==0 and year%100!=0)):
#         return True
#     return False
# cnt=0
# for i in range(2000,2026):
#     if(leap_year(i)):
#         cnt+=1
#         print(i,end=", ")
# print(cnt)
# # -------------------------------
# def prime(num):
#     factors=0
#     for i in range(2,(num//2)+1):
#         if(num%i==0):
#             factors+=1
#             break
#     if(factors==0):
#         if(num!=1):
#             return True
#     return False
# for j in range(1,51):
#     if(prime(j)):
#         print(j,end=", ")
# print()
# # ---------------------------------------
# '''
# # a b
# c # d
# e f #
# '''
# n=3
# code=97
# for i in range(1,n+1):
#     rows=""
#     for j in range(1,n+1):
#         if(i==j):
#             rows+="#"+" "
#         else:
#             rows+=chr(code)+" "
#             code+=1
#     print(rows)
# # -------------------------
# # s="wxy"  #output:"xyz"
# # new=""
# # for i in s:
# #     code=ord(i)+1
# #     if(ord(i)>=122):
# #         new+=chr(ord(i)-25)
# #     new+=chr(code)
# # print(new[:3])

# # s="_siva_charan"  #output:SivaCharan
# # new=""
# # print(new)
# # for i in range(1,len(s)):
# #     if(s[i-1]=="_"):
# #         new+=s[i].upper()
       
# #     elif s[i]!="_":
        
# #         new+=s[i]
# # print(new)

# s="MyNameIs" #output:"my_name_is"
# res=s[0].lower()
# for i in range(1,len(s)):
#     if(s[i].isupper()):
#         res+="_"+s[i].lower()
#     else:
#         res+=s[i]
# print(res)
# s = "he llo wor ld"
# new = ""
# for i in range(len(s)):
#     if s[i] != ' ':
#         new += s[i]
# print(new)
# # ----------------------------
# def reverse(s):
#     new=""
#     for i in s:
#         new=i+new
#     print(new)
# reverse("hello")
# # ------------------
# def spacerev(s):
#     new=""
#     for i in range(len(s)-1,-1,-1):
#         if(s[i]!=" "):
#             new+=s[i]
#     print(new)
# spacerev("he llo wor ld")
# # ---------------------------------
# # . Input: "my_variable_name" Output: "myVariableName"
# inp="my_variable_name"
# new=""
# for i in range(1,len(inp)):
#     if(inp[i-1]=="_"):
#         new+=inp[i].upper()
#     elif(inp!="_"):
#         new+=inp[i]
# print(new)
# # ---------------------------------
# s="hELLo"
# new=""
# for i in s:
#     if(i.isupper()):
#         new+=i.lower()
#     else:
#         new+=i.upper()
# print(new)
# # ---------------------------------
# # strong password
# s=""
# small=0
# cap=0
# numcount=0
# spc=0
# if(len(s)>=8 and len(s)<=16):
#     for i in s:
#         if(ord(i)>=97 and ord(i)<=122):
#             small+=1
#         elif(ord(i)>=65 and ord(i)<=90):
#             cap+=1
#         elif(ord(i)>=48 and ord(i)<=57):
#             numcount+=1
#         else:
#             spc+=1
# if(small>=1 and cap>=1 and numcount>=1 and spc>=1):
#     print("strong password")
# else:
#     print("weak")
# # ---------------------------------
# s="aabbcc"
# l=""
# for i in s:
#     if i not in l:
#         l+=i
# print(l)


# value={
#     "I":1,
#     "v":5,
#     "X":10,
#     "L":50,
#     "C":100,
#     "M":1000
    
# }
# s="LCV"
# res=0


# # -------------------------------
# l=[2,3,4,5,6,6,6,6,7,8,9,9]  #secmax=4 secmin=2
# maxi=0
# sec_max=-1
# for i in l:
#     if(i>maxi):
#         maxi=i
# for i in l:
#     if(i>sec_max and i!=maxi):
#         sec_max=i
# print(sec_max)
# mini=maxi
# sec_mini=sec_max
# for i in l:
#     if(i<mini):
#         mini=i
# for i in l:
#     if(i<sec_mini and i!=mini):
#         sec_mini=i
# print(sec_mini)
    

# # L=[1,2,9]
# # res=0
# # for i in L:
# #     res=res*10+i
# # print(res+1)
# # l=[]
# # for i in str(res+1):
# #     l.append(i)
# # print(l) #[1,3,0]
# a=[10,9,8]
# b=[1,2,3,4,5,6,7]
# res=[]
# p1,p2=0,0
# while(p1<len(a) and p2<len(b)):
#     if(a[p1]<b[p2]):
#         res.append(a[p1])
#         p1+=1
#     elif(a[p1]==b[p2]):
#         res.append(a[p1])
#         p1+=1
#         res.append(b[p2])
#         p2+=1
#     else:
#         res.append(b[p2])
#         p2+=1
# if(p1>p2):
#     while(p2<len(b)):
#         res.append(b[p2])
#         p2+=1
# else:
#     while(p1<len(a)):
#         res.append(b[p1])
#         p1+=1
# print(res)
# a="110011110011111110"  "longest:11111"    
# cnt=0
# res=0
# for i in a:
#     if(i=="1"):
#         cnt+=1
#         if(cnt>res):
#             res=cnt
#     else:
#         cnt=0
# print(res)
# print("--------")
# l=[1,1,7,1,1]
# num=len(l)//2 #2
# p1=num-1
# p2=num+1
# while(p1>=0 and p2<=len(l)-1 and l[num]>=2):
#     l[p1]+=1
#     l[p2]+=1
#     l[num]-=2
#     p1-=1
#     p2+=1
# print(l)
n=10
for i in range(n,0,-1):
    ls=" "*(n-i)
    if i==1 :
        print("*"+ls+"*"*(i)+ls+"*")
    else:
        if i==n:
            print("* "+"  "*(n-1)+"*")
            print("*"+ls+"* "+"  "*(i-2)+"*"+ls+"*")
        else:
            
            print("*"+ls+"* "+"  "*(i-2)+"*"+ls+"*")
for i in range(2,n+1):
    ls=" "*(n-i)
    if i==1 :
        print("*"+ls+"* "*(i)+ls+"*")
    else:
        
        if i==n:
            
            print("*"+ls+"* "+"  "*(i-2)+"*"+ls+"*")
            print("* "+"  "*(n-1)+"*")
        else:
            
            print("*"+ls+"* "+"  "*(i-2)+"*"+ls+"*")















    