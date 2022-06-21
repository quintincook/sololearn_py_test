#for loop
# the for loop is used to iterate over a given sequence, such as lists or strings
#the code below outputs each item in the list and adds an exclamation mark at the end 
words = ["hello", "world", "spam", "eggs"]
for word in words: 
    print(word + "!")
# In the code above, the word variable represents the corresponding item of the list in each iteration of the loop.
# During the 1st iteration, word is equal to "hello", and during the 2nd iteration it's equal to "world", and so on.

#the for loop can be used to iterate over strings
str = "testing for loops"
count = 0 

for x in str: 
    if(x == 't'):
        count += 1

print(count)
# The code above defines a count variable, iterates over the string and calculates the count of 't' letters in it.
# During each iteration, the x variable represents the current letter of the string.
# The count variable is incremented each time the letter 't' is found, thus, at the end of the loop it represents the number of 't' letters in the string.
#Similar to while loops, the break and continue statements can be used in for loops, 
# to stop the loop or jump to the next iteration.

list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break

#for vs while 
#both, for and while loops can be used ot execute a block of code for multiple times
# it is common to use the for loop when the number of iterations is fixed 
#for example, iterating over a fixed list of items in a shopping list
#the while loop is used when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop
# for exampl, ending the loop when the user enters a specific input in a calculator program 
# both the for and while loop can be used to achieve the same results, however, the for loop has cleaner and shorter syntax, making it a better choice in most cases 

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

for x in list: 
    sum = sum +x

print(sum)