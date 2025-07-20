'''
* * * *
* * * *
* * * *

'''
rows=5
code=65
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        pattern+=chr(code)+" "
        code+=1
    print(pattern)
'''
*
* *
* * *
'''
rows=5
# code=97
num=1
for i in range(1,rows+1):
    pat=""
    for j in range(1,i+1):
        pat+=str(rows)+" "
        num+=1
    rows-=1
        # code+=1
    print(pat)

'''
* * *
* *
*
'''

rows=5
code=97
for i in range(rows,0,-1):
    pat=""
    for j in range(1,i+1):
        pat+=str(j)+" "
        code+=1
    print(pat)

'''
* * *
*   *
* * *
'''
rows=5
for i in range(1,rows+1):
    pat=""
    for j in range(1,rows+1):
        if(j==1 or i==1 or j==rows or i==rows):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)
'''
* * *
*
* * *
'''
rows=5
for i in range(1,rows+1):
    pat=""
    for j in range(1,rows+1):
        if(j==1 or i==1 or i==rows):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)
'''
* * * * *
*
* * * * *
*
* * * * *
'''
rows=5
mid=(rows//2)+1
for i in range(1,rows+1): #E
    pat=""
    for j in range(1,rows+1):
        if(i==1 or i==rows or j==1 or i==mid):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)
rows=5
for i in range(1,rows+1): #F
    pat=""
    for j in range(1,rows+1):
        if(i==1 or j==1 or i==mid):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)
for i in range(1,rows+1):#H
    pat=""
    for j in range(1,rows+1):
        if(j==1 or j==rows or i==mid):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)

for i in range(1,rows+1): #I
    pat=""
    for j in range(1,rows+1):
        if(i==1 or i==rows or j==mid):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)
for i in range(1,rows+1): #M
    pat=""
    for j in range(1,rows+1):
        if(i<=mid):
            if(j==1 or i==j or i+j==rows+1 or j==rows):
                pat+="*"+" "
            else:
                pat+=" "+" "
        else:
            if(j==1 or j==rows):
                pat+="*"+" "
            else:
                pat+=" "+" "
    print(pat)
for i in range(1,rows+1): #N
    pat=""
    for j in range(1,rows+1):
        if(j==1 or i==j or j==rows):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)
for i in range(1,rows+1): #X
    pat=""
    for j in range(1,rows+1):
        if(i==j or i+j==rows+1):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)

for i in range(1,rows+1):# Z
    p=""
    for j in range(1,rows+1):
        if(i+j==rows+1 or i==1 or i==rows):
            p+="*"+" "
        else:
            p+=" "+" "
    print(p)
            
for i in range(1,rows+1): #T
    p=""
    for j in range(1,rows+1):
        if(i==1 or j==mid):
            p+="*"+" "
        else:
            p+=" "+" "
    print(p)
for i in range(1,rows+1): #J
    pat=""
    for j in range(1,rows+1):
        if(j<=mid):
            if(i==1 or j==mid or i==rows):
                pat+="*"+" "
            else:
                pat+=" "+" "
        else:
            if(i==1):
                pat+="*"+" "
            else:
                pat+=" "+" "
    print(pat)
'''----------------------------------------------------------------'''

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
'''-----------------------------------------------------'''
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
# rows=5
# for i in range(1,rows+1):
#     pat=""
#     for sp in range(1,rows-i+1):
#         pat+=" "+" "
#     for j in range(1,i+1):
#         pat+="*"+" "
#     print(pat)
    
'''optimized'''
for i in range(1,rows+1):
    space=rows-i
    col=i
    print((" "+" ")*space +("*" +" ")*col)
print("\n")
'''--------------------------------------------------------------------'''
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
'''---------------------------------------------------------'''

'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
# for i in range(rows,0,-1):
#     res=""
#     for sp in range(1,rows-i+1):
#         res+=" " +" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)
for i in range(rows,0,-1):
    sp=rows-i
    col=i
    print((" " +" ")*sp +("*"+" ")* col)
'''--------------------------------------------------------------------------'''
'''        i   j  sp
    *      1   1  4
   * *     2   2  3
  * * *    3   3  2
 * * * *   4   4  1
* * * * *  5   5  0
 * * * *   6   4  1
  * * *    7   3  2
   * *     8   2  3
    *      9   1  4
'''
# for i in range(1,rows*2):
#     pat=""
#     if(i<=rows):
#         for sp in range(1,rows-i+1):
#             pat+=" "
#         for j in range(1,i+1):
#             pat+="*"+" "
#     else:
#         for sp in range(1,i-rows+1):
#             pat+=" "
#         for j in range(1,(2*rows-i)+1):
#             pat+="*"+" "
#     print(pat)
# optimized
for i in range(1,(2*rows)):
    if(i<=rows):
        sp=rows-i
        col=i
        print(" "* sp +("*"+" ")*col)
    else:
        sp=i-rows
        col=(2*rows)-i
        print(" "*sp +("*" +""))

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
code=97
for i in range(rows,1,-1):
    pattern=" "
    for space in range(1,rows-i+1):
        pattern+=" "
    for j in range(1,i+1):
        pattern+=chr(code)+" "
        code+=1
    print(pattern)


for i in range(1,rows+1):
    pattern=" "
    for space in range(1,rows-i+1):
        pattern+=" "
    for j in range(1,i+1):
        pattern+=chr(code)+" "
        code+=1
    print(pattern)
print("\n")
# optimized code
rows=5
for i in range(1,2*rows):
    space=(i-1) if i<=rows else 2*rows-i-1
    col=rows-space
    print(" "*space +("*"+" ")*col)

    
'''---------------------------------------------------------------'''
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


    