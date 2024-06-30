'''
Sistema de Gestión de Hospital
Enunciado:
Crea un sistema de gestión de hospital con las siguientes clases y características:

Clase Persona: con atributos nombre, edad, y género. Métodos:

__str__(): devuelve una cadena con la información de la persona.

Clase Paciente (subclase de Persona): con atributos adicionales enfermedad y habitación. Métodos:

asignar_habitación(habitación): asigna una habitación al paciente.
actualizar_enfermedad(nueva_enfermedad): actualiza la enfermedad del paciente.
Clase Doctor (subclase de Persona): con atributos adicionales especialidad y pacientes (lista de pacientes). Métodos:

agregar_paciente(paciente): agrega un paciente a la lista de pacientes del doctor.
eliminar_paciente(paciente): elimina un paciente de la lista de pacientes del doctor.
mostrar_pacientes(): imprime todos los pacientes del doctor.
'''
class Persona:
  def __init__(self, nombre, edad, genero):
    self.nombre = nombre
    self.edad = edad
    self.genero = genero
  def __str__(self):
    return f"Nombre: {self.nombre}, Edad: {self.edad}, Género:{self.genero}"

class Paciente(Persona):
  def __init__(self, nombre, edad, genero, enfermedad, habitacion):
    super().__init__(nombre, edad, genero)
    self.enfermedad = enfermedad
    self.habitacion = habitacion
  def asignar_habitacion(self, habitacion):
    self.habitacion = habitacion
  def actualizar_enfermedad(self, nueva_enfermedad):
    self.enfermedad = nueva_enfermedad
  def __str__(self):
    return f"{super().__str__()}, Enfermedad: {self.enfermedad}, Habitación: {self.habitacion}"

class Doctor(Persona):
  def __init__(self, nombre, edad, genero, especialidad):
    super().__init__(nombre, edad, genero)
    self.especialidad = especialidad
    self.pacientes = []
  def agregar_paciente(self, paciente):
    self.pacientes.append(paciente)
  def eliminar_paciente(self, paciente):
    self.pacientes.remove(paciente)
  def mostrar_pacientes(self):
    for paciente in self.pacientes:
      print(paciente)


paciente1 = Paciente("Pedro", 40, "Masculino", "Asma", 1)
paciente2 = Paciente("Ana", 35, "Femenino", "Diabetes", 2)
paciente3 = Paciente("Luis", 45, "Masculino", "Hipertensión", 3)
doctor1 = Doctor("Juan", 50, "Masculino", "Cardiología")
doctor1.agregar_paciente(paciente1)
doctor1.agregar_paciente(paciente2)
doctor1.agregar_paciente(paciente3)
paciente3.actualizar_enfermedad("Asma")
doctor1.mostrar_pacientes()