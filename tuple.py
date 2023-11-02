# myTuple=("apple","banana","cherry")
# print(myTuple)

# myTuple1=("apple","banana","cherry","apple","cherry")
# print(myTuple1)
# print(len(myTuple1))
# print(type(myTuple1))

# tuple1=("apple","banana","cherry")
# tuple2=(1,5,7,9,3)
# tuple3=(True,False,False)
# print(tuple1,tuple2,tuple3)

# # myTuple2=tuple("apple","banana","cherry")
# print(myTuple2)

thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x)

thistuple=("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])



thistuple=("apple","banana","cherry")
print(thistuple[1])


thistuple=("apple","banana","cherry","kiwi","orange")
print(thistuple[2:5])

thistuple=("apple","banana","cherry","kiwi","orange")
print(thistuple[:4])

thistuple=("apple","banana","cherry","kiwi","orange")
print(thistuple[2:])


thistuple=("apple","banana","cherry","kiwi","orange")
print(thistuple[-4:1])

thistuple=("apple","cherry","banana")
if "apple" in thistuple:
    print("yes,'apple' is in the fruit tuple")