'''

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

'''

def createPhoneNumber(numbers):
  parte1 = "".join(numbers[0:3])
  parte2 = "".join(numbers[3:6])
  parte3 = "".join(numbers[6])
  return f"({parte1}) {parte2}-{parte3}"  
  