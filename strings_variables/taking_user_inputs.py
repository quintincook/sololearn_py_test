# to get input from the user in Python, you can user the intuitevly named input function. 
# the input function prompts the user for input, and returnes what they enter as a string(wiht the contents automatically escaped)
x = input() 
print(x)
#even iff the user enters a number, it is processed as a string 

#the input statement needs to be followed by a parenthese
# can provide a string to input() between the parentheses, producing a promt message
name = input("Enter name here: ")
print("Welcome " + name)
#promt message helps to clarify what imput the program is asking for 