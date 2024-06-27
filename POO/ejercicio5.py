"""
Ejercicio 5: Clase Vehículo y Subclases
Enunciado: Crea una clase base Vehiculo con atributos marca y modelo, y un método moverse que imprima "El vehículo se está moviendo". 
Luego, crea dos subclases Coche y Bicicleta. 
La clase Coche debe tener un atributo adicional combustible y un método repostar que imprima "El coche está repostando". 
La clase Bicicleta debe tener un atributo adicional tipo (montaña, carretera) y un método pedalear que imprima "La bicicleta está pedaleando".
"""
class Vehiculo:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  def moverse(self):
    print("El vehículo se está moviendo")

class Coche(Vehiculo):
  def __init__(self, marca, modelo, combustible):
    super().__init__(marca, modelo)
    self.combustible = combustible
  def repostar(self):
    print("El coche está repostando")

class Bicicleta(Vehiculo):
  def __init__(self, marca, modelo, tipo):
    super().__init__(marca, modelo)
    self.tipo = tipo
  def pedalear(self):
    print("La bicicleta está pedaleando")