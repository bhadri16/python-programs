# BMI
print("please enter the weight in terms of kilogram ")
H=int(input())
print("please enter the height in terms of meters")
G=float(input())
W=H/G**2
if (W<=18.5):
    print("the person is under weight")
elif(W>18.5 and W<24.9 ):
    print("the person is normal ") 
elif(W>=25 and W<=29.9):
    print("the person is over weight ")
elif(W>=30 and W<=34.9):
    print("the person is obese")
else:
    print("invalid input ")