
p = float(raw_input("Enter amount: "))
n = float(raw_input("Enter in years: "))
r = float(raw_input("Enter rate: "))

r = (r/100)/12
n = n * 12

x = (1+r)**n
print "$%.2f" % (p*((r*x)/(x-1)))
