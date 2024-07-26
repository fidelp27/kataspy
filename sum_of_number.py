'''
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.
'''
#Forma 1
def getSum(a, b):
  if a == b:
      return a
  if a > b:
      return sum(range(b, a + 1))
  else:
      return sum(range(a, b + 1))

#Forma 2
def getSum2(a, b):
  minimo = min(a,b)
  maximo = max(a,b)
  return (maximo - minimo +1)*(minimo + maximo) / 2

print(getSum(-1,2))
print(getSum2(-1,2)) 
  