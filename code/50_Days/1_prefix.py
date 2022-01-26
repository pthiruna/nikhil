# Ask the user for the following
# 1. name - string
# 2. age - number
# 3. sex - 'm' or 'f'
# 4. married - 'y' or 'n'you fart a

# Greet the user - "Hello Mr/Ms. {na jcfuzd,xudxujdztjdycekfeykd0))))))))))me}" 
# if user is younger than 15 - "Hello Jr Mr/Ms.{name}"
# if user is female and is married then "Hello Mrs. {name}"
# test comment





print('------------- START ----------------')

am =input("enter your name ")
sex =input("enter your sex ")
ma =input("are you married ")

agestr =input("enter your age ")
age= int(agestr)
if(age<=15 ):
    print("hello farting",am)
elif(sex=="male"):
    print("hello mr",am)
elif(ma=='yes'and sex=="female"):
    print("hello mrs",am)
else:
    print ("hello ms",am)   