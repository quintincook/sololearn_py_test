#boolean logic 
#is used to make more complicated conditions for if statements that rely on more than one condition
#pythons boolean operators are and, or, and not 
# the and operator takes two arguements, and evaluates as True if, and only if, 
#both of its areguemnts are True. otherwise, it evaluates to false
print( 1 == 1 and 2 ==2 )
print(1 == 1 and 2 == 3 )
print( 1 != 1 and 2==2)

#ex 
humidity = int(input()) 
if 40 <= humidity and 60 >= humidity: 
    print("norm")

#the or operator also takes two arguments. it evaluates to True if either(or both) of its arguments are True, and False if both arguments are false
print(1 == 1 or 2 == 2)

print(1 == 1 or 2 == 3)

print(1 != 1 or 2 == 2)

print(2 < 1 or 3 >  6)

#unlike the other two operators above, not only takes one argument and inverts it
# the result of not true is false and not false goes to true 
print(not 1 == 1)
print( not 1 > 7) 

if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")