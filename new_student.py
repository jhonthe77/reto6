
from collections import namedtuple
def new_student():
    documento = input("Ingrese su Cédula: ")
    genero = input("Ingrese su género: ")
    nombre = input("Ingrese su nombre: ")
    apellidos = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento: ")
    ciclo = input("Ingrese el ciclo al que pertenece: ")
    if ciclo.isdigit():
        ciclo=int(ciclo)
        if ciclo>0 and ciclo<=4:
         Estudiante = namedtuple('Estudiante', [
                            'documento', 'genero', 'nombres', 'apellidos', 'correo', 'fecha_nacimiento', 'ciclo'])
         new_student=Estudiante(documento,genero,nombre,apellidos,correo,fecha_nacimiento,ciclo)
         return new_student

