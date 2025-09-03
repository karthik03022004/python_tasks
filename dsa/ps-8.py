# l=[1,2,3,4]
# l.append(5)
# print(l)
# # ------------
# l=[1,2,3,4]
# l.remove(3) #remove(ele)
# print(l)
# # ------------------
# l=[1,2,9,8]
# print(f"max:{max(l)}")
# # ----------------------------
# l=[1,2,9,8]
# print(f"max:{min(l)}")
# print(f"min:{sum(l)}")
# # --------------------
# l=[1,2,2,3,2]
# print(f"countof 2:{l.count(2)}")
# print(f"reverse_list:{l.reverse()}cla")


# ps-10
l=[[1, 2], [3, 4]]  #output:[1,4]
res=[]
rows=len(l)
for i in range(rows):
    for j in range(len(l[i])):
        if(i==j):
            res.append(l[i][j])
print(res)
# -------------
l=[[1, 2], [3, 4]]  #output:[2,3]
res=[]
rows=len(l)
for i in range(rows):
    for j in range(len(l[i])):
        if(i+j==rows-1):
            res.append(l[i][j])
print(res)

# -------------------
l=[[1, 2], [3, 4]]  #output:[2,3]
res=[]
rows=len(l)
for i in range(rows):
    for j in range(len(l[i])):
        if(i!=j):
            res.append(l[i][j])
print(res)
# ----------------------
