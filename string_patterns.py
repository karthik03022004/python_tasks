# #     *        1 i  1 j  4 space
# #    * *       2   2   3
# #   * * *      3   3   2
# #  * * * *     4   4   1
# # * * * * *    5   5   0
# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for space in range(1,rows-i+1):
#         pattern+=" "
#     for j in range(1,i+1):
#         pattern+="*"+" "
#     print(pattern)
'''------optimized code-----'''
rows=5
for i in range(1,rows+1):
    space=rows-i
    col=i
    print(" "*space + ("*"+" ")* col)
# # * * * * *     1   5    0
# #  * * * *      2   4    1
# #   * * *       3   3    2
# #    * *        4   2    3
# #     *         5   1    4

# for i in range(rows,0,-1):
#     pattern=""
#     for space in range(1, rows-i+1):
#         pattern+=" "
#     for j in range(1,i+1):
#         pattern+="*"+" "
#     print(pattern)
for i in range(rows,0,-1):
    space=rows-i 
    col=i
    print(" "*space + ("*"+" ")*col)

# homework task

            #  i  j  sp
# * * * * *    1  5  0
#  * * * *     2  4  1
#   * * *      3  3  2
#    * *       4  2  3
#     *        5  1  4
#    * *       6  2  3
#   * * *      7  3  2
#  * * * *     8  4  1
# * * * * *    9  5  0
rows=5
for i in range(rows,1,-1):
    pattern=" "
    for space in range(1,rows-i+1):
        pattern+=" "
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)


for i in range(1,rows+1):
    pattern=" "
    for space in range(1,rows-i+1):
        pattern+=" "
    for j in range(1,i+1):
        pattern+="*"+" "
    print(pattern)
print("\n")
# optimized code
rows=5
for i in range(1,2*rows):
    space=(i-1) if i<=rows else 2*rows-i-1
    col=rows-space
    print(" "*space +("*"+" ")*col)

# jun14 task 
rows=9 #Y shape
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if(i<=mid):
            if(i==j or i+j==rows+1):
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if(j==mid):
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)
print()         
rows=7 #y shape
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if(i<=mid):
            if(i==j or i+j==rows+1):
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if(i+j==rows+1):
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)
    
print()
rows=5 #M shape
mid=(rows//2)+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if(i<=mid):
            if(j==1 or j==rows or i==j or i+j==rows+1):
                res+="*"+" "
            else:
                res+=" "+" "
        else:
            if(j==1 or j==rows):
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)


    