largest=None
smallest=None

while True:
    val=input("Enter a number: ")
    if val=='done':
        break
    try:
        ival=int(val)
    except:
        print("Invalid data")
        continue
    if largest is None:
        largest=ival
    elif ival>largest:
        largest=ival
    if smallest is None:
        smallest=ival
    elif ival<smallest:
        smallest=ival

print('Maximum is',largest)
print('Minimum is',smallest)
