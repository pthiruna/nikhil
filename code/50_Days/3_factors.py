print('------------- START ----------------')
xstr =input("enter a number ")
xnum= int(xstr)
x=1
while(x<=xnum):
    z=xnum%x
    if(z==0):
        print(x)
    x=x+1
print('------------- end ----------------')
