# sumof pairs
l=[1,4,5,2,7] #output:true 4+2=6
t=9
# found=False
# for i in range(len(l)):
#     sum=0
#     for j in range(i+1,len(l)):
#         if(l[i]+l[j]==t):
#             found=True
#             break
# if(found):
#     print(True)
# else:
#     print(False)

# 2 pointers
l.sort()
i=0
j=len(l)-1
found=False
while(i<=j):
    if(l[i]+l[j]==t):
        found=True
        break
    elif(l[i]+l[j]<t):
        i+=1
    else:
        j-=1
print(True,i,j) if(found) else print(False)
        

