# word="malayali"           longest palindromic substrin in a worrd
# longest=""
# for i in range(len(word)):
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]
#         if(temp==temp[::-1] and len(temp)>len(longest)):
#             longest=temp
            
# print(longest)

word="ABCDAAA" #shortest palin substrings
short=word
for i in range(len(word)):
    temp=""
    for j in range(i,len(word)):
        temp+=word[j]
        if(temp==temp[::-1] and len(short)>len(temp) and len(temp)>=2):
            short=temp
print("no palin substrings") if short==word else print(short)