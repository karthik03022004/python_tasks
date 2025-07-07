'''                    LCM of 2 numbers             
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

'''

'''LCM (least common multiple): finding  common multiple least from 2 numbers'''

# (3,9)lcm=9
# 9=9,18,27...
# 3=3,6,9,12...

# (5,10)lcm=10
# 5=5,10,15,20,25..
# 10=10,20,30...

# (8,12)lcm=24
# 12=12,24,36,48,60...
# 8=8,16,24,32,40....

# (11,13)lcm=143
# 11=11,22,33,44,55,66,77,8,99,110,121,132,143..,
# 13=13,26,39 52,65,78,91,104,117,130,143..
