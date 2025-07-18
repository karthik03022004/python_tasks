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
food=["birayani","noodels","fry","icecream","mommos","fry","fry"]
item="fry"
for i in range(len(food)):
    if(food[i]==item):
        print(f"{food[i]} is at {i+1} position")
        break
# count logic
count=0
for i in food:
    if(i==item):
        count+=1
print(count)
# reverse logic
rev=[]
for i in range(len(food)-1,-1,-1):
    rev.append(food[i])
print(rev)

#task-  list=[1,"A",2,"B","a","z"]  output:us=AB ls=az sum=3
l=[1,"A",2,"B","a",'z']
us=""
ls=""
sum=0
for i in l:
    i=str(i)
    if(ord(i)>=65 and ord(i)<=90):
        us+=i
    elif(ord(i)>=97 and ord(i)<=122):
        ls+=i
    else:
        
        sum+=int(i)
print(sum,us,ls)




