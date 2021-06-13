# E1. Get an array with all the letters of the elements in word_list
# word_list = ['cat','dog','rabbit']
# letter_list = [ ]
# for a_word in word_list:
#   for a_letter in a_word:
#     letter_list.append(a_letter)
# print(letter_list)
## 1. Modify the given code so that the final list only contains a single copy of each letter
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
  for a_letter in a_word:
    if a_letter not in letter_list:
      letter_list.append(a_letter)
print(letter_list)
## 2. Redo using list comprehensions
word_list_2 = ['cat','dog','rabbit']
letter_list_2 = [a_letter_2 for a_word_2 in word_list_2 for a_letter_2 in a_word_2]
print(letter_list_2)