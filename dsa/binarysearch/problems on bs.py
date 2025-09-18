# n=-64
# n1=abs(n)
# ans=0
# for i in range(n1):
#     if(i*i*i==n1):
#         ans=i
#         break
# if(n<0):
#     ans=ans*-1
#     print(ans)
# else:
#     print(ans)

# def cube_root(n):  #cube root using binary search 
#     s=abs(n)
#     low=0
#     high=s
#     ans=0
#     while(low<=high):
#         mid=(low+high)//2
#         if(mid*mid*mid==s):
#             ans=mid
#             break
#         elif(mid*mid*mid>s):
#             high=mid-1
#         else:
#             low=mid+1
#     if(n<0):
#         ans=-1*ans
#         print(ans)
#     else:
#         ans=1*ans
#         print(ans)
# cube_root(-125)

# l=[1,2,3,3,3]
# #use dict 
# low=0
# high=len(l)-1
# if(l[-1]!=l[-2]):
#     print(l[-1])
    
# if(l[0]!=l[1]):
#     print(l[0])
# else:
#     while(low<=high):
#         mid=(low+high)//2
#         if(l[mid]!=l[mid+1] and l[mid]!=l[mid-1]):
#             print(l[mid])
#             break
#         elif(mid%2==1):
#             if(l[mid]==l[mid-1]):
#                 low=mid+1
#             else:
#                 high=mid-1
#         elif(mid%2==0):
#             if(l[mid]==l[mid+1]):
#                 low=mid+1
#             else:
#                 high=mid-1

# binary search :-> searching an element in a sorted collection(list,array,set)
# linear search:-> searching element from start to end in a collection
# time complexity:O(n) space complexity:O(1)
# l=[10,20,30,40,50] #t=40 output:3
# t=40
# for i in range(len(l)):
#     if(l[i]==t):
#         print(i)
#         break

# binary search :-> searching an element in a sorted collection(list,array,set)
# time complexity:O(n) space complexity:O(1)
# l=[10,20,30,40,50] #t=40 output:3
# t=40
# i=0
# j=len(l)-1
# while(i<=j):
#     mid=(i+j)//2
#     if(t==l[mid]):
#         print("index:",mid)
#         break
#     elif(l[mid]<t):
#         i=mid+1
#     elif(l[mid]>t):
#         j=mid-1


# finding using square root using binary search
n=64
low=0
high=n
found=False
if(low==n):
    found=True
    print(low)
else:
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid==n):
            found=True
            print(mid)
            break
        elif(mid*mid>n):
            high=mid-1
        elif(mid*mid<n):
            low=mid+1
print("no int root") if(found==False) else  print("root found")


        
