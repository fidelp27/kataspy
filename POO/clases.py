class Currency:
  def __init__(self, name, symbol, factor):
    self.name = name
    self.symbol = symbol
    self.factor = factor
  
  def convert_amount_to_base_currency(self, amount):
    return amount * self.factor

  def convert_amount_from_base_currency(self, amount):
    return amount / self.factor  
  
  def __repr__(self):
    return f"{self.name}"

class Money:
  def __init__(self, amount:float, currency:Currency):
    self.amount = amount
    self.currency = currency

  def base_currency_amount(self):
    return self.currency.convert_amount_to_base_currency(self.amount)

  def __add__(self, amount_operation):
    amount = self.base_currency_amount() + amount_operation.base_currency_amount()
    amount = self.currency.convert_amount_from_base_currency(amount)
    return Money(amount, self.currency)

  def __sub__(self, amount_operation):
    amount = self.base_currency_amount() - amount_operation.base_currency_amount()
    amount = self.currency.convert_amount_from_base_currency(amount)
    return Money(amount, self.currency)

  def __mul__(self, amount_operation):
    return Money(self.amount * amount_operation, self.currency)

  def __truediv__ (self, amount_operation):
    return Money(self.amount / amount_operation, self.currency)
    
    
  def __repr__(self):
    return f"{self.currency.symbol}{self.amount}"

dolar = Currency("Dolar", "$", 1)
euro = Currency("Euro", "€", 0.9)
one_dollar = Money(1, dolar)
one_euro = Money(1, euro)
print(one_dollar + one_euro)
print(one_dollar - one_euro)
print(one_dollar * 3)
print(one_dollar / 2)