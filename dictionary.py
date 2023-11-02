# MyDict={
#     "university":"gla university",
#     "location":"mathura",
#     "year":"2010"
# }
# print(MyDict)



# MyDict1={
#     "university":"gla university",
#     "location":"mathura",
#     "year":"2010"
# }
# print(MyDict1["university"])



# MyDict2={
#     "university":"gla university",
#     "location":"mathura",
#     "year":"2010",
#     "year":"1990"
# }
# print(MyDict2["year"])
# print(len(MyDict2))
# print(type(MyDict2))






# thisDict={
#     "brand":"ford",
#     "electric":"false",
#     "year":"1978",
#     "colors":["red","white","green"]
# }
# print(thisDict)

# DataDetails=dict(name="john",age=45,country="Norway")
# print(DataDetails)



# # MyDict={
# #     "university":"gla university",
# #     "location":"mathura",
# #     "year":"2010"
# }

# check=MyDict["year"]
# print(check)

# x=MyDict.get("year")
# print(x)

# x1=MyDict.keys()
# print(x1)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":"1967"
# }
# x=car.keys()
# print(x)

# car["color"]="white"
# print(car)
# print(x)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":"1967"
# }
# if "model" in car:
#     print("yes")

# thisDict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1963
# }

# 



# for x in thisDict:
#     print(thisDict[x])



# for x in thisDict.values():
#     print(x)

# for x in thisDict.keys():
#     print(x)


# thisDict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1963
# }
# thisDict.pop("model")
# print(thisDict)

# thisDict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1963
# }
# del thisDict["model"]
# print(thisDict)

# mystudents={
#     "stud1":{
#         "name":"anas",
#         "age":18,
#         "village":"jattari"
#     },
#     "stud2":{
#         "name":"ram",
#         "age":19,
#         "village":"ushrah"
#     },
#     "stud3":{
#         "name":"shyam",
#         "age":20,
#         "village":"tappal"
#     }
# }

# print(mystudents)

# for x in mystudents:
#     print(x)

# WORKSHOP PYTHON
# CREATING A DICTIONORY
# student={
#         "name":"Alice",
#     "age":25,
#     "grade":"A"
# }
# ACCESING VALUE OF DICTIONORY
# ACCESSING VALUE BY USING KEY
# name=student["name"]
# age=student["age"]
# MODIFING
# student["age"]=35
# student["city"]="new york"
# ITERATING THROUGH DICTIONORY
# FOR KEY,VALUE IN student.items()
# # print(f"{key}:{value}")
# student={
#         "name":"Alice",
#         "age":25,
#         "grade":"A"}
# print(f"The dictionary is {student}")
# student["age"]=17
# print(f"The dictionary is {student}")
# student["name"]="lav"
# print(f"The dictionary is {student}")

# squares={num:num**3 for num in range(1,6)}
# print(squares)
# removing the key value
# del student["grade"]

# questionn 1=
# student={
#     "name":"alice",
#     "age":25,
#     "grade":"b"
# }
# student["city"]="new york"
# a=student.get("city")
# print(a)

# num={
#     0:10,
#     1:20
# }
# num[2]=30
# print(num)

# dic1={
#     1:10,2:20
# }
# dic2={
#     3:30,4:40
# }
# dic3={
#     5:50,6:60
# }
# dic1. update(dic2)
# dic1.update(dic3)
# print(dic1)


# dic={'x':10,'y':20,'z':30}
# for key,values in dic.items():
#     print(f"{key}={values}")

# squares={num:num**2 for num in range(1,16)}
# print(squares)

# squares={num:num**2 for num in range(1,6)}
# print(squares)

# my_dic={'data':100,'data2':-54,'data3':247}
# sum=0
# for value in my_dic.values():
#     sum=sum+int(value)
# print("the sum is",sum)

# color_dict={'red':'#ff0000','green':'008000','black':'000000'}
# color_dict1={1}
# x=color_dict.keys()
# l_list=[]
# for i in x:
#     l_list.appened(i)
# l_list=sorted(l_list)
# for j in l_list:
#     color_dict[j]=color_dict[j]
# print(color_dict)
# print(type(color_dict))

# color_dict={'red': '#FF0000', 'green': '#008000', 'black': '#000000', 'white': 'FFFFFF'}
# color_dict1={}
# x=color_dict.keys()
# l_ist=[]
# for i in x:
#     l_ist.append(i)
# l_ist1=sorted(l_ist)
# for j in l_ist1:
#     color_dict1[j] = color_dict[j]
# print(color_dict1)
# print(type(color_dict1))

d={1:10,2:20,3:30,4:40,5:50,6:60}
k=int(input("enter the key to be searched"))
if k in d:
    print("found")
else:
    print("not found")