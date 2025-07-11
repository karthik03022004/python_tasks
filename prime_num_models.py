# num=7
# facts=0
# for i in range(2,(num//2)+1):
#     if(num%i==0):
#         facts+=1
#         break
# if(facts==0):
#     print("primenum")
# else:
#     print("not prime")
'''----------------------------------------------------------'''
# print prime numbers in given range and count primes in range
num=200
cnt=0
for i in range(1,num+1):
    facts=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            facts+=1
            break
    if(facts==0 and i!=1):
        cnt+=1
        print("prime:",i)
print("count of prime numbers:",cnt)
'''-------------------------------------------------------'''
# print nth prime number
# 2,3,5,7,11,13,17,19

# n=25
# cnt=0
# num=2
# while(cnt!=n):
#     fact=0
#     for i in range(2,(num//2)+1):
#         if(num%i==0):
#             fact+=1
#             break
#     if(fact==0):
#         p=num
#         cnt+=1
#         num+=1
#     else:
#         num+=1
# print(p)
'''------------------------------------------------------'''

# print next prime number
n=9 #output:17
n1=n
found=False # to enter into loop assumin i didnt find any prime
while(found==False): 
    n1+=1 #next prime
    fact=0 #checkinf factors
    for i in range(2,(n1//2)+1): #12->factors:1,2,3,4,6,12
        if(n1%i==0):
            fact+=1
            break
    if(fact==0):
        next_prime=n1
        print("next prime",next_prime)
        found=True
    else:
        found=False
print(n)
# find previous prime
# n=13 #output:11
for i in range(n-1,1,-1):
    fact=0
    for j in range(2,(i//2)+1):
        if(i%j==0):
            fact+=1
            break
    if(fact==0):
        prev_prime=i
        print("previous prime",prev_prime)
        break

# find nearest prime
if((next_prime-n)>(n-prev_prime)):
    print("nearest prime:",prev_prime)
elif((next_prime-n)<(n-prev_prime)):
    print("nearest prime:",next_prime)
else:
    print(prev_prime,n,next_prime,"are same distance")




    
        