# substring
s="sivacharankarthik"
sub="karthi"
possible=False
for i in range(len(s)):
    if(s[i:i+len(sub)]==sub):
        possible=True
        print(f"{i} and {i+len(sub)}")
        break
    else:
        pass
print("substring") if possible else print("no substring")
'''-------------------------------------------------------------------'''
# longest word in a sentence
sen="my name is siva charan karthik living in hyderabad"
words=sen.split(" ")
longest=""
for i in words:
    if(len(i)>len(longest)):
        longest=i
print(f"longest word: {longest}")
'''-------------------------------------------------------------------'''
#anagram
s1="live"
s2="evil"
isana=True
if(len(s1)!=len(s2)):
    isana=False
else:
    for i in s1:
        if(s1.count(i)!=s2.count(i)):
            isana=False
            break
        else:
            isana=True
print("anagram") if isana else print("not anagram")

cnt=0
for i in s2:
    if(s1.count(i)==s2.count(i)):
        cnt+=1
print(cnt) 
print("yes ana")if(cnt==len(s1)) else print("no ana")
'''---------------------------------------------------------------------------'''
# longest palindromic substring
s="malayalam"
longest=""
cnt=0
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        temp+=s[j]
        if(temp==temp[::-1] and len(temp)>=2):
            cnt+=1
            print(temp)
        if(temp==temp[::-1] and len(longest)<len(temp)):
            longest=temp
print(f"cnt of palindromes:{cnt}")
print(longest)
'''--------------------------------------------------------------------------'''
# shortest palindromic substring
s="malayalam"
shortest=s
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        temp+=s[j]
        if(temp==temp[::-1] and len(temp)>=2 and len(shortest)>len(temp)):
            shortest=temp
print(shortest)
'''-----------------------------------------------------------------------------------'''
# unique palindromes
s="malayalam"
list=[]
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        temp+=s[j]
        if(temp==temp[::-1] and len(temp)>=2):
            if temp not in list:
                list.append(temp)
print(" ".join(list))
'''----------------------------------------------------------------------------------'''
s1="13579"
s2="2468"
# output="123456789"
if(len(s1)>len(s2)):
    itr=s1
else:
    itr=s2
res=""
for i in range(len(itr)):
    if(i<len(s1) and i<len(s2)):
        res+=s1[i]+s2[i]
    else:
        res+=itr[i]
print(res)
'''----------------------------------------------------------------'''
# palindrome
s="siva charan"
vowel=""
for i in s:
    if i in 'aeiou':
        vowel+=i
print(vowel)
'''------------------------------------------------------------------------'''
s="aabb999" #output:aaaaa i want longest reapting string and cnt of char
longest=""
i=0
while(i<len(s)):
    cnt=1
    temp=s[i]
    for j in range(i,len(s)-1):
        if(s[j]==s[j+1]):
            temp+=s[j]
            cnt+=1
            # if(len(longest)<cnt):
            #     longest=temp
        else:
            break
    print(temp,cnt)
    i+=cnt
# print(longest,cnt)
'''-------------------------------------------------------------------------------------------'''
s="abcdefabcdefghi" #out: abcdefghi i want longest non repaeating substring
longest=""
for i in range(len(s)):
    temp=""
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp+=s[j]
            if(len(longest)<len(temp)):
                longest=temp
            else:
                break
print(longest)




