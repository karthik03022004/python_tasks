# read the 2d array
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    res=[]
    for j in range(col):
        res.append(l[i][j])
    output.append(res)
print(output)

# print sum of each row
output=[]
for i in range(rows):
    sum=0

    for j in range(col):
        sum+=l[i][j]
    output.append(sum)
print(output)

# output=[[7,4,1],[8,5,2],[9,6,3]]
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
cols=len(l[0])
output=[]
for i in range(rows):
    l1=[]
    for j in range(cols):
        # print(l[rows-j-1][i],end=" ")
        l1.append(l[rows-j-1][i])
    output.append(l1)
print(output)

# diagnol sum
dsum=0
for i in range(rows):
    for j in range(cols):
        if(i==j or i+j==rows-1):
            dsum+=l[i][j]
print(dsum)
# -----------------------------------
# 1
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
assume=True
for i in l:
    if(len(i)!=rows):
        assume=False
print("square") if(assume==True) else print("no square")

# 2
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    for j in range(col):
        if(i==j):
            output.append(l[i][j])
print(output)
        
# 3
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    for j in range(col):
        if(i+j==rows-1):
            output.append(l[i][j])
print(output)

# 4
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    for j in range(col):
        if(i!=j):
            output.append(l[i][j])
print(output)

# 5
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    for j in range(col):
        if(i+j!=rows-1):
            output.append(l[i][j])
print(output)
# 6
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        if(i>=j):
            r.append(l[i][j])
        else:
            r.append(0)
    output.append(r)
print(output)
# 7
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        if(i<=j):
            r.append(l[i][j])
        else:
            r.append(0)
    output.append(r)
print(output)
# 8
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        r.append(l[j][i])
    output.append(r)
print(output)
# 9
l=[[1,2,3],[4,1,6],[7,8,1]]
rows=len(l)
col=len(l[0])
ele=l[0][0]
diagnol=True
for i in range(rows):
    if(l[i][i]!=ele):
        diagnol=False
        break
print(diagnol)
# 10
l=[[0, 3],[3, 0]]
rows=len(l)
col=len(l[0])
diagnol=True
ele=l[0][rows-1-0]
for i in range(rows):
    if(ele!=l[rows-1-i][i]):
        diagnol=False
        break
print(diagnol)

# 11
l=[[1, 2],[3, 4]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        if(i==j):
            l[i][j]=0
        r.append(l[i][j])
    output.append(r)
print(output)
# 12
l=[[1, 2],[3, 4]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        if(i+j==rows-1):
            l[i][j]=0
        r.append(l[i][j])
    output.append(r)
print(output)

#13
l=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(l)
col=len(l[0])
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        if(i!=j):
            l[i][j]=0
        r.append(l[i][j])
    output.append(r)
print(output)
# 14
l=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in range(rows):
    for j in range(col):
        sum+=l[i][j]
print(sum)
# 15
A=[[1,2],[3,4]] 
B=[[5,6],[7,8]]
rows=len(A)
col=len(B)
output=[]
for i in range(rows):
    r=[]
    
    for j in range(col):
        res=0
        for k in range(rows):
            res+=A[i][k]*B[k][j]
        r.append(res)
    output.append(r)
print(output)

# sum
output=[]
for i in range(rows):
    r=[]
    for j in range(col):
        sum=A[i][j]+B[i][j]
        r.append(sum)
    output.append(r)
print(output)
        


