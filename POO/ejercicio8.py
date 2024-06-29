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