print("1.celcius to farenheit")
print("2.farenheit to celcius")
n=int(input("enter your choice"))
if n==1:
    c=float(input("enter the temperature in celcius"))
    f=9/5*c+32
    print("temperature in farenheit",f)
elif n==2:

    f=float(input("enter the temperature in farenheit"))
    c=(f-32)*5/9
    print("temperature in  celcius",c)
else:
    print("invalid input")
