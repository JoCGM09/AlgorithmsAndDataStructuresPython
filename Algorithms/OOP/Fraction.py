# Function GCD (Greatest common divisor) with Euclid's Algorithm
def gcd(m,n):
  while m % n != 0:
    old_m = m
    old_n = n

    m = old_n
    n = old_m % old_n
  return n

#Define a class
class Fraction:
  # Constructor
  def __init__(self, m, n):
    self.num = m
    self.den = n

  # toString method (override)
  def __str__(self):
    return str(self.num) + '/' + str(self.den)

  # add method (override)
  def __add__(self, other_fraction):
    new_num = self.num*other_fraction.den + self.den*other_fraction.num
    new_den = self.den*other_fraction.den
    common = gcd(new_num, new_den)
    return Fraction(new_num//common,new_den//common)

  # equals method
  def __eq__(self, other):
    first_num = self.num * other.den
    second_num = self.den * other.num
    return first_num == second_num


fraction1 = Fraction(3,5)
fraction2 = Fraction(6,5)
print(fraction1.__add__(fraction2))