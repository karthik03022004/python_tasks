# # '''
# # * * * * *
# # *   *
# # * * * * *
# #     *   *
# # * * * * *        
# # '''
# # rows=5
# # mid=(rows//2)+1
# # for i in range(1,rows+1):
# #     pat=""
# #     for j in range(1,rows+1):
# #         if(i<=mid):
# #             if(i==1 or j==1 or i==mid or j==mid):
# #                 pat+="*"+" "
# #             else:
# #                 pat+=" "+" "

# #         else:
            
# #             if(j==rows or i==rows or j==mid):
# #                 pat+="*"+" "
# #             else:
# #                 pat+=" "+" "
# #     print(pat)


# # Interview-Style Programming Questions: Basic Math and Logic
# # ___                        problemsoving1_____________________________________
# #  1. Area of Square
# # Question: Calculate the area of a square. - Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25
# def area(side):
#     return side*side
# side=5
# print(area(side))
# # ________________________________________
# # 2. Area of Rectangle
# # Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24
# def area_rect(l,b):
#     return l*b
# print(area_rect(6,4))
# # ________________________________________
# # 3. Area of Triangle
# # Question: Calculate the area of a triangle using base and height. - Formula: Area = (1/2) × base × height - Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0
# def triangle(b,h):
#     return (0.5)*b*h
# print(triangle(8,5))
# # ________________________________________
# # 4. Perimeter of Square
# # Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - Side = 6 - Output: - Perimeter of square is: 24
# def peri_square(side):
#     return (4*side)
# print(f"perimeter square:{peri_square(6)}")
# # ________________________________________
# # 5. Perimeter of Rectangle
# # Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) - Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16
# def peri_rect(l,b):
#     return 2*(l+b)
# print(peri_rect(5,3))
# # ________________________________________
# # 6. Perimeter of Triangle
# # Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18
# def p_tri(s1,s2,s3):
#     return s1+s2+s3
# print("perimeter of tri:",p_tri(5,6,7))
# # ________________________________________
# # 7. Break Amount into 1000s, 500s, and Remaining Change
# # Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200
# def change(amount):
#     s1000=amount//1000
#     amount=amount%1000
#     s500=amount//500
#     amount=amount%500
#     return s1000,s500,amount
# print(change(3700))


# # ________________________________________
# # 8. Convert Seconds into Hours, Minutes, and Seconds
# # Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
# def convert(sec):
#     hrs=sec//3600
#     sec=sec%3600
#     min=sec//60
#     sec=sec%60
#     return hrs,min,sec
# print(convert(3672))

# # ________________________________________
# # 9. Sum of Marks (Maths, Physics, Chemistry)
# # Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263
# def sum_marks(m,p,c):
#     return m+p+c
# print(sum_marks(85,90,88))
# # ________________________________________
# # 10. Average of Marks (Maths, Physics, Chemistry)
# # Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67
# def average(m,p,c):
#     return (m+p+c)/3
# print("average:",average(85,90,88))

# # n=21
# # res=0
# # res+=n
# # while(n!=0):
# #     n//=3
# #     res+=n
# #     rem=n%3
# #     res+=rem
# # print(res)

# n=6
# tot=n
# w=n
# while(w>=3):
#     e=w//3
#     tot+=e
#     w=e+(e%3)
# print(tot)
# # -------------------------------------------------------------------------------------------------------------------
# #                                problemsolving 5
# # . Print All Prime Numbers from m to n
# # Problem: Given a range from m to n, print all prime numbers in that range.
# # Input: m = 10, n = 30
# # Output: 11 13 17 19 23 29

# m=10
# n=30
# for i in range(m,n+1):
#     factors=0
#     for j in range(2,i):
#         if(i%j==0):
#             factors+=1
#             break
#     if(factors==0):
#         print(i)
# '''--------------------------------------------------'''
# m=1
# n=10
# cnt_prime=0
# for i in range(m,n+1):
#     factors=0
#     for j in range(2,(i//2)+1):
#         if(i%j==0):
#             factors+=1
#             break
#     if(factors==0):
#         if(i!=1):
#          cnt_prime+=1
# print(f"cnt:{cnt_prime}")
# '''-------------------------------------------------------'''

# def armstrong(m,n):
#     for i in range(m,n+1):
#         num=i
#         s=str(num)
#         digits=len(s)
#         sum=0
#         while(num!=0):
#             d=num%10
#             sum+=d**digits
#             num=num//10
#         if(sum==i):
#             print(sum)
# armstrong(1,500)
# '''--------------------------------------------------------------'''
# def next_prime(m,n):
#     for i in range(m+1,n+1):
#         factors=0
#         for j in range(2,i):
#             if(i%j==0):
#                 factors+=1
#                 break
#         if(factors==0):
#             print("first prime in range:",i)
#             break
# next_prime(10,25)
# '''------------------------------------------------------------'''
# def last_prime(m,n):
#     for i in range(n-1,m+1,-1):
#         factors=0
#         for j in range(2,(i//2)+1):
#             if(i%j==0):
#                 factors+=1
#                 break
#         if(factors==0):
#             print('last prime in range',i)
#             break
# last_prime(10,50)
# '''------------------------------------------------------------------'''
# def first_vowel(s):
#     for i in s:
#         if(i in 'aeiou'):
#             print(i)
#             break
# first_vowel("krishna")
# '''---------------------------------------------------------------------'''
# def last_vowel(s):
#    for i in s[::-1]:
#        if(i in "aeiou"):
#            print(i)
#            break
# last_vowel("krishna")
# '''----------------------------------------------------------------------'''
# def even(n):
#     for i in range(1,n+1):
#         if(i%2!=0):
#             continue
#         else:
#             print(i)
# even(10)
# '''--------------------------------------------------------------------------'''


# def odd(n):
#     for i in range(1,n+1):
#         if(i%2==0):
#             continue
#         print(i)
# odd(10)
# '''----------------------------------------------------------------------'''

# prime=0
# comp=0
# m=1
# n=10
# for i in range(m,n):
#     factors=0
#     for j in range(2,i):
#         if(i%j==0):
#             factors+=1
#             break
#     if(factors==0):
#         if(i!=1):
#             prime+=1
#     else:
#         comp+=1
# print(prime,comp)
# '''-------------------------------------------------------------------------'''

#                        problemsolving 4
 # 1. Square Star Pattern
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
# N=4
# for i in range(1,N+1):
#     stars="* "*N
#     print(stars)
# -------------------------------------------
# # 2. Rectangle Star Pattern
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
# R,C=3,5
# for i in range(1,R+1):
#     stars='* '*C
#     print(stars)
# -----------------------------------------
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
# -----------------------------------------------
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
# '''
# N=4
# for i in range(1,N+1):
#     sp='  '*(N-i)
#     stars='* '*(i)
#     print(sp+stars)
# ----------------------------
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
# --------------------------------
# 6 Expected Output:
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
# ------------------------------
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
# -------------------------------------
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
# -------------------------------
# 10. Reverse Right Angle Triangle (Type 2)
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
# -----------------------------------
# 11. Left Pascal Triangle
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
# -------------------------------------
# 12. Right Pascal Triangle
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
# --------------------------------------------
# 13. Sandglass Pattern
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
# -----------------------------------------
''' 16
* * * *
*     *
*     *
* * * *
'''
# n=4
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("* "*n)
#     else:
#         print("* "+" "*n+"*")
# ---------------------------------
''' 17
* * * * * * * *
*             *
*             *
* * * * * * * *
'''
# n=5
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("* "*2*n)
#     else: 
#         print("* "+"  "*(2*n-2)+"*")

# rows=5
# for i in range(1,rows+1):
#     row=""
#     for j in range(1,i+1):
#         row+=str(j)+' '
#     print(row)     26
# ------------------------------------

# rows=5
# for i in range(1,rows+1):
#     row=" "
#     for j in range(1,i+1):
#         row+=str(i)+" "
#     print(row)   27
# -------------------------------------
# rows=4
# num=1
# for i in range(1,rows+1):
#     row=""
#     for j in range(1,i+1):
#         row+=str(num)+' '
#         num+=1
#     print(row)      28
# ------------------------------------------
# rows=5
# for i in range(1,rows+1):
#     row=""
#     for j in range(i,0,-1):
#         row+=str(j)+" "
#     print(row)               29
# -------------------------------------------
# rows=5
# for i in range(rows,0,-1):
#     row=""
#     for j in range(i,0,-1):
#         row+=str(j)+" "
#     print(row)                 30
# ---------------------------------------------
# rows=5
# for i in range(1,rows+1):
#     sp='  '*(rows-i)
#     row=""
#     for j in range(1,i+1):
#         row+=str(j)+' '
#     print(sp+row)             31
# --------------------------------------------------
# rows=5
# for i in range(1,rows+1):
#     row=""
#     for j in range(1,i+1):
#         j1=2*j
#         row+=str(j1)+' '
#     print(row)                      33
# --------------------------------------------------
# rows=5
# for i in range(1,rows+1):
#     row=""
#     for j in range(1,i+1):
#         j1=2*j-1
#         row+=str(j1)+" "
#     print(row)                             34
# -----------------------------------------------------




#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

n=4
for i in range(1,n+1):
    sp='  '*(n-i)
    num=""
    for j in range(1,i+1):
        num+=str(j)+" "
    
    for j in range(i-1,0,-1):
        num+=str(j)+' '
    print(sp+num)
    


    
