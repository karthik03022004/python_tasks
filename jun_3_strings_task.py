'''            Check whether the char is lower,upper,number using function

def check_char(char_acter):
    code=ord(char_acter)
    if(code>=97 and code<=122):
        print("lowercase:",chr(code))
    elif(code>=65 and code<=90):
        print("uppercase:",chr(code))
    elif(code>=48 and code<=57):
        print("number:",chr(code))
    else:
        print("It's an other character")
char_acter=input("enter charcter:")
check_char(char_acter)'''

'''                      (hello-hfllp)write function to convert vowel char into next char'''
'''
def encode_decode(s):
    new_string=""
    for i in range(len(s)):
        code=ord(s[i])
        if(s[i]=='a' or s[i]=='e' or s[i]=='i'or  s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=="O" or s[i]=="U"):

            
            new_string+=chr(code+1)
        else:
            new_string+=s[i]
    print(new_string)
s=input()
encode_decode(s)
'''

#                       strings easy problems


# 1. Create a string with your name and print it.
name="Siva Charan"
print("my name:",name)
# 2. Get the first character from the string.
print(name[0])
# 3. Get the last character from the string.
le=len(name) #length of string
print(name[le-1])
# 4. Concatenate two strings.
surname="Kammampati"
name=surname+" "+name
print(name)
# 5. Repeat a string 3 times.
print(name*3 ,end='\n')
# 6. Slice the first 5 characters.
print(name[0:5])
# 7. Reverse a string using slicing.
print(name[::-1])
# 8. Check if a substring exists in a string.
sub_str="Siva"
if sub_str in name:
    print("substring is present")
else:
    print("substring is not present")

# 9. Find the length of a string.
print("length:",len(name))
# 10. Convert string to uppercase.
Upper_name=name.upper()
print(Upper_name)
# 11. Convert string to lowercase.
Lower_name=name.lower()
print(Lower_name)
# 12. Capitalize the first letter.
#             captilize means put uppercase in string
cap_name=name.capitalize()
print(cap_name)
# 13. Convert a string to title case.
title_name=name.title()
print(title_name)
# 14. Remove leading spaces using lstrip().
str1="         name: siva"
str1=str1.lstrip()
print(str1)
# 15. Remove trailing spaces using rstrip().
str_r="name:siva           "
str_r=str_r.rstrip()
print(str_r)
# 16. Remove both ends’ spaces using strip().
str_strip="        name:siva         "
str_strip=str_strip.strip()
print(str_strip)
# 17. Replace all spaces with underscores.
print(name.replace(" ",'_'))
# 18. Count how many times a character appears.
for i in range(len(name)):
    print("char:",name[i],"times:",name.count(name[i]))
# 19. Find index of a character using find().
# find()-> return the index of char in string
ch='K'
print(name.find(ch))
# 20. Use rfind() to find last occurrence.
# rfind()-> returns postion of char index from right most postion
ch='a'
print(name.rfind(ch))
# 21. Use index() to find substring position.
sub="aran"
print(name.index(sub))
# 22. Split a string by spaces.
print(name.split(" "))
name2=name.split()
# 23. Join a list of words into a string.
print(" ".join(name2))
# 24. Check if string starts with "Hello".
name1="Hello"+name
print(name1)
if(name1.startswith("Hello")):
    print("yes it has")
else:
    print("NO hello is not there")
# 25. Check if string ends with "world".
st="HeloWorld"
print(st.endswith("World"))
# 26. Check if a string is digit.
st1="1234567"
print("number:",st1.isdigit())
# 27. Check if a string is alphabet.
print("all alpha:",st.isalpha())
# 28. Check if a string is alphanumeric.
print(name)
print("alphanum:",name.isalnum())
# 29. Get ASCII value of a character.
c='R'
print(c,"ascii:",ord(c))
# 30. Convert ASCII to character.
n1=82
print(n1,"ascii:",chr(n1))
# 31. Remove punctuation from string.
pun_str="" '''noooooooooooooooooooooo'''
# 32. Swap case of all characters.
print(name.swapcase())
# 33. Count total words in a string.
print(name)
cnt_space=name.count(" ")
words=cnt_space+1
print(words)
# 34. Count total sentences in a string.
'''noooooooooooooooooooooooooooooo'''
# 35. Convert string to list of characters.
print(name)
str_to_list=list(name)
print(str_to_list)
# 36. Convert list of characters to string.
list_to_str="".join(str_to_list)
print(list_to_str)
# 37. Pad string to the left with * to length 10.
w="siva"
# print(w.zfill(9)) 00000siva
print(w.rjust(10,'*'))
# 38. Center align string using center().
print(w.center(6,'*'))
# 39. Format string with variables using f-string.
edu="B.tech"
year=2025
marks=8.3
print(f"my name is :{name} graduated from {edu} in {year} with {8.3} CGPA")

# 40. Use % operator to format a string.
print("my name is %s and completed my %s in year %d with %f CGPA."%(name,edu,year,marks))

