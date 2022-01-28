
# Ask usr for a number  
# return the sumation
# ex user enters 4. you need to return 4 + 3 + 2 + 1 + 0, which is 10

print('------------- START ----------------')
xstr =input("enter a number ")
xnum= int(xstr)
sum=xnum
x=xnum
while(x>0):
    x=x-1
    sum=sum+x   
print("The sum is : ", sum)

print('------------- END ----------------')
