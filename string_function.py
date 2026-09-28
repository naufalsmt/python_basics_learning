str1 = 'rahulshettyacademy.com'
str2 = "udemy"
str3 = " Naufal "
str4 = "this.is.time"
str5 = "rahul"

f1 = str1[0]
print(f1)
f2 = str1[0:5]
print(f2)
f3 = str1 + str2
print(f3)
f4 = str3.split() # split the string and make it an array
print(f4)
f5 = str4.split(".") # split the string by dots and make it an array
print(f5)
print(f5[0])
f6 = str3.lstrip() # remove space from left
print(f6)
f7 = str3.rstrip() # remove space from right
print(f7)
f8 = str3.strip() # remove space from both side
print(f8)
f9 = str5 in str1 # check the text from str5 in str1
print(f9)
f10 = str5 in str2 # check the text from str5 in str2
print(f10)

