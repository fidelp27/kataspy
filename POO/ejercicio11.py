'''
Sistema de Gestión de Bibliotecas Mejorado
Enunciado:
Mejora el sistema de gestión de bibliotecas para incluir categorías de libros y usuarios con diferentes roles.

Clase Libro: con atributos titulo, autor, categoria, y disponible. Métodos:

prestar(): cambia el estado de disponible a False.
devolver(): cambia el estado de disponible a True.
__str__(): devuelve una cadena con la información del libro.
Clase Usuario: con atributos nombre, rol (puede ser "lector" o "bibliotecario"), y libros_prestados (lista de libros prestados). Métodos:

prestar_libro(libro): agrega un libro a libros_prestados si está disponible.
devolver_libro(libro): elimina un libro de libros_prestados y lo devuelve a la biblioteca.
Clase Biblioteca: con un atributo catalogo (lista de libros). Métodos:

agregar_libro(libro): agrega un libro al catálogo (solo si el usuario es "bibliotecario").
mostrar_libros_disponibles(): imprime todos los libros disponibles.
mostrar_libros_por_categoria(categoria): imprime todos los libros disponibles de una categoría específica.
'''