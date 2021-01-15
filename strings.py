fruit=input("Enter a fruit name: ")
index=0

while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1


for letter in fruit:
    print(letter)

#count a letter in a word
sword=input("Enter word: ")
alphabet=input("Enter a letter you want to count: ")
count=0

for letter in sword:
    if letter == alphabet:
        count=count+1
    print(count)

# str.replace('bob','allen')
# str.find('a')
# str.upper()
# str.lower()   each makes a copy of the original string
#str.strip() strips whitespaces from both ends (left, lstrip) (right, rstrip)
#str.startswith('Please') returns true or false

#parsing and extracting
data='From stephen.marguard@uct.ac.za Sa Jan 09:14:16 2008'
atpos=data.find('@')
sppos=data.find(' ',atpos)
host=data[atpos+1:sppos]
print(host)
