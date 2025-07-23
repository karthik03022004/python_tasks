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