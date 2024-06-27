class Stack:
  def __init__(self, data:list):
    self.data = data
    self.top = 0
    self.len = 0
  def push(self, value):
    self.data.append(value) 
    self.top += 1
    self.len += 1
  def pop(self):
    if self.len == 0:
      return None
    temp = self.data[self.top - 1]  
    self.data = self.data[:-1]
    self.top -= 1
    self.len -= 1
    return temp
  def peek(self):
    if self.len == 0:
      return None
    return self.data[self.top - 1]
  def __len__ (self):
    return self.len
  def __repr__ (self):
    return str(self.data)
  def isEmpty(self):
    return self.len == 0

pila = Stack([])
pila.push(1)
pila.push(2)
pila.push(3)
pila.pop()
print(pila.__len__())
print(pila.peek())

