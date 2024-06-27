"""
Ejercicio 3: Clase Rectángulo
Enunciado: Crea una clase Rectangulo que tenga los atributos ancho y alto. La clase debe tener métodos para calcular el área y el perímetro del rectángulo. Usa las siguientes fórmulas:

Área: 
ancho × alto
Perímetro: 
2 × (ancho + alto)
"""
class Rectangulo:
  def __init__(self, ancho, alto):
    self.ancho = ancho
    self.alto = alto
  def area(self):
    return self.ancho * self.alto
  def perimetro(self):
    return 2 * (self.ancho + self.alto)