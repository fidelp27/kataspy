"""
Ejercicio 4: Clase Cuenta Bancaria
Enunciado: Crea una clase CuentaBancaria que tenga los atributos titular y saldo. La clase debe tener métodos para depositar dinero (depositar), retirar dinero (retirar) y mostrar el saldo (mostrar_saldo). Asegúrate de que no se pueda retirar más dinero del que hay en el saldo.
"""
class CuentaBancaria:
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo
  def depositar(self, cantidad):
    self.saldo += cantidad
  def retirar(self, cantidad):
    if cantidad > self.saldo:
      return "No se puede retirar más dinero del que hay en el saldo"
    else:
      self.saldo -= cantidad
  def mostrar_saldo(self):
    return f"El saldo de la cuenta de {self.titular} es {self.saldo}"


cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())
cuenta.retirar(2000)
print(cuenta.mostrar_saldo())
cuenta.retirar(700)
print(cuenta.mostrar_saldo())  