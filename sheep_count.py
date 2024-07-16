'''

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,
[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]

The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

'''

from functools import reduce


#forma 1
def count_sheeps(sheep):
    return reduce(lambda acc, s: acc + 1 if s else acc, sheep, 0)

#forma 2
def count_sheeps2(sheep):
  count = 0
  for s in sheep:
    if s:
      count += 1
  print(count)
  return count


lista = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

count_sheeps(lista)
count_sheeps2(lista)