"""
Ejercicio 1: Sistema de Gestión de Biblioteca
Enunciado:
Crea un sistema de gestión de biblioteca con las siguientes clases y características:

Clase Libro: con atributos titulo, autor, y disponible (booleano). Métodos:

prestar(): cambia el estado de disponible a False.
devolver(): cambia el estado de disponible a True.
__str__(): devuelve una cadena con la información del libro.

Clase Usuario: con atributos nombre y libros_prestados (lista de libros prestados). Métodos:

prestar_libro(libro): agrega un libro a libros_prestados si está disponible.
devolver_libro(libro): elimina un libro de libros_prestados y lo devuelve a la biblioteca.

Clase Biblioteca: con un atributo catalogo (lista de libros). Métodos:

agregar_libro(libro): agrega un libro al catálogo.
mostrar_libros_disponibles(): imprime todos los libros disponibles.
"""
class Libro:
  def __init__(self, titulo: str, autor: str, disponible:bool):
    self.titulo = titulo
    self.autor = autor
    self.disponible = disponible
  def prestar(self):
    self.disponible = False
  def devolver(self):
    self.disponible = True
  def __str__(self):
    return f"Título: {self.titulo}, Autor: {self.autor}, Disponible:{self.disponible}"
  def __repr__(self) -> str:
    return f"Libro({self.titulo}, {self.autor}, {self.disponible})"

class Usuario:
  def __init__(self, nombre: str):
    self.nombre = nombre
    self.libros_prestados = []
  def prestar_libro(self, libro: Libro):
    if libro.disponible:
      self.libros_prestados.append(libro)
      libro.prestar()
      print(f"El libro '{libro.titulo}' ha sido prestado a {self.nombre}.")
    else:
      print(f"El libro '{libro.titulo}' no está disponible para préstamo.")
  def devolver_libro(self, libro: Libro):
    if libro in self.libros_prestados:
      self.libros_prestados.remove(libro)
      libro.devolver()
      print(f"El libro '{libro.titulo}' ha sido devuelto a la biblioteca.")

class Biblioteca:
  def __init__(self):
    self.catalogo = []
  def agregar_libro(self, libro:Libro):
      self.catalogo.append(libro)
  def libros_disponibles(self):
    libros_disponibles = [libro for libro in self.catalogo if libro.disponible]
    print("Libros disponibles:")
    for libro in libros_disponibles:
      print(libro)
  def libros_no_disponibles(self):
    libros_no_disponibles = [libro for libro in self.catalogo if not libro.disponible]
    print("Libros no disponibles:")
    for libro in libros_no_disponibles:
      print(libro)

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", True)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", True)
libro3 = Libro("1984", "George Orwell", True)
libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", True)
libro5 = Libro("Un mundo felz", "Aldous Huxley", True)


biblio = Biblioteca()
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
biblio.agregar_libro(libro3)
biblio.agregar_libro(libro4)
biblio.agregar_libro(libro5)
usuario1 = Usuario("Juan")
usuario1.prestar_libro(libro1)
usuario2 = Usuario("Fidel")
usuario2.prestar_libro(libro5)
usuario2.prestar_libro(libro1)
usuario2.prestar_libro(libro3)
usuario1.devolver_libro(libro1)
usuario2.prestar_libro(libro1)

biblio.libros_disponibles()
biblio.libros_no_disponibles()



    
    