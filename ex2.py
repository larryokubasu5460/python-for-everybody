# text = "X-DSPAM-Confidence:    0.8475";

# ipos=text.find('0')
# # epos=text.find('',ipos)
# data=text[ipos:]
# print(float(data))

# finding average
# count=0
# sum=0
# print("Before ",count,sum)
# for value in [10,11,12,13,145,135,1456,90]:
#     count=count+1
#     sum=sum+value
#     print(count,sum,value)
# print("After ",sum,count,sum/count)

# finding largest

# largest=-1
# for value in [4,56,0,234,56,2345,341]:
#     if value>largest:
#         largest=value
#     print("current value {}, Largest so far: {}".format(value, largest))
# print("Largest: ",largest)

# for i,value in enumerate([45,6,76,890,786]):
#     if value==890:
#         print("Position of 890 is:", i)

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
