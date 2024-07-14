'''
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def evenOrOdd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

#Forma 2
def evenOrOdd2(number):
  return "Even" if number % 2 == 0 else "Odd"

