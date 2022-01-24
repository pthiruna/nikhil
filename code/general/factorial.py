print('------------- START ----------------')
# use enters 4. then print
# calculate the ans. which is a = 4 * 3 * 2 * 1 
# print the ans = 24
# if user enters 2 . a = 2 * 1 ; wich is 2

xstr = input("Enter a number : ")
xnum = int(xstr)
a= xnum
c= xnum -1
while(c > 0):
    a=a*c
    c=c-1
print(a)


print('------------- end ----------------')
