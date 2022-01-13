print('------------- START ----------------')
# use enters 3. then print 
#  3 x 1 = 3
#  3 x 2 = 6 ...

xstr = input("Enter a number : ")
xnum = int(xstr)

t=0
while(t<=10):
    r = xnum*t
    print(xnum ,'x', t, '=', r)
    t=t+1
print('------------- END ----------------')


