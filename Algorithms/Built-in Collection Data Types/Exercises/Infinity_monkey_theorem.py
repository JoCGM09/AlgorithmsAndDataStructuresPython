## A monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

import random

## target string
goal = 'methinks it is like a weasel'


## Function 1: Random string with 28 characters
def random_string():
  all_letters='qwertyuiopasdfghjklzxcvbnm '
  a_string = ''
  for i in range(28):
    a_string += all_letters[random.randrange(27)]
  return a_string

def score(a_string):
  count = 0
  for i in range(28):
    if a_string[i] == goal[i]:
      count+=1
  return count


def generate():
  max = 0
  result = []
  for i in range(10000):
    random_one = random_string()
    if max < score(random_one):
      max = score(random_one)
      result.clear()
      result.append(random_one)
      result.append(max)
  return result

print(generate())


