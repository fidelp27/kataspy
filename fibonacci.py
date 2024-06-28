def fibonacci(a,b,range):
  i = 0
  sequence = [a,b]
  while i < range - 2 :
    sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2 ])
    i+=1
  return sequence

print(fibonacci(10,20,5))