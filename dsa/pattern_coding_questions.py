# '''
# Document: Interview-Style Pattern Printing Questions
# Topic: Star and Shape Patterns
# Language: Python
# '''

# # 1. Square Star Pattern
# '''
# Question:
# Write a Python program to print a square pattern of stars of size N.

# Input:
# N = 4

# Expected Output:
# * * * *
# * * * *
# * * * *
# * * * *
# '''
N=4
for i in range(1,N+1):
    stars="* "*N
    print(stars)
 
# # 2. Rectangle Star Pattern
n=4
for i in range(1,n+1):
    stars="* "*n
    print(stars)
# '''
# Question:
# Write a Python program to print a rectangle pattern of stars with R rows and C columns.

# Input:
# R = 3, C = 5

# Expected Output:
# * * * * *
# * * * * *
# * * * * *
# '''
R,C=3,5
# for i in range(1,R+1):
#     stars='* '*C
#     print(stars)
for i in range(1,R+1):
    stars="* "*C
    print(stars)
# # 3. Left-Aligned Right Angle Triangle
# '''
# Question:
# Write a Python program to print a left-aligned right angle triangle of stars.

# Input:
# N = 4

# Expected Output:
# *
# * *
# * * *
# * * * *
# '''
# N=4
# for i in range(1,N+1):
#     stars='* '*i
#     print(stars)
n=4
for i in range(1,n+1):
    stars="* "*i
    print(stars)
# # 4. Right-Aligned Right Angle Triangle
# '''
# Question:
# Write a Python program to print a right-aligned right angle triangle of stars.

# Input:
# N = 4

# Expected Output:
#       *
#     * *
#   * * *
# * * * *
N=4
for i in range(1,n+1):
    sp="  "*(N-i)
    stars="* "*i
    print(sp+stars)
# '''
# N=4
# for i in range(1,N+1):
#     sp='  '*(N-i)
#     stars='* '*(i)
#     print(sp+stars)
# # 5. Inverted Left-Aligned Right Angle Triangle
# '''
# Question:
# Write a Python program to print an inverted left-aligned right angle triangle of stars.

# Input:
# N = 4

# Expected Output:
# * * * *
# * * *
# * *
# *
# '''
# N=4
# for i in range(N,0,-1):
#     print("* " *i)


    
# # 6. Inverted Right-Aligned Right Angle Triangle
# '''
# Question:
# Write a Python program to print an inverted right-aligned right angle triangle of stars.

# Input:
# N = 4

# Expected Output:
# * * * *
#   * * *
#     * *
#       *
# '''
# N=4
# for i in range(N,0,-1):
#     sp=N-i
#     stars=i
#     print('  '*(sp)+'* '*(stars))
# # 7. Diamond Pattern
# '''
# Question:
# Write a Python program to print a diamond pattern of stars of height N (odd number).

# Input:
# N = 5

# Expected Output:
#            i  j  sp
#     *      1  1   4
#   * * *    2  3   2
# * * * * *  3  5   0
#   * * *    4  3   2
#     *      5  1   4

# '''
n=5
s=1
mid=(n//2)+1
for i in range(1,n+1):
    if(i<=mid):
      sp=" "*(n-i)
      stars="* "*s
      s+=2
      print(sp+stars)
    
    



# # 8. Parallelogram Pattern
# '''
# Question:
# Write a Python program to print a parallelogram star pattern of height N and width M.

# Input:
# N = 4, M = 5

# Expected Output:
#       * * * * *
#     * * * * *
#   * * * * *
# * * * * *
# '''
# N=4
# M=5
# for i in range(N,0,-1):
#     sp=' '*(2*(i-1))
#     col='* '*(M)
#     print(sp+col)

# # 9. Right Angle Triangle (Type 2)
# '''
# Question:
# Write a Python program to print a right-angle triangle of stars where each row starts with one space less.

# Input:
# N = 5

# Expected Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# '''
# rows=5
# for i in range(1,rows+1):
#     sp=rows-i
#     col=i
#     print(" "*sp +"* "*col)
# # 10. Reverse Right Angle Triangle (Type 2)
# '''
# Question:
# Write a Python program to print the reverse of the above triangle.

# Input:
# N = 5

# Expected Output:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# '''
# rows=5
# for i in range(rows,0,-1):
#     sp=rows-i
#     col=i
#     print(' '*sp+'* '*col)
# # 11. Left Pascal Triangle
# '''
# Question:
# Write a Python program to print a left Pascal triangle using stars.

# Input:
# N = 4

# Expected Output:
#              i  j  sp
#       *      1  1  3
#     * *      2  2  2
#   * * *      3  3  1
# * * * *      4  4  0
#   * * *      5  3  1
#     * *      6  2  2
#       *      7  1  3
# '''
# rows=4
# for i in range(1,2*rows):
#     if(i<=rows):
#         sp=rows-i
#         col=i
#         print('  '*sp +'* '*col)
#     else:
#         sp=i-rows
#         col=rows-sp
#         print('  '*sp+'* '*col)
        

# # 12. Right Pascal Triangle
# '''
# Question:
# Write a Python program to print a right Pascal triangle using stars.

# Input:
# N = 4

# Expected Output:
#         i    j      
# *       1    1       
# * *     2    2
# * * *   3    3
# * * * * 4    4
# * * *   5    3
# * *     6    2
# *       7    1
# '''
# rows=4
# for i in range(1,2*rows):
#     if(i<=rows):
#         stars=i
#         print('* '*stars)
#     else:
#         stars=rows-1
#         rows-=1
#         print('* '*stars)
# # 13. Sandglass Pattern
# '''
# Question:
# Write a Python program to print a sandglass star pattern.

# Input:
# N = 5

# Expected Output:
#                i  j  sp
# * * * * *      1  5   0
#  * * * *       2  4   1
#   * * *        3  3   2
#    * *         4  2   3
#     *          5  1   4
#    * *         6  2   3
#   * * *        7  3   2
#  * * * *       8  4   1
# * * * * *      9  5   0
# '''
# rows=5
# dup=rows
# for i in range(1,2*rows):
#     if(i<=rows):
#         sp=i-1
#         stars=rows-sp
#         print(' '*sp+'* '*stars)
#     else:
#         sp=2*rows-i-1
#         stars=rows-sp
#         print(' '*sp+'* '*stars)

'''                      HALLOW SHAPES'''

'''
* * * *
*     *
*     *
* * * *
'''
n=4
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "*n)
    else:
        print("* "+" "*n+"*")

'''
* * * * * * * *
*             *
*             *
* * * * * * * *
'''
n=5
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "*2*n)
    else: 
        print("* "+"  "*(2*n-2)+"*")
'''
*
* *
*  *
*    *
* * * *
'''
# n=5
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("* " *i)
#     else:
#         print("* " +"  "*(i-2)+"*")

'''
* * * * *
*     *
*   *
* *
*
'''
# n=5
# for i in range(n,0,-1):
#     if(i==n or i==1):
#         print("* " *i)
#     else:
#         print("* " +"  " *(i-2)+"*")
'''
        *
      * *
    *   *
  *     *
* * * * *
'''
n=5
for i in range(1,n+1):
    left="  "*(n-i)
    if(i==1 or i==n):
        print(left+"* "*i)
    else:
        print(left+"* "+"  "*(i-2)+"*")
'''
* * * * *
  *     *
    *   *
      * *
        *
'''
n=5
for i in range(n,0,-1):
    left="  "*(n-i)
    if(i==n or i==1):
        print(left+"* "*i)
    else:
        print(left+"* "+"  "*(i-2)+"*")
    



    