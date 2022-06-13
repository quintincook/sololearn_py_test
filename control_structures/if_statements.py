#you can use if statements to run code if a certain condition holds
#if an expression evaluates to True, some statements are carried out
#otherwise, they aren't carried out
#an if statement looks like this: 
# if expression: 
#     statement 
if 10 > 5: 
    print("10 greater than 5")

print("Program ended")

temp = int(input())
if temp >= 100: 
    print("Boiling")

num = 12
if num > 5:
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")

num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")