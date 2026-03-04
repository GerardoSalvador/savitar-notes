#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Libro:

    def __init__(self, id, autor, titulo):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.esta_prestado = False

    def __str__(self):
        return f"Libro({self.id},{self.autor}, {self.titulo}, {self.esta_prestado})"
    
    def __repr__(self):
        return self.__str__()
    
class Biblioteca:
    
    def __init__(self):
        self.libros = {} # {1 : Libro(1, "Gerardo Salvador", "El mundo de sofia")}
    
    def agregar_libro(self, libro):
        if libro.id not in self.libros:
            self.libros[libro.id] = libro
        else:
            print(f"\n[!] No es posible agregar el libro con ID {libro.id_libro}")

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n[!] No es posible prestar el libro con ID {id_libro}")

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.esta_prestado]
    
class BibliotecaInfantil(Biblioteca):
    
    def __init__(self):
        super().__init__()
        self.libros_para_ninos = {} # -> {1:True, 2:False, 3:True}

    def agregar_libro(self, libro, es_para_ninos):
        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id] = es_para_ninos

    def prestar_libro(self, id_libro, es_para_ninos):
        if id_libro in self.libros and self.libros_para_ninos[id_libro] == es_para_ninos and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n[!] No es posible prestar el libro con ID {id_libro}")
    
    @property
    def mostrar_estado_libros_para_ninos(self):
        return self.libros_para_ninos

if __name__ == '__main__':

    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1, "Gerardo Salvador", "El mundo de sofia")
    libro2 = Libro(2, "Gerardo Python", "Como ser un lammer")
    libro3 = Libro(3, "Gerardo", "Aprende a colorear desde cero")

    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=False)
    biblioteca.agregar_libro(libro3, es_para_ninos=True)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    biblioteca.prestar_libro(1, es_para_ninos = False)

    biblioteca.prestar_libro(1, es_para_ninos=True)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    print(f"\n[+] Libros prestados: {biblioteca.mostrar_libros_prestados}")

    print(f"\n[+] Libros para niños: {biblioteca.mostrar_estado_libros_para_ninos}")