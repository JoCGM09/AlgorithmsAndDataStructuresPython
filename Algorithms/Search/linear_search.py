"""
- Search algorithm who search a value in a given array by traversing from the first element, till the element is matched, then returns th index of the element, else return -1.
- Is applied on unsorted or unordered lists with a few elements. 
- It has a time comlexity of O(n).
- It is very simple to implementate.
"""

def linear_search(list, target):
  for i in range (0, len(list)):
    if list[i] == target:
      return i
  return -1

def validate(index):
  if index != -1:
    print(f'Target found at index {index}')
  else:
    print("Target not found")   

############ Test ############

numbers = [2,4,6,7,8,13]
result = linear_search(numbers, 7)
result2 = linear_search(numbers, 5)
validate(result)
validate(result2)
