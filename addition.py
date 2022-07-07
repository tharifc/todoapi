n=int(input("enter the number"))
s=0
num1=num=n
count=0
while(n>0):
    d=n%10
    count=count+1
    n=n//10
print(count)
while(num>0):
    d=num%10
    s=s+d**count
    num=num//10
if(num1==s):
    print("armstrong number")
else:
    print("not armstrong")
