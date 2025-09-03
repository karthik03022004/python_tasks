# . Input: "he llo wor ld" Output: "helloworld"
s="hell o wo rld"
new=""
for i in s:
    if i!=" ":
        new+=i
print(new)
# -----------------------------
# Input: "hello" Output: "olleh"
s="hello"
new=""
for i in s[::-1]:
    new+=i
print(new)
# ---------------------------
# Input: "he llo world" Output: "dlrowolleh"
s="he llo world"
new=""
for i in s[::-1]:
    if(i!=" "):
        new+=i
print(new)
# --------------------------
# . Input: "my_variable_name" Output: "myVariableName"
s="my_variable_name"
new=""
for i in range(len(s)):
    if(s[i-1]=="_"):
        new+=s[i].upper()
    elif(s[i]!="_"):
        new+=s[i]
print(new)
# --------------------------
# Input: "my_variable_name" Output: "MyVariableName"
s="my_variable_name"
new=s[0].upper()
for i in range(1,len(s)):
    if(s[i-1]=="_"):
        new+=s[i].upper()
    elif(s[i]!="_"):
        new+=s[i]
print(new)
# ---------------------------
# Input: "myVariableName" Output: "my_variable_name"
s="myVariableName"
new=s[0]
for i in range(1,len(s)):
    if(s[i].isupper()):
        new+="_"+s[i].lower()
    elif(s[i].islower()):
        new+=s[i]
print(new)
# -------------------------------------
# 7) Input: "myVariable" Output: "MyVariable"
s="myVariable"
new=s[0].upper()
for i in range(1,len(s)):
    new+=s[i]
print(new)
# ---------------------------
# 8. Convert Pascal Case to Camel Case
# Problem: Convert a string from PascalCase to camelCase. Input: "MyVariable" Output: "myVariable"
s="MyVariable"
new=s[0].lower()
for i in range(1,len(s)):
    new+=s[i]
print(new)
# -----------------------
'''
9. Convert Pascal Case to Snake Case
Problem: Convert a string from PascalCase to snake_case. Input: "MyVariable" Output: "my_variable"
'''
s="MyVariable"
new=s[0].lower()
for i in range(1,len(s)):
    if(s[i].isupper()):
        new+="_"+s[i].lower()
    elif(s[i].lower()):
        new+=s[i]
print(new)
# -------------------------------
# 10. Convert Text to Camel Case
# . Input: "hello world example" Output: "helloWorldExample"
s="hello world example"
new=""
for i in range(len(s)):
    if(s[i-1]==" "):
        new+=s[i].upper()
    elif(s[i]!=" "):
        new+=s[i]
print(new)
# ------------------------------------
'''
11. Convert Text to Snake Case
Problem: Convert a space-separated sentence into snake_case. Input: "hello world example" Output: "hello_world_example"
'''
s="hello world example"
new=""
for i in range(len(s)):
    if(s[i-1]==" "):
        new+="_"+s[i]
    elif(s[i]!=" "):
        new+=s[i]
print(new)
# ------------------------------
# 12. Convert Text to Pascal Case
# Problem: Convert a space-separated sentence into PascalCase. Input: "hello world example" Output: "HelloWorldExample"
s="hello world example"
new=s[0].upper()
for i in range(1,len(s)):
    if(s[i-1]==" "):
        new+=s[i].upper()
    elif(s[i]!=" "):
        new+=s[i]
print(new)
# --------------------------------
'''
13. Swap Upper and Lower Case
Problem: Swap the case of each letter in a given string. Input: "HeLLo" Output: "hEllO"
'''
s="HeLLo"
new=""
for i in s:
    if(65<=ord(i)<=90):
        new+=i.lower()
    elif(97<=ord(i)<=122):
        new+=i.upper()
print(new)
# --------------------------------
'''
14. Separate Digits from Text
Problem: Extract all digits from a given alphanumeric string. Input: "abc123d4" Output: "1234"
'''
s="abc1234"
new=""
for i in s:
    if i in "1234567890":
        new+=i
print(new)
# -----------------------------------
'''
15. Print Uppercase, Lowercase, Digits, and Special Characters Separately
Problem: Print each type of character separately from the string. Input: "Abc123!@#" Output:
Uppercase: A
Lowercase: b c
Digits: 1 2 3
Special Characters: ! @ #
'''
s="Abc123!@#"
upper=""
lower=""
dig=""
special=""
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        upper+=i+" "
    elif(ord(i)>=97 and ord(i)<=122):
        lower+=i+" "
    elif(ord(i)>=47 and ord(i)<=58):
        dig+=i+" "
    else:
        special+=i+" "
print("uppercase: ",upper)
print("lowecase: ",lower)
print("digits:",dig)
print("special:",special)
# ------------------------------------
'''
16. Count of Uppercase, Lowercase, Digits, and Special Characters
Problem: Count each type of character in a string. Input: "AbC@123x!" Output:
Uppercase: 2
Lowercase: 1
Digits: 3
Special Characters: 2
'''
s="AbC@123x!"
Uppercase=0
Lowercase=0
Digits=0
Special_Characters=0
for i in s:
    if(65<=ord(i)<=90):
        Uppercase+=1
    elif(i.islower()):
        Lowercase+=1
    elif(i.isdigit()):
        Digits+=1
    else:
        Special_Characters+=1
print("uppercase:",Uppercase)
print("Lowercase:",Lowercase)
print("Digits:",Digits)
print("special char:",Special_Characters)
# ---------------------
'''
17. Check Password Strength
Problem: Check if a password contains at least one uppercase, one lowercase, one digit, and one special character. Input: "Pass123!" Output: "Strong Password"
'''
s="Pass123!"
upflag=0
lowflag=0
numflag=0
spflag=0
for i in s:
    if(i.isupper()):
        upflag=1
    elif(i.islower()):
        lowflag=1
    elif(i.isdigit()):
        numflag=1

    else:
        spflag=1
    
if(upflag==1 and lowflag==1 and numflag==1 and spflag==1):
    print("strong")
else:
    print("weak")
# --------------------------------------------------
# 18. Remove Duplicates in a Given Input
# Problem: Remove duplicate characters from a string. Input: "aabbcc" Output: "abc"
s="aabbccgggggggggggggggg"
no_dup=""
for i in s:
    if(i not in no_dup):
        no_dup+=i
print(no_dup)
# temp=""
# i=0
# while(i<len(s)):
#     if(s[i] not in temp):
#         temp+=s[i]
#     i+=1
# print(temp)
# ---------------------
'''
19. Print Duplicates in a Given String
Problem: Identify and print duplicate characters in a string. Input: "aabbccde" Output: a b c
'''
s="aabbccde"
dup=""
for i in s:
    if(s.count(i)>=2 and i not in dup):
        dup+=i+" "
print(dup)
# i=0
# temp=""
# while(i<len(s)):
  
#     for j in range(i+1,len(s)):
#         if(s[j]==s[i] and s[i] not in temp):
#             temp+=s[i]
#             break
            
#     i+=1
# print(temp)
# ------------------
s="xyz" #output: yza
s="abc"
res=""
for i in s:
    if(ord(i)>=122):
        res+=chr(ord(i)-25)
    else:
        res+=chr(ord(i)+1)
print(res)
