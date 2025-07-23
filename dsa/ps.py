n = 3
for i in range(1,n+1):
    for j in range(1,n+1):
        if i ==1 or j ==1 or j == 2 or i == n:
            print("* ",end='')
        else:
            print(' ',end='')
    print()
n = 2
for i in range(1,n+1):
    for j in range(1,n+1):
        if   j == 2 or i == n:
            print("* ",end='')
        else:
            print(' ',end='')
    print()