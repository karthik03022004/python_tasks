'''--------------------------------LCM--------------'''
'''
n1=3  3,6,9,12..
n1=6 6 12 18... lcm=6

n1=12  12 24 36 48......
n2=24  24 48 72 98.........  lcm=24

15=15 30 45 60 75 90 105 120 135 150
18=18,36,54,72,90,108,126,144,162,180 lcm=90
'''
# n1=15
# n2=5
# small=0
# big=0
# if(n1>n2):
#     big=n1
#     small=n2
# else:
#     big=n2
#     small=n1
# if(big%small==0):
#     print(f"lcm1: {big}")
# else:
#     found=False
#     lcm=big
#     while(found==False):
#         if(lcm % n1==0 and lcm % n2==0):
#             print(f"lcm1:{lcm}")
#             found=True
#         else:
#             lcm+=big
# '''----------------------------------'''
# # lcm other method
# n1=12
# n2=10
# lcm=n1
# lcm_not_found=True
# while(lcm_not_found==True):
#     if(lcm%n1==0 and lcm%n2==0):
#         print(f"lcm2:{lcm}")
#         lcm_not_found=False
#     else:
#         lcm+=n1
# ----------------------------------------------------
#                   gcd
# n1=5 1 5
# n2=10 1 2 5 10
n1=90  #1 2 3 6 9 18
n2=15  # 1 3 5 15
small=0
big=0
gcd=0
if(n1>n2):
    big=n1
    small=n2
else:
    big=n2
    small=n1
gcd=0
for i in range(1,small+1):
    if(n1%i==0 and n2%i==0):
        gcd=i
print(f"hcf:{gcd}")
# ----------------------------------------------------------------
#                         prime
n1
