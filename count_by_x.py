'''
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]
countBy(2,5) === [2,4,6,8,10]
'''
# forma 1
def countBy(x, n):
  z = []
  counter = 1
  while counter <= n:
    z.append(x * counter)
    counter += 1
  return z

# forma 2
def countBy2(x, n):
  z = [x * elem for elem in range(1,n+1)]
  print(z)
  return z

