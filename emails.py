inp=input("Enter the name of the file: ")
try:
    fh=open(inp)
except:
    print("FIle does not exist")
    quit()
count=0
for line in fh:
    line=line.strip()
    if not line.startswith('From '):
        continue
    count=count+1
    word=line.split()
    print(word[1])

print("There were {} line with From as the first word".format((count)))