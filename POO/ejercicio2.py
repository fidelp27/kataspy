"""
Ejercicio 2: Clase Círculo
Enunciado: Crea una clase Circulo que tenga un atributo radio. La clase debe tener métodos para calcular el área y la circunferencia del círculo. Usa las siguientes fórmulas:

Área:  
𝜋 × 𝑟𝑎𝑑𝑖𝑜2

Circunferencia: 
2 × π × radio
"""
import math 

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def area(self):
    return math.pi * self.radio ** 2

  def circunferencia(self):
    return (2 * math.pi * self.radio)

circulo = Circulo(85)
print(f"Área: {circulo.area():.2f}") 
print(f"Circunferencia: {circulo.circunferencia():.2f}")