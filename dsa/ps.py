'''
* * * * *
*   *
* * * * *
    *   *
* * * * *        
'''
rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    pat=""
    for j in range(1,rows+1):
        if(i<=mid):
            if(i==1 or j==1 or i==mid or j==mid):
                pat+="*"+" "
            else:
                pat+=" "+" "

        else:
            
            if(j==rows or i==rows or j==mid):
                pat+="*"+" "
            else:
                pat+=" "+" "
    print(pat)