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
