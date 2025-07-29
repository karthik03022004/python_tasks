set1={1,2,3,4,5,6}
for i in set1:
    print(i)
# --------------------------
set1.add(7)
print(set1)
# ----------------------------
set1.update({9,10})
print(set1)
# -------------
set1.remove(10)
print(set1)
# -----------------------
set1.discard(11)
print(set1)
# ------------------
set1.add(True)
print(set1)
set2={True,10,8,7}
com=set2.union(set1)
print(com)
inter=set2.intersection(set1)
print(inter)
dif=set1.difference(set2)
print(dif)
sydiff=set1.symmetric_difference(set1)
print(sydiff)
print(set1.issubset(set2))
# ----------------------------------
# Task
# Create a set with integers and print it.
s1={1,2,3,4,5,6,7,8,9}
for i in s1:
    print(i)