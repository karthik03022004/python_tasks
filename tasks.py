'''                           Print the position of the vowels 


word=input("enter :") #Take input
word=word.lower() # coverting all char to lowercase
for i in range(len(word)):
    if(word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u'): # check vowels
        print(f"{word[i]} is in {i} index")

'''

'''                       program to find no of consonants      '''
'''
word=input("enter:")
word=word.lower()
count_conso=0
for i in range(len(word)):
    if(word[i]!='a' and word[i]!='e' and word[i]!='i' and word[i]!='o' and word[i]!='u' and word[i]!=' '):
        count_conso+=1
print(f"{count_conso} consonants")
'''

#                take a function and str,num as parameters return characters that are the multiples of num
'''
def char_multiples(s,num):
    for i in range(len(s)):
        if(i%num==0 and s[i]!=' '):
            print(s[i],i)
s=input("enter string:")
num=int(input("num:"))
s=s.lower().strip()

char_multiples(s,num)

#                         count no of words using method

def count_word(sentence):
    cnt=sentence.count(' ')
    print(cnt+1)
sentence=input()
count_word(sentence)
'''
#                         counting words without method
'''
def count_words(sentence):
    cnt=0
    for i in range(len(sentence)):
        c=sentence[i]
        if(c==' '):
            cnt+=1
    print(f"the number of words is:{cnt+1}")
sentence=input()
#count_words(sentence)


def task(word):
    word=word.find('p')
    return word
word="i am learning python"
print(task(word))
'''
'''                               methods in string :
var_name.upper()
var_name.lower()
var_name.capitalize()
var_name.title()
var_name.strip()
var_name.lstrip()
var_name.rstrip()
var_name.replace(oldstr,newstr)
var_name.find()
var_name.count()
'''

#                                     count uppercase and lowercases
'''
def count_up_lo(s):
    count_up=0
    count_lo=0
    for i in range(len(s)):
        if(s[i]==s[i].upper() and s[i]!=' '):
            count_up+=1
        elif(s[i]==s[i].lower() and s[i]!=' '):
            count_lo+=1
    return count_up,count_lo
    # print(f"no of lower-cases:{count_lo},no of upper-cases:{count_up}")
s=input()
print(count_up_lo(s))
'''

#1QCreate a string with your name and print it.

name="Siva charan karthik Kammampati"
print("My Name Is:",name)

#2Q)Get the first character from the string.
print("First character:",name[0])

#3Q)Get the last character from the string.
last=len(name)-1 #len-1 gives final index of string
print("Last Character",name[last])

#4Q)Concatenate two strings.
new_string="from nellore"
print(name+" "+new_string)

#5Q)      Repeat a string 3 times.
#print(name*3,end="\n")
for i in range(1,4):
    print(name)

#6Q) Slice the first 5 characters.

print(name[0:5]) # stop before 5 0,1,2,3


#7Q) Reverse a string using slicing.
print(name[::-1])

#8Q)Check if a substring exists in a string.
sub_string="charan"  
if sub_string in name:
    print("it exist")
else:
    print("not exist")



#9Q)Find the length of a string.
print("length of string:",len(name))

#10Q) Convert string to uppercase.
print("ALL UPPERCASE:",name.upper())

#11Q)  Convert string to lowercase.
print("all lower-case:",name.lower())

#12Q)  Capitalize the first letter.
print("Captilize:",name.capitalize())


#13Q) Convert a string to title case.
print("title-case:",name.title())

#14Q) Remove leading spaces using lstrip().
word="           sample word"
print("string after using lstrip:",word.lstrip())

#15Q)Remove trailing spaces using rstrip().

word_new="sample string                                                      "

print("string without trailing spaces is:",word_new.rstrip())
