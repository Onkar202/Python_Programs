# 4. A file contains a word "Donkey" multiple times. You need to write a program which
# replace this word with ##### by updating the same file.

with open("Chapter_09_File_(I-O)/animals.txt","r") as f:
    content = f.read()
    content = content.replace("donkey","######")

with open("Chapter_09_File_(I-O)/animals.txt","w") as f:
    f.write(content)
    
    # print(lines)