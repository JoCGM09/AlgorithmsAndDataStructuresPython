"""
- Search algorithm who search a value in a given list by looking for the middle of it. If we get a match return the index, else if we do not get a match check whether the element is less or greater than the middle element. If is greater pick the elements on the right and start again, if is less pick the left.  
- Is applied on sorted lists with a lot of elements. 
- It has a time comlexity of O(logn).
- It is very simple to implementate.
"""
# min and max -> Pointers at the beginning and the end of the list zone to check
# step -> Number of steps to catch the target
# middle -> Middle index at the list

def binary_search(list, target):
  min = 0
  max = len(list) - 1
  step = 0

  while min <= max:
    middle = (min + max) // 2

    if list[middle] == target:
      step+=1
      return middle, step 
    elif list[middle] < target:
      step+=1
      min = middle + 1
    else:
      step+=1
      max = middle - 1
  return -1, 0    

def validate(index, step):
  if index != -1:
    print(f'Target found at index {index}, number of steps for search: {step}')
  else:
    print('Target not found')  

############ Test ############

numbers = [2,4,6,7,8,13,16]
numbers2 = [3,4,6,7,8,11]
result1, index1 = binary_search(numbers,7)
result2, index2 = binary_search(numbers, 4)
result3, index3 = binary_search(numbers2, 8)
result4, index4 = binary_search(numbers2, 5)

validate(result1, index1)
validate(result2, index2)
validate(result3, index3)
validate(result4, index4)