n=int(input("Enter a number "))
s=n
b=len(str(s))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==sum:
    print(s," is an armstrong number")
else:
    print(s," is not an armstrong number")
