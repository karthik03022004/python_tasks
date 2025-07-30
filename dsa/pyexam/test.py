# 1)
s=input("enter:")
upper=""
lower=""
number=""
sym=""
space_cnt=0
for i in s:
    if(i>="A" and i<="Z"):
        upper+=i
    elif(i>='a' and i<='z'):
        lower+=i
    elif(i>='0'and i<='9'):
        number+=i
    if(i==" "):
        space_cnt+=1
    else:
        sym+=i
print(upper,lower,number,sym,space_cnt)
#---------------------------------------------------------
# 2)
m=int(input("enter:"))
n=int(input("enter:"))
cnt=0
for i in range(m,n+1):
    factors=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            factors+=1
            break
    if(factors==0):
        
        cnt+=1
print(cnt)
#------------------------------------------------------------------
# 3)
n = 5
for i in range(n, 0, -1):
    sp = " " * (n - i)
    row = ""
    for j in range(1, i + 1):
        row += str(j) + " "
    print(sp + row)
# --------------------------------------------------------------------
# 4)
n1="111"
n2='1'

def dec(n1):
    res=0
    for i in range(len(n1)):
        if(n1[len(n1)-i-1]=="1"):
            res+=1*(2**i)
        else:
            res+=0
    return res
r1=dec(n1)
r2=dec(n2)
print(bin(r1+r2))


    

        
    