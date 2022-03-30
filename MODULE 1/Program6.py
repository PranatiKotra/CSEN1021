a=int(input("Enter an integer number 1:"))
b=int(input("Enter an integer number 2:"))
op=input("Enter the operator to be used:")
if op=="+":
  print(a+b)
elif op=="-":
  print(a-b)
elif op=="*":
  print(a*b)
elif op=="/":
  print(a/b)
elif op=="%":
  print(a%b)
else:
  print("OPERATOR NOT FOUND")
