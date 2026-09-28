a, b, c = 2, 5.5, "hello"

print(a, b, c)

print(b)

print('-'*30)
# print("value is "+b)

print("{} {} {} {}".format("value is", b, "greater than", a))

print('-'*30)
# list
values = [1, 10, 20, "shetty"]  # array position becomes 0, 1, 2, 3

print(values[2]) # 2nd position = 20
print(values[0]) # 0th position = 1
print(values[-1]) # last position = shetty
print(values[1:3]) # position from 1 to 3 = 10,20 (include first but not include 3rd (0 to n-1))
values.insert(2, "raman") # inserting an object to 2nd position
print(values)
values.append(30) # add an object to last position
print(values)
values[2] = "RAMAN" # update second position object
print(values)
del values[2] # delete second position object
print(values)
values.remove(30) # remove a particular object from array
print(values)

print('-'*30)
# tuple -- same as list but not able to update
val = (100, 200, "good")
print(val)
print(val[2])

print('-'*30)
#  dictionary
dic = {"ab": 100, 10: 20, 35: "hello", "c": "world" }
print(dic)
print(dic["ab"])
print(dic["c"])
print(dic[10])
print(dic[35])

print('-'*30)
# create and add dictionary

address = {}

address["first_name"] = "Naufal"
address["last_name"] = "MT"
address["age"] = 40

print(address)
print(address["first_name"])

print('-'*30)
greeting = "Good morning"

if greeting == "Good afternoon":
    print("condition matches")
else:
    print("condition not matches")
print(greeting)

print('-'*30)
# for loop
num = [2, 4, 6, 8]
for i in num:
    print(i*2)

print('-'*30)
summation = 0
for j in range(1,11): # here range is '1' to '11-1' means 1 to 10
    summation += j # here summation = summation + j
print(summation)

print('-'*30)
for k in range(1,11,2): # here the range is 1 to 10 with increment by 2
    print(k)

print('-'*30)
#while loop

ex = 4
while ex > 1: # check the condition and this loop continue the execute until reach the condition
    print(ex)
    ex -= 1

print('-'*30)
ext = 10
while ext > 1:
    if ext != 5: # here loop skip 5 and complete the loop
        print(ext)
    ext -= 1

print('-'*30)
exr = 10
while exr > 1:
    if exr == 5: # loop break once exr reaches 5
        break
    print(exr)
    exr -= 1

print('-'*30)
ht = 10
while ht > 1:
    if ht == 9: # skip the number 9 and continue on loop
        ht -= 1
        continue
    if ht == 5: # loop brea once ht reaches 5
        break
    print(ht)
    ht -= 1

print('-'*30)
