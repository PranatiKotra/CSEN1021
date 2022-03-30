m1=int(input("Enter marks of subject 1:"))
m2=int(input("Enter marks of subject 2:"))
m3=int(input("Enter marks of subject 3:"))
m4=int(input("Enter marks of subject 4:"))
m5=int(input("Enter marks of subject 5:"))
marks=[m1,m2,m3,m4,m5]
total=0
for i in marks:
  total+=i
  avg=total/5
print(avg)
if avg>90 and avg<100:
  print("A+")
elif avg>80 and avg<90:
    print("A")
elif avg>70 and avg<80:
  print("B+")
elif avg>60 and avg<70:
  print("B")
else:
  print("FAIL")
