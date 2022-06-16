#while loops 
# for example, lets say we need to process multiple user inputs, so that each time the user inputs something, the same block of code needs to execute
#below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates 

i = 1
while i <= 5: 
    print(i)
    i = i + 1

print("Finished!")
#During each loop iteration, the i variable will get incremented by one, until it reaches 5
#So, the loop will execute the print statement 5 times 

items = int(input())
days = int(input()) 

i = 1
while i <= days: 
    items =items * 2
    i = i + 1

print(items )

#you can use multiple statements in the while loop 
#for example you can use an if statement to make decisions.
#this can be useful, if you are making a game and need to loop thorugh a number of player actions and add or remove points of the player
# the code below uses an if/else statement inside a while loop to separate the even and odd numbers in the range of 1 to 10

x = 1
while x < 10: 
    if x%2 == 0:
        print(str(x) + " is even")
    else: 
        print(str(x) + " is odd")
    
    x +=1
#str(x) is used to convert the number x to a string, so that it can be used for concatenation.

#break
#to end a while loop prematurely, the break statement can be used 
#for example, we can break an infinite loop if some condition is met:
print("\nbreak")
i = 0 
while True: 
        print(i)
        i = i + 1
        if i >= 5: 
            print("Breaking")
            break

print("Finished") 
#while True is a short and easy way to make an infinite loop 
#an example use case of break: 
# An infinite while loop can be used to continuously take user input. 
# For example, you are making a calculator and need to take numbers from the user to add and stop, when the user enters "stop".
# In this case, the break statement can be used to end the infinite loop when the user input equals "stop".
# Using the break statement outside of a loop causes an error 

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

#continue
#another statement that can be used within loops is continue. 
#unlike break, continue jumps back to the top of the loop, rather than stopping it
#Basically, the continue statements stops the current iteration and continues with the next one 
print("\nContinue")
i = 0 
while i <5: 
    i += 1 
    if i == 3:
        print("Skipping 3")
        continue
    print(i)

# An example use case of continue:
# An airline ticketing system needs to calculate the total cost for all tickets purchased. 
# The tickets for children under the age of 1 are free. We can use a while loop to iterate 
# through the list of passengers and calculate the total cost of their tickets. Here, the continue statement can be used to skip the children.
# using the continue statement outside of a loop causes an error 