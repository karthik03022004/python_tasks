'''="Python"
print(str[0])
print(str[-1])
print(str[2])
print(str[0:3])

str1="Siva charan"
print(str1[0:11:2])'''


'''str="Hello World"
print(str[1])
print(str[-1])
print(str[1:3])
print(str[1:-1])
print(str[:3])
print(str[2:])
print(str[:-1])
print(str[::2])
print(str[1::2])
print(str[::-1])# reverse the word
print(str[-1::])'''

# string concat
'''first_name=input("enter first name:")
last_name=input("enter last name:")
full_name=first_name+" "+last_name
print(full_name)'''


#length of string
'''str=input()
print(len(str))'''
#methods in string
'''str="Siva Charan"
print(str.upper())
print(str.lower())
print(str.strip())
print(str.replace('a','k'))
print(str.count('a'))
print(str)'''


#print('siva\'s car \nand siva\"s ')

#problems on strings
#count vowels in string
'''str=input()
str=str.lower()
a=str.count('a')
e=str.count('e')
i=str.count('i')
o=str.count('o')
u=str.count('u')

print(f"no of vowels:{a+e+i+o+u}")
'''
# grade calculator
'''m=int(input())
p=int(input())
c=int(input())
tot=m+p+c
avg=tot/3
percentage=((tot)/300)*100
grade=""
if percentage>=90:
    grade="A"
elif percentage>=80:
    grade="B"
elif percentage>=70:
    grade="C"
else:
    grade="F"
print(f"total marks:{tot} and avg marks:{avg} \n grade:{grade}")'''

# check palindrome
'''str=input("enter word:")
if(str==str[::-1]):
    print(f"{str} is a palindrome")
else:
    print(f"{str}not a plaindrome")'''


# largest 
'''x=int(input())
y=int(input())
z=int(input())
if(x>y and y>z):
    print(f"{x} is biggest")
elif(y>x and y>z):
    print(f"{y} is biggest")
else:
    print(f"{z} is biggest")'''

#leap year
'''year=int(input("enter yera in integer format only:"))
if((year%400==0) or (year%4==0 and year%100!=0)):
    print(f"{year} is leap year")
else:
    print(f"{year} not leap year")'''

# temp convert with if else
'''
temp=float(input("enter tmeperature:"))
unit=input("enter unit")
unit=unit.lower()
if(unit=='c'):
    res1=(9/5)*temp+32
    res2=273+temp
    print(f"temp in farheit:{res1} F")
    print(f"temp in kelvin is{res2} K")
elif(unit=='f'):
    res1=(5/9)*(temp-32)
    res2=res1 +273
    print(f"temp in clecius :{res1} C")
    print(f"temp in kelvin is:{res2} K")
elif(unit=='k'):
    res1=temp-273
    res2=(5/9)*(temp-273)+32
    print(f"temp in celcius :{res1}C")
    print(f"temp in farhenheit:{res2}F")
else:
    print("enter correct unit")'''

str1="Siva charan"
print(str1[0:11:2])
