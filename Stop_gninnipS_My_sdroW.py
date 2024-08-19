'''
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"
'''

def spinWords(string):
  return " ".join([word[::-1] if len(word)>4 else word for word in string.split()])

print(spinWords("Hey fellow warriors")) 

def spinWords2(string):
  return " ".join(list(map(lambda x:x[::-1] if len(x)>4 else x, string.split())))

print(spinWords2("Hey fellow warriors")) 
