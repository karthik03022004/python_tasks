'''                    LCM of 2 numbers             '''
n1=int(input())
n2=int(input())
big=0
small=0
big,small=(n1,n2) if n1>n2 else (n2,n1)
print(big,small)
if(big % small ==0):
    print("lcm:",big)
lcm_found=False
lcm=big
while lcm_found==False:
    
    if(lcm%n1==0 and lcm%n2==0):
        print("lcm:",lcm)
        lcm_found=True
    else:
        lcm+=big


