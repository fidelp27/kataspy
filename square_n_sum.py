'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
'''
#forma 1
def squareSum(numbers):
  return sum([elem**2 for elem in numbers])

#forma 2
def squareSum2(numbers):
  return sum(map(lambda x: x**2, numbers))

#forma 3
def squareSum3(numbers):
  return sum(x**2 for x in numbers)

