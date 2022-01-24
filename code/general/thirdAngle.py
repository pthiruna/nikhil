print('------------- START ----------------')
a1 =input("enter first angle ")
a2 =input("enter second angle ")
a1n = int(a1)
a2n=int(a2)
x=a1n+a2n
if(x>180):
    print("invalid angle")
elif(a1n < 0):
    print ("Are you kidding me ? Enter a positive angle")
else:
    print('The third angle is: ', 180-x)

print('------------- END ----------------')
print("oh my god I love your hair")                         