def computepay(h,r):
    try:
        ihrs=float(h)
        irate=float(r)
    except:
        print("Enter numbers")
        quit()
    if ihrs <= 40:
        pay=ihrs*irate
        return pay
    else:
        pay=ihrs*irate
        ipay=(ihrs-40)*irate/2
        total=pay+ipay
        return total



hrs=input("Enter hours worked: ")
rate=input("Enter rate: ")
p=computepay(hrs,rate)
print("Pay",p)