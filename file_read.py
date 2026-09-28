file = open('text.txt')
# note: file read only one time if code written read multiple times.
# print(file.read()) # raad all content from the opened file
# # print(file.read(2)) # read only first two characters from the opened file
# print(file.readline()) # read only first line and if given one more same line of code without comment, second code
# print(file.readline()) # written second line

# method 1 - read all content from file by using while loop. when the variable read empty then loops exit
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

# method 2 - read all content from file by for loop. initially the content from the file convert to list
line = file.readlines() # this readlines() convert file content into to list format
for l in line:
    print(l)

file.close()