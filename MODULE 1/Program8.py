a=int(input("Enter the starting range:"))
b=int(input("Enter the ending range:"))
print("EVEN num:")
for i in range(a,b):
  if i%2==0:
    print(i)
print("ODD num:")
for j in range(a,b):
  if j%2!=0:
    print(j)  
