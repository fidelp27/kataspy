'''
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
'''
#forma 1
def positiveSum(arr):
  sum = 0
  for elem in arr:
    if elem > 0:
      sum = sum + elem
  return sum

#forma 2
def positiveSum2(arr):
  return sum(filter(lambda x: x > 0, arr))

#forma 3
def positiveSum3(arr):
  return sum([elem for elem in arr if elem > 0])