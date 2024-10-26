n=int(input("Enter Number Here:"))
num=n
a=0
y=len(str(n))
print()
for i in range(len(str(n))):
    b=n%10
    n=n//10
    a=a+(b**y)
print("The sum of digits is:" , a)
if a==num:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")
print()
