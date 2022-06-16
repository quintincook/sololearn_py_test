#the appedn method adds an item to the end of an existing list
nums = [1, 2, 3]
nums.append(4)
print(nums) 
#the dot before append is there because it is a method of the list class. 
words = ["hello"]
words.append("world")
print(words[1])

#to get the number of items in a list, you can use the len function
nums = [1, 3, 5, 2, 4]
print(len(nums))
#unlike the index of the items, len does not start with 0. 
#so, the list above contains 5 items, meaning len will return 5
#len is written before the list it is being called on, without a dot 

#given a list, calculate the middle elements index 
items = [2, 4, 6, 8, 10, 12, 14]
print(len(items)//2)

#the insert method is similar to append, esxcept that it allows you to insert a new item at any position in the list, as opposed to just at the end 
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words) 
#elements, that are after the inserted item, are shifted to the right

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))

#The index method finds the first occurrence of a list item and return its index 
#if the item isnt in the list it raises a valueError
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
#print(letters.index('z'))

# There are a few more useful functions and methods for lists.
# max(list): Returns the list item with the maximum value
# min(list): Returns the list item with minimum value
# list.count(item): Returns a count of how many times an item occurs in a list
# list.remove(item): Removes an object from a list
# list.reverse(): Reverses items in a list.
print(letters.count('p'))
print(max(letters))
print(letters.reverse())