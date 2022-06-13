#operator precedence is a very important concept in programming. 
#it is an extension of the mathematical idea of order of operations(multiplication being performed before addition, etc.) to include other operators, such as those in boolean logic 
print(False == False or True)

print(False == (False or True))

print((False == False) or True)
#pythons order of operations is the smae as that or normal mathematics: 
# parentheses first, then exponentiation, then multiplication/division, and then addition/ subtraction

if 1 + 1 * 3 == 6:
   print("Yes")
else:
   print("No")

grade = 88
if (grade >= 70 and grade <= 100): 
    print("passed!")

type = input() 
if (type == "Visa" or  type =="Amex"): 
    print("accepted")

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")