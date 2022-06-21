#range 
#the range() function returns a sequence of numbers 
#by default, it saterts from 0, increments by 1 and stops before specified number 
numbers = list(range(10))
print(numbers)
#in order to output the range as a list, we need to explicitly convert it to a slit, using the list function 
nums = list(range(5))
print(nums[4])

#if range is called with one argument, it produces an object with values form 0 to that range
# if it is called with two arguments, it produces values from the first to the secondn 
numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0,20))

nums = list(range(5, 8))
print(len(nums))

#range can have a third argument, which determines the interval of the sequence produced, also called the step 
numbers = list(range(5, 20, 2))
print(numbers)
#We can also create list of decreasing numbers, using a negative number as the third argument, for example list(range(20, 5, -2)).

nums = list(range(3, 15, 3))
print(nums[2])

#the for lop is commonly used to repeat some code a certain number of times
#this is done by combining the for loops with range objects 
for i in range(5): 
    print("hello!")
#dont need to call list on the range object when it is used in a for loop, becasue it isnt being indexed, so a list isnt required

a = int(input())
b = int(input())
print(list(range(a,b)))

for i in range(10):
  if not i % 2 == 0:
    print(i+1)

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])