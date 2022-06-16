#list operations
#the item at a certain index in a list can be reassigned 
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print( nums )
#you can replace the item with an item of a different type

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

#lists can be added and multiplied in the same way as strings
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3) 

#to check if an item is in a list, the in operator can be used
# it returns True if the item occurs one or more times in the list, and False if it doesnt 
print(2 in nums )
print(4 in nums)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
#the in operator is also used ot determine whether or not a string is a substring of another string

#practice: 
items = [42, 88, 721, 12, 43, 22, 908]

num = int(input())
if num in items: 
    print("bingo")

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])

#to check if an item is not in a list, you can use the not operator in one of the following ways: 
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums) 