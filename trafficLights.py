'''
You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow
'''

def updateLight(current):
  colors = ['green', 'yellow', 'red']
  indexColor = colors.index(current.lower())
  if indexColor == len(colors) - 1:
    return colors[0]
  return colors[indexColor +1]

print(updateLight('yellow'))