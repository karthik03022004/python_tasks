'''                longest word in astring           '''
# i love python language     output: language
'''
def longest_word(s):
    s=s.split(" ")
    longest=""
    for i in range(len(s)):
        if(len(longest)<len(s[i])):
            longest=s[i]
    print("lonest word:",longest)
s=input()
longest_word(s)'''


'''               alternate strings combine in a string'''
# s1="13579" 0,1,2,3,4
# s2="2468"  0,1,2,3
'''
s1=input()
s2=input()
itr=""
if(len(s1)<len(s2)):
    itr=s2
else:
    itr=s1
new=""
for i in range(len(itr)):
    if(i<len(s1) and i<len(s2)):
        new+=s1[i]+s2[i] #0,1,2,3
    else:
        new+=itr[i]
print(new)'''


# * * * * * 
# *
# * * * * *
#         *
# * * * * * 




