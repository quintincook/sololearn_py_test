#assume we want to take the age of the user as input.
#we know that the input() function returens a string.
# to convert it to a number, we can use the int() function: 
age = int(input())
print(age)

#similarly, in order to convert a number to a string, the str() funciton is used. 
# thsi can be useful if you need to use a number in string concatenation 
age = 42 
print("his age is " +str(age))
#you can convert to float using the float() function 

x = "2"
y = "4"
z = int(x) + int(y)
print(z)

#you can use input() multiple times to take multiple user inputs 
name = input()
age = input()
print(name + " is " +age)
#when input() function executes, program flow stops until a user enters some value

x = input()
y = input()
print ( x * int(y))