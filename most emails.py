inp=input("Enter the name of the file: ")
if len(inp)<1:
    inp='one.txt'
try:
    fh=open(inp)
except:
    print("FIle does not exist")
    quit()
count=0
dct=dict()
lst=[]
for line in fh:
    line=line.strip()
    if not line.startswith('From '):
        continue
    # count=count+1
    word=line.split()
    lst.append(word[1])
for words in lst:
    dct[words]=dct.get(words,0)+1

# print(dct)
mname=None
ncount=None
for name,count in dct.items():
    if ncount is None or count>ncount:
        mname=name
        ncount=count
        
print(mname,ncount)
# print("There were {} line with From as the first word".format((count)))