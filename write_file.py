from os import write

with open("text.txt","r") as f: # open the file in read mode and mentioned as f
    content = f.readlines() # read the values in the files and stored to content
    with open("text.txt","w") as w: # open the file in write mode and mentioned as w
        for lines in reversed(content): # get each value from the content in the reverse order and saving to lines
            w.write(lines) # write lines back to file