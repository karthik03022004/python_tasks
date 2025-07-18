# append
# extend
# insert(val,ind)
# remove(val)
# pop(ind)
# clear()
# reverse()
# sort()
# ------above one is mutating methods
# count()
# index()
# copy()
'''----------------------------------------------------------------'''
# # ->sum of elememts-sum() method
# num=[1,2,3,4,5,6,7,8,-9]
# print("sum:",sum(num))

# #-> returns max of elements-max() method
# print("max:",max(num))
# # highest=max(5,6,7,809)
# # print(highest)

# # returns min of elements-> min() method
# print("min:",min(num))

# # print the second highest
# highest=max(num)
# num.remove(highest)
# print(num)
# print("second highest:",max(num))

# fun to print nth highest
# def nhighest(li,n):
#     if(len(li)<n):
#         return "not possible"
#     else:
#         for i in range(n-1):
#             highest=max(li)
#             li.remove(highest)
#     return max(li)
# l=[9,9,8,8,7,7,6,6,5,5]
# n=7
# # here we are removing duplicates
# new=[]
# for i in l:
#     if(i not in new):
#         new.append(i)
# print(new)
# print(f"{n}th highest is {nhighest(new,n)}")

# num=[-2,-4,-6,-8,-90,-900,-10000]
# highest=num[0] # logic to finding highest in a list 
# for i in num:
#     if i>highest:
#         highest=i
# print("maxiuum:",highest)

# tot=0
# for i in num: #sum logic 
#     tot+=i
# print(tot)

# index logic
# food=["birayani","noodels","fry","icecream","mommos","fry","fry"]
# item="fry"
# for i in range(len(food)):
#     if(food[i]==item):
#         print(f"{food[i]} is at {i+1} position")
#         break

# # count logic
# count=0
# for i in food:
#     if(i==item):
#         count+=1
# print(count)

# # reverse logic
# rev=[]
# for i in range(len(food)-1,-1,-1):
#     rev.append(food[i])
# print(rev)

# #task-  list=[1,"A",2,"B","a","z"]  output:us=AB ls=az sum=3
# l=[1,"A",2,"B","a",'z']
# us=""
# ls=""
# sum=0
# for i in l:
#     i=str(i)
#     if(ord(i)>=65 and ord(i)<=90):
#         us+=i
#     elif(ord(i)>=97 and ord(i)<=122):
#         ls+=i
#     else:
        
#         sum+=int(i)
# print(sum,us,ls)
# '''---------------------------------------------------------------------------'''
# nested list
# sum of numbers in a nested list 
nested=[1,[2,3]]
sum=0
for i in nested:
    if(isinstance(i,list)):
        for j in i:
            sum+=j
    else:
        sum+=i
print("sum of nested list:",sum)

# print(isinstance(1,int))
# print(isinstance(2.3,float))
# print(isinstance(True,bool))
# print(isinstance({},dict))
# ---task - to check the data type of an user input 
# n=eval(input())
# if(isinstance(n,int)):
#     print("class <int>")
# elif(isinstance(n,float)):
#     print("class <float>")
# elif(isinstance(n,bool)):
#     print("class <bool>")
# elif(isinstance(n,complex)):
#     print("class <complex>")
# elif(isinstance(n,str)):
#     print("class <str>")
# elif(isinstance(n,list)):
#     print("class <list>")
# elif(isinstance(n,tuple)):
#     print("class <tuple>")
# elif(isinstance(n,dict)):
#     print("class <dict>")
# else:
#     print("class <set>")

num=[[-1,-2],[-3,-4],[-5,6]] # find the max sum value of a sublist
max_list=[]
# max_val=0 # won't work for neg val in sublist
max_val=num[0][0]
for i in num:
    sum=0
    for j in i:
        sum+=j
    if(sum>max_val):
        max_val=sum
        max_list=i
print(max_val,max_list)

num=[[1,5],[3,-6],[100,900]]
maxi=num[0][0]
for i in num:
    for j in i:
        if(j>maxi):
            maxi=j
print("maximum value:",maxi)
# task to find mini val in a sub list
mini=num[0][0]
for i in num:
    for j in i:
        if(j<mini):
            mini=j
print("minimum val in sub list:",mini)

# matrix - finding matrix is square or not
matrix=[
    [1,2,3,3],
    [4,5,6,3],
    [8,9,10,3],
    [7,7,7,7]
]
rows=len(matrix)
sq_matrix=True
for i in matrix:
    if(rows!=len(i)):
        sq_matrix=False
    
print("square matrix") if sq_matrix else print("not a square matrix")
'''-----------------------------------------------------------------------'''
# checking 2 matrices has has same rows and cols
mat1=[
    [1,2],
    [3,4]
]
mat2=[
    [5,6],
    [7,8]
]
if(len(mat1)!=len(mat2)):
    print("rows and cols are not equal so arthmetic op are not possible.")
else:
    possible=True
    for i in range(len(mat1)):
        if(len(mat1[i])!=len(mat2[i])):
            possible=False
    print("matrices have same rows and cols") if possible else print("rows and cols are not equal so arthmetic op are not possible.")
# addition of 2 matrices
addition=[]
for i in range(len(mat1)):
    row=[]
    for j in range(len(mat1)):
        sum=mat1[i][j]+mat2[i][j]
        row.append(sum)
    addition.append(row)
print(addition)
# subraction of 2 matrices
subraction=[]
for i in range(len(mat1)):
    row=[]
    for j in range(len(mat1)):
        res=mat1[i][j]-mat2[i][j]
        row.append(res)
    subraction.append(row)
print(subraction)
# multipliation of 2 matrices
# check condition->cols of mat1==rows of mat2
mul_check=True
for i in mat1:
    if(len(i)!=len(mat2)):
        mul_check=False
        break
if(mul_check):
    mul=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat2[0])):
            res=0
            for k in range(len(mat2)):
                res+=mat1[i][k]*mat2[k][j]
            row.append(res)
        print(row)
    
            












