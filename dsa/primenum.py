r=5
n=7 #output: 11 13 17 19 23
i=1
while(i<=r):
    n+=1
    for j in range(2,(n//2)+1):
        factors=0
        if(n%j)==0:
            factors+=1
            break
    if(factors==0):
        print(n)
        i+=1
'''---------------------------------------------'''
s="vivekananda"
l=[]
for i in range(len(s)):
    cnt=0
    for j in range(i,len(s)):
        if(s[i]==s[j]):
            cnt+=1
    if(s[i] not in l):
        l.append(s[i])
        l.append(cnt)
print(l)
# ------------------------------------------
# class room problems
def add2num(a,b):
    return a+b
print(f"sum of 2 numbers using function:{add2num(2,3)}")
# ---------------------------------
def even_or_odd(n):
    if(n&1==0):
        return "even"
    return "odd"
print(even_or_odd(9))
# --------------------------------
def leap_year(year):
    if(year%400==0 or (year%4==0 and year%100!=0)):
        return True
    return False
cnt=0
for i in range(2000,2026):
    if(leap_year(i)):
        cnt+=1
        print(i,end=", ")
print(cnt)
# -------------------------------
def prime(num):
    factors=0
    for i in range(2,(num//2)+1):
        if(num%i==0):
            factors+=1
            break
    if(factors==0):
        if(num!=1):
            return True
    return False
for j in range(1,51):
    if(prime(j)):
        print(j,end=", ")
# ---------------------------------------
