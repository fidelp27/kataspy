'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "########################
'''
import re
def maskify(cc):
  if len(cc) <= 4:
    return cc
  else:
    return "#" * (len(cc) - 4) + cc[-4:]

def maskify2(cc):
  return re.sub(r'.(?=.{4})', '#', cc)


print(maskify("4556364607935616"))
print(maskify2("4556364607935616"))