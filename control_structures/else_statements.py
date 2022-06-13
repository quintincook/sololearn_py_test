#the if statement allows you to check a condition and run some statements, if the condition it True
# the else statement can be used to run some statements when the condition of the if statement is False 
#as with if statements, the code inside the block should be indented
x = 4
if x ==5: 
    print("Yes")
else:
    print("No")

age = int(input())
name = input()

if age >= 18: 
    print("Welcome " + name)
else: 
    print("Sorry")

if 1 + 1 == 2:
   if 2 * 2 == 8:
      print("if")
   else:
      print("else")    
# every if condition block can have only one else statment
# in order to make multiple checks, you can chain if and else statemtns
num = 3
if num == 1:
    print("One")
else: 
    if num == 2:
        print("Two")
    else: 
        if num == 3: 
            print("Three")
        else: 
            print("Something else")

#elif statments 
# multiple if/else statemtns make the code long and not very readable 
# the elif (short for else if) statemtn is a shortcut to use when chaining if and else steatements, making the code shorter
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3: 
    print("Three")
else: 
    print("Something else")