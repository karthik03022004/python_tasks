
details={
    "age":21,
    "city":"hyd"
    
}
print(dict["city"])
# dict is mutable 
details["name"]="siva"
print(details)

company={
    "google":"sundar pichai",
    "apple":"timcook",
    "twitter":"musk"
}
val=company.get("apple") #get method
print(val)
print(company.get("amazon","print this if not"))

print(company.keys()) #keys method -dict_keys(['google', 'apple', 'twitter'])

print(len(company)) # len works for strings,list,dict

print(company.values()) #values method- dict_values(['sundar pichai', 'timcook', 'musk'])
print(company.items()) #items method-dict_items([('google', 'sundar pichai'), ('apple', 'timcook'), ('twitter', 'musk')])

for i in company.items():
    if "google" in i:
        print(i)

print(company.update({"apple":"timcoo"}))
print(company)
places={
    "hyd":"biryani",
    "guntur":"bajji",
    "kkd":"sewt"
}
places.update({"kkd":"sweet"})
print(places)
places["ttd"]="laddu"
print(places)
print(places.popitem()) #popitem returns last item
marks={
    "siva":99,
    "siva ch":95,
    "bhargav":88,
    "srinivas":93
}
# avg of marks
tot=0
cnt=0
for i in marks.values():
    tot+=i
    cnt+=1
print("avg:" ,tot/cnt)
student={
    "name":"siva",
    "marks":[99,98,87,96,95],
}
tot=sum(student["marks"])
print(tot)
student["sum"]=tot
print(student)