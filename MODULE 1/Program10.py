p=int(input("Enter principle amount:"))
r=int(input("Enter rate:"))
n=int(input("Enter time:"))
i=1
for i in range(n):
  interest=(p*r*n)/100
  amt=p+interest
  p=amt
print(interest)
