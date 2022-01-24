print('------------- START ----------------')
xstr =input("Enter the last number of the fibonnaci series: ")
xnum= int(xstr)
ppa=1
pa = 1
a=pa
while(a<xnum):
    ppa=pa
    pa=a
    a=pa+ppa
    print(a)
if(a>xnum):
    print('number not in fibonnaci series')
print('------------- END ----------------')