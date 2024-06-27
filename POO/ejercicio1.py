"""
Ejercicio 1: Clase Persona

Enunciado: Crea una clase Persona que tenga los atributos nombre y edad. La clase debe tener un método presentarse que imprima una presentación en formato: "Hola, me llamo [nombre] y tengo [edad] años."

"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def presentarse(self):
    return f"Hola, me llamo {self.name} y tengo {self.age} años."
