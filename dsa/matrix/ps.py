# l=[[1,2,3],[4,5,6],[7,8,9]]
# n=len(l)
# d=n+(n-1)
# for i in range(d):
#     sum=0
#     if(i<=d//2):
#         r=n-(i+1)
#         for j in range(i+1):
#             sum+=l[j][r]
#             r+=1
#         print(sum)
#     else:
#         c=n-(d-i)
#         for j in range(d-i):
#             sum+=l[c][j]
#             c+=1
#         print(sum)

l=[[27,29,53],[-28,49,-24]] 
m=[[23,52,-38,72],[-64,15,-59,-10],[-75,43,10,25]]
found=True
for i in range(len(l)):
    if(len(l[i])!=len(m)):
        found=False
        break
print(found)


row1=len(l)
row2=len(m)
col1=len(l[0])
col2=len(m[0])
if(col1>col2):
    itr=col2
else:
    itr=col1
output=[]

for i in range(row1):
    res=[]
    for j in range(col2):
        sum=0
        for k in range(itr):
            sum+=l[i][k]*m[k][j]
        res.append(sum)
    output.append(res)
print(output)
        
# traling zeros
n=4
cnt_z=0
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
str_fact=str(fact)
for i in str_fact[::-1]:
    
    if(i=="0"):
        cnt_z+=1
    else:
        break    
print(cnt_z)
