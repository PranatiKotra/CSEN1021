n=int(input("Enter a number:"))
temp=n
rev=0
while(n>0):
  d=n%10
  rev=rev*10+d
  n=n//10
if temp==rev:
  print("PALINDROME NUMBRE")
else:
  print("NOT A PALINDROME NUMBRE")
n1=n
i=1
s=0
for i in range(n):
  if(n%i)==0:
    s=s+i
if n==s:
  print("PERFECT NUMBRE")
else:
  print("NOT A PERFECT NUMBRE")
