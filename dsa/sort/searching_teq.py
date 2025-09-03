# binary serach :
def first_ele(l,t):
    i=0
    j=len(l)-1
    res=-1
    while(i<=j):
        mid=i+(j-i)//2
        if(l[mid]==t):
            res=mid
            j=mid-1
        elif(l[mid]<t):
            i=mid+1
        else:
            j=mid-1
    return res
def last_ele(l,t):
    i=0
    j=len(l)-1
    r=-1
    while(i<=j):
        mid=i+(j-i)//2

        if(l[mid]==t):
            r=mid
            i=mid+1
        elif(l[mid]<t):
            i=mid+1
        else:
            j=mid-1
    return r

l=[1,2,3,3,3,4] #output:2(first 3 ) and 4(last 3)
t=3
print(first_ele(l,t))
print(last_ele(l,t))