word=open('romeo.txt','r')

# count=0
# for line in word:
#     line.strip()
#     count=count+1

# print("Lines ", count)

# inp=word.read()
# print(len(inp))
# print(inp[:100])

for line in word:
    line=line.rstrip()
    if line.startswith('move'):    #another logic to print this would be using if not line.startswith(): continue
        print(line)
inp=input('Enter the file name: ')
try:
    fh=open(inp)
except:
    print("{} does not exist".format(inp))
count=0
total=0
for line in fh:
    if not 'X-DSPAM-Confidence:' in line:
        continue
    else:
        count=count+1
        data=line.find(":")
        value=line[data+1:]
        total=total+float(value)

print("Average spam confidence: ", total/count)

# range returns a list 
t=[12,345,3,15,567,567,3,23,5]
print(t[::-1])

# split() breaks a string into a parts and produces a list of strings
