from pickle import FALSE, TRUE


print('------------- START ----------------')
xstr =input("Enter a number: ")
xnum= int(xstr)
a=2
isPrime = TRUE
while(a<xnum):
    c=xnum%a
    if(c == 0):
        isPrime = FALSE    
    a=a+1

if(isPrime == TRUE):
    print("It is a prime number")
else:
    print("It is not a prime number")


print('------------- END ----------------')
















