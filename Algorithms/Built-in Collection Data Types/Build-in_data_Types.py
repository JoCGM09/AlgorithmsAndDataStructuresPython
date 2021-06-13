# Python built-in collection classes
# 1. LIST: ordered, comma-delimited in square brackets, heterogeneous (i.e., data objects need not all be from rge same class)
my_list = [1, 3, True, 6.4, 'hi']
print(my_list)
# Methods: 
# 1.1 append(item) : adds a new item to the END
# 1.2 instert(position , item): insterts an item at the position given
# 1.3 pop() : REMOVES AND RETURNS the LAST item
# 1.4 pop(i): REMOVES AND RETURNS the i'th item
# 1.5 sort(): Modifies a list to be sorted
# 1.6 reverse(): Reverse order
# 1.7 del a_list[i]: Deletes the ith item
# 1.8 index(item): Returns the index of an item
# 1.9 count(item): Returns the number of occurrences of item 
# 1.10 remove(item): Removes the FIRST ocurrence of item

# 2. STRING: Letters, numbers and symbols called characters. 
my_string = 'My string'
print(my_string)
# Methods:
# 2.1 center(e): String centered in a field of size e
# 2.2 count(item): Returns the number of ocurrences of item in the string 
# 2.3 ljust(e): Returns a string LEFT-JUSTIFIED in a field of size e
# 2.4 lower(): Returns a string in all lowercase
# 2.5 rjust(e): Returns a string right-justified in a field of size e
# 2.6 find(item): Returns the INDEX of ocurrence of item 
# 2.7 split(char): Splits a string into substrings   

# 3. TUPLES: Immutables, cannot be changed, comma-delimited valuesa enclosed in parentheses. 
my_tuple = (2, 4, True, 4.45)
print(my_tuple)

# 4. SET: Unordered collection of data objects, do not allow duplicates, comma-delimited enclosed in curly braces.
my_set = {2,3,5,'hi',False}
print(my_set)
# Methods:
# 4.1 union(set2): Returns a NEW SET with all elements from BOTH sets 
# 4.2 intersection(set2): Returns a NEW SET with only COMMON elements of both sets
# 4.3 diference(set2): Returns a NEW SET with all items form first set not in second 
# 4.4 issubset(set2): Returns a new set with all ELEMENTS of one set are in the other
# 4.5 add(item): Adds an item to the set (in order)
# 4.6 remove(item): Removes item from set  
# 4.7 pop(): Removes an arbitriary element from the set
# 4.8 clear(): Removes all elements

# 5. DICTIONARY: Associated pairs od items, key and value, comma-delimited enclosed in curly braces.set
my_dictionary = {'hi':2, 'hello': 3}
print(my_dictionary)
# Methods:
# 5.1 keys(): Return the list of keys 
# 5.2 values(): Returns the list of values
# 5.3 items(): Returns the key-value pairs
# 5.4 get(k): Returns the value associated with k, none otherwise
# 5.5 get(k, alt): Returns the value associated with k, alt otherwise
