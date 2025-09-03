'''
* * * *
* * * *
* * * *
* * * *
'''
# rows=4
# for i in range(1,rows+1):
#     pat=""
#     for j in range(1,rows+1):
#         pat+="*"+" "
#     print(pat)
'''
rows=4
for i in range(1,rows+1):
    col="* "* rows
    print(col)
    '''
'''--------------'''
# rectangle
# n=4
# i=1
# while(i<=n):
#     print(("*"+" ")*(2*n))
#     i+=1
'''----------------------------'''
'''
*
* *
* * *
* * * *
'''
# n=8
# i=1
# while(i<=n):
#     print("* " *i)
#     i+=1
# ------------------------------------
# rows=5
# for i in range(1,rows+1):
#     print("* "*i)
# -----------------------------------------
'''        i  j  sp
    *      1  1  4
   * *     2  2  3
  * * *    3  3  2
 * * * *   4  4  1
* * * * *  5  5  0
'''
# i=1
# while(i<=rows):
#     space=" "*(rows-i)
#     col="* "*i
#     print(space+col)
#     i+=1
# -------------------------
# rows=5
# for i in range(1,rows+1):
#     sp=" "*(rows-i)
#     stars="* "*i
#     print(sp+stars)
# # -------------------------------
# for i in range(1,rows+1):
#     pat=""
#     for sp in range(1,(rows-i)+1):
#         pat+=" "
#     for col in range(1,i+1):
#         pat+="*"+" "
#     print(pat)
'''-----------------------------------------'''
'''        i  j  sp
* * * *    1  4  0
 * * *     2  3  1
  * *      3  2  2
   *       4  1  3
'''
# rows=4
# i=0
# j=rows
# while(i<rows):
#     sp=" "*i
#     stars="* "*j
#     print(sp+stars)
#     i+=1
#     j-=1
# # -----------------------------------
# rows=5
# for i in range(rows,0,-1):
#     sp=" "*(rows-i)
#     stars="* "*i
#     print(sp+stars)

'''-----------------------------------------'''
'''         i    j     sp
    *       1    1     4
   * *      2    2     3
  * * *     3    3     2
 * * * *    4    4     1
* * * * *   5    5     0
 * * * *    6    4     1
  * * *     7    3     2
   * *      8    2     3
    *       9    1     4
'''
# rows=5
# i=1
# while(i<=rows):
#     sp=' '*(rows-i)
#     stars='* '*(i)
#     print(sp+stars)
#     i+=1
# i=rows-1
# while(i>=1):
#     sp=' '*(rows-i)
#     stars='* '*i
#     print(sp+stars)
#     i-=1
# rows=5
# for i in range(1,2*rows):
#     if(i<=rows):
#         sp=' '*(rows-i)
#         stars='* '*(i)
#         print(sp+stars)
#     else:
#         sp=' '*(i-rows)
#         stars='* '*(2*rows-i)
#         print(sp+stars)
'''---------------------------------------------------'''
# PS-2
# 1)
'''
Output:
* * * *
* * * *
* * * *
* * * *
'''
n=4
for i in range(1,n+1):
    print("* " *n)
'''2
Input: m = 3, n = 5
Output:
* * * * *
* * * * *
* * * * *
'''
m=3
n=5
for i in range(1,m+1):
    print("* "*n)
'''3
*
* *
* * *
* * * *
* * * * *
'''
for i in range(1,n+1):
    print("* " *i)
# for i in range(1,n+1):
#     pat=""
#     for j in range(1,i+1):
#         pat+="* "
#     print(pat)
'''4
        *
      * *
    * * *
  * * * *
* * * * *
'''
for i in range(1,n+1):
    sp="  "*(n-i)
    stars="* "*(i)
    print(sp+stars)
'''5
Output:
* * * * *
* * * *
* * *
* *
*
'''
print("----------")
for i in range(n,0,-1):
    stars="* "*i
    print(stars)
'''6
* * * * *
  * * * *
    * * *
      * *
        *
'''
print("----------")
for i in range(n,0,-1):
    sp="  "*(n-i)
    stars="* "*i
    print(sp+stars)
'''7
      *
    * * *
  * * * * *
* * * * * * *
'''
print("-------------")
n=4
num=1
for i in range(1,n+1):
    sp='  '*(n-i)
    stars="* "*(num)
    num+=2
    print(sp+stars)
'''
Output:
    *
  * * *
* * * * *
  * * *
    *
'''
n=3
num=1
for i in range(1,n+1):
    sp='  '*(n-i)
    stars='* '*(num)
    num+=2
    print(sp+stars)
num=1
for i in range(n,0,-2):
    sp='  '*num
    num+=1
    stars="* "*i
    print(sp+stars)

