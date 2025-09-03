# # bubble sort
# l=[5,7,2,10,1]
# swaps=0
# for i in range(len(l)):
#     for j in range(len(l)-1):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
#             swaps+=1

# print("bubble sort:",l,swaps)
# # selection sort
# l=[5,7,2,10,1]
# swaps=0
# for i in range(len(l)):
#     ind=i
#     for j in range(i,len(l)):
#         if(l[ind]>l[j]):
#             ind=j
#     l[i],l[ind]=l[ind],l[i]
#     swaps+=1
# print("selection sort:",l,swaps)


# # insertion sort
# l=[5,7,2,10,1]
# swaps=0
# for i in range(len(l)):
#     j=i
#     while(l[j-1]>l[j] and j>=1):
#         l[j-1],l[j]=l[j],l[j-1]
#         swaps+=1
#         j-=1
# print("insertion sort:",l,swaps)
# # binary search
# arr=[10,20,30,40,50]
# t=40
# i=0
# j=len(arr)-1
# while(i<=j):
#     mid=(i+j)//2
#     if(arr[mid]==t):
#         print(mid)
#         break
#     elif(arr[mid]>t):
#         j=mid+1
#     else:
#         i=mid+1



