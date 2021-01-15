# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to
#  the list. When the program completes, sort and print the resulting words in alphabetical order

inp=input('Enter file name: ')
try:
    fh=open(inp)
except:
    print('File does not exist')
    quit()
lst=list()
for line in fh:
    line=line.strip()
    word=line.split()
    for x in word:
        if x in lst:
            continue
        lst.append(x)
lst.sort()
print(lst)

