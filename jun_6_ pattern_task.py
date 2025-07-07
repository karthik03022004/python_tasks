# * * * * *
#         *
# * * * * *
# *
# * * * * *
'''
rows=int(input())
mid=(rows//2)+1
for i in range(1,rows+1):
    pat=""
    for j in range(1,rows+1):
        if(i<=mid):
            if(i==1 or j==rows or i==mid):
                pat+="*"+" "
            else:
                pat+=" "+" "

        else:
            if(j==1 or i==rows):
                pat+="*"+" "
            else:
                pat+=" "+" "
    print(pat)
'''


    
#  * * * * * 
#          *
#  * * * * *
#          *
#  * * * * *
rows=int(input())
mid=(rows//2)+1
for i in range(1,rows+1):
    pat=""
    for j in range(1,rows+1):
        if(i==1 or i==mid or i==rows or  j==rows):
            pat+="*"+" "
        else:
            pat+=" "+" "
    print(pat)

    
