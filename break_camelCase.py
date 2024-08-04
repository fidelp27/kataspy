'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''
import re


def solution(string):
  return ' '.join(re.split(r'(?=[A-Z])' , string))

print(solution('camelCase'))
