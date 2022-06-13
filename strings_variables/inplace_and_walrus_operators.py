#in-place operators 
#in place operators allow your to write code like 'x = x + 3' more concisely, as 'x +=3'
#the same thing is possible with other operators such as -,*,/ and % as well
x = 2 
print(x)
x +=3 
print(x)

x = 4 
x *=3
print(x)

#these operators can be used on types other than numbers, as well, such as strings
x = "spam"
print(x)
x += "eggs"
print(x)

x= "a"
x *=3
print(x)

#walrus operator  := allows you to assign values to variabels within an expression, including variables that do not exist yet
#Suppose we want to take an integere from the user, assign it to a variable num and output it: 
num = int(input())
print(num)
#the walrus operator accomplishes these operations at once: 
print(num:=int(input()))