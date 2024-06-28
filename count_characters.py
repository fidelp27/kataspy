'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''

def counting(string):
  if len(string) == 0: 
    return {}
  else:
    return {letter:string.count(letter) for letter in list(string)}

print(counting("aba"))