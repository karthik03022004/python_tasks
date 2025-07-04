#    write a function to return Number of palindromes in a string
def count_palindrome(s):
    s=s.split(" ")
    cnt=0
    for i in range(len(s)):
        if(s[i][::-1]==s[i]):
            cnt+=1
            print("Palindromes in string is:",s[i])
    print("Total Palindromes in string:",cnt)
s=input("enter:")
count_palindrome(s)

'''
output:
enter:my family consists of amma akka anna naana
Palindromes in string is: amma
Palindromes in string is: akka
Palindromes in string is: anna
Total Palindromes in string: 3'''