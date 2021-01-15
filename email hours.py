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
lst=list()
for line in fh:
    line=line.strip()
    if not line.startswith('From '):
        continue
    word=line.split()
    iword=word[5].split(":")
    lst.append(iword[0])
for words in lst:
    dct[words]=dct.get(words,0)+1
 
# print([(k,v) for k,v in sorted(dct.items())])
for k,v in sorted(dct.items()):
    print(k,v)