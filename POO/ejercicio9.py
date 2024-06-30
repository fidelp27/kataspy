'''
Sistema de Gestión de Cursos
Enunciado:
Crea un sistema de gestión de cursos con las siguientes clases y características:

Clase Curso: con atributos nombre, código, y estudiantes (lista de estudiantes). Métodos:

agregar_estudiante(estudiante): agrega un estudiante a la lista de estudiantes.
eliminar_estudiante(estudiante): elimina un estudiante de la lista de estudiantes.
mostrar_estudiantes(): imprime la información de todos los estudiantes inscritos en el curso.


Clase Estudiante: con atributos nombre, matrícula, y cursos (lista de cursos). Métodos:

inscribirse_curso(curso): agrega un curso a la lista de cursos y al estudiante a la lista de estudiantes del curso.
retirarse_curso(curso): elimina un curso de la lista de cursos y al estudiante de la lista de estudiantes del curso.
mostrar_cursos(): imprime la información de todos los cursos en los que está inscrito el estudiante.
'''
class Curso:
  def __init__(self, nombre, codigo):
    self.nombre = nombre
    self.codigo = codigo
    self.lista = []
  def agregar_estudiante(self, estudiante):
    self.lista.append(estudiante)
  def eliminar_estudiante(self, estudiante):
    self.lista.remove(estudiante)
  def mostrar_estudiantes(self):
    for estudiante in self.lista:
      print(estudiante)
  def __str__(self):
    return f"Nombre: {self.nombre}, Código: {self.codigo}, Estudiantes:{self.lista}"

class Estudiante:
  def __init__(self, nombre, matricula):
    self.nombre = nombre
    self.matricula = matricula
    self.cursos = []
  def inscrbirse_curso(self, curso):
    self.cursos.append(curso)
    curso.agregar_estudiante(self)
  def retirarse_curso(self, curso):
    self.cursos.remove(curso)
    curso.eliminar_estudiante(self)
  def mostrar_cursos(self):
    for curso in self.cursos:
      print(curso)
  def __str__(self):
    return f"Nombre: {self.nombre}, Matrícula: {self.matricula}, Cursos:{self.cursos}"