# try:
#    l=10/5
# except Exception as e:
#     print(f"error :{e}")
# else:
#     print(l)
# finally:
#     print("final block")
# ------------------------------------
# file handling
# creating a file using write
# try:
#     file=open("textfile1.txt" "r")
# except Exception as e:
#     print(e)
# else:
#     print(file.readlines())
#     file.close()
# finally:
#     print("this is final block")
'''---------------------------------'''
# try:
#     file=open("./textfile1.txt","w")
# except Exception as e:
#     print(e)
# else:
#     file.write("this is the first line in file\n")
#     file.write("this is the second line")
# file=open("textfile1.txt","w")
'''-----------------------------------------'''
# file.write("line1")
# file.write("line2")
# file.writelines("[line1,line2]")
# file.close()
'''-------------------------------------------'''
# try:
#     file=open("sample.txt","r")
#     print(file.read())
# except Exception as e:
#     print(e)
# finally:
#     print("the end")
'''--------------------------------------------------'''
with open("sample.txt",'r') as file:
    
    
    file.flush()
    file.seek(5) #moves cursor to a specified positions
    print(file.read())
    print(file.tell())
    
    

