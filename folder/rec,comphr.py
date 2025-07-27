# # factorial usig loop
# def factorial(n):
#     f=1
#     for i in range(n,0,-1):
#         f*=i
#     return f

# n=7
# print(factorial(n))
# -------------------------------------------
# factorial using reccursion
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# n=5
# print(factorial(n))
# -----------------------------------------------------
# fibonacci number
# 0 1 1 2 3 5 8 13 21 34 55 
# n=3
# if(n==1 or n==0): print(0)
# elif(n==2): print(1)
# n1=0
# n2=1
# for i in range(2,n):
#     next=n1+n2
#     n1=n2
#     n2=next
# print(next)
# -----------------------------------------------
# fib series
# n=10
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     res=a+b
#     a=b
#     b=res
# ----------------------------------------------
'''Recursion'''
# def fibonacci(n):
#     if(n==0 or n==1):
#         return 0
#     elif(n==2):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# n=10
# print(fibonacci(n))
'''------------------------------------------------------------------------------------'''
# compreshion 
l=[1,2,3,4,5,6,7,8,9,10]
new=[i for i in l if i%3==0]
print(new)
'''-------------------------------------------------------'''
# convert lower to upper
name=["siva","charan"]
name_list=[word.upper() for word in name]
print(name_list)
'''---------------------------------------'''
# print squares of num
num_list=[i**2 for i in range(1,10)]
print(num_list)
'''--------------------------------------------------'''
# dict comprehnsion
# count of each caharcter in a string and find highest reapeating
word="hari hara "
output={x:word.count(x) for x in word if x!=' '}
print(output)
high=0
c=""
for i in word:
    cnt=word.count(i)
    if(cnt>high):
        high=cnt
        c=i
print(c,high)
'''--------------------------------------------------------------------------'''
# swap keys and values
data={
    "dominos":"pizza",
    "buger king":"buger",
    "biryani":"barawarchi"
}
new_data={data[key]:key for key in data}
print(new_data)
'''--------------------------------------------------'''
# print key and len of key
len_data={val:len(val) for val in data.values()}
print(len_data)
'''--------------------------------------------'''
# print val>50
val={
    'a':40,
    'b':60,
    'c':76,
    'd':56,
}
new={k:v for k,v in val.items() if(v>50)}
print(new)
'''---------------------------------------------------'''
# finding highest and lowest val in dict
high=0
c=''
for k,v in val.items():
    if(v>high):
        high=v
        c=k
print(f"max:{c},{high}")
low=high
low_c=''
for k,v in val.items():
    if(v<low):
        low=v
        low_c=k
print(f"low:{low},{low_c}")
'''-------------------------------------------------------'''
'''           set comprenhsion     '''
# finding vowels in string
s="i am doing python"
res={ch for ch in s if ch in 'aeiou'}
print(res)
'''-------------------------------------------'''
# output:{'Python', 'Am', 'I', 'Doing'}
s=s.split(" ")
res1={i.title() for i in s}
print(res1)
'''---------------------------------------'''
# print words start with vowels
l=['apple','ubuntu','unix']
new_set={word for word in l if word[0] in 'aeiou'}
print(new_set)
'''----------------------------------------------------'''
# matrix(transpose)

matrix=[
   [1,2,3],
   [4,5,6]
]
'''
[1,4]
[2,5]
[3,6]
'''
out=[]
for j in range(len(matrix[0])):#0,1,2
    row=[]
    for i in range(len(matrix)):#0,1
        
        row.append(matrix[i][j])
    out.append(row)
print(out)

