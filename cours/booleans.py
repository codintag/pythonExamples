
#Booleans  = True or False

print( 10 > 5) # return True

print(5 == 5) #return True

print(10 < 5) #return false

#make a condition

x = 25
y = 18

if x > y:
    print('x is greater than y')
else:
    prin('x is not greater than y')


#evaluate values and variables with bool() function
print(bool("Bonjour"))
print(bool(34))

#All the following Values will return False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}) )
