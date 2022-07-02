
from collections import namedtuple
import new_student as nw
import menu as mn

def student(opcion):
    
    Estudiante = namedtuple('Estudiante', [
                            'documento', 'genero', 'nombres', 'apellidos', 'correo', 'fecha_nacimiento', 'ciclo'])
    luis = Estudiante('515684874', 'masculino', 'Luis', 'alvares',
                      'luis@gmail.com', '05/03/1960', 2)
    Eduardo = Estudiante('45894562', 'masculino', 'Eduardo', 'Cantillo',
                         'cantillo@hotmail.com', '15/05/1980', 2)
    Ana = Estudiante('35668954', 'femenino', 'Ana', 'Gomes',
                     'ana@gmail.com', '13/08/1999', 3)
    Milena = Estudiante('1689747412', 'femenino', 'Milena', 'Mancilla',
                        'milena@gmail.com', '05/11/2000', 1)
    student = [luis, Eduardo, Ana, Milena]

    if opcion == 1:
        op = mn.menu_dos()
        return student,op 
    elif opcion == 2:
        new_student = nw.new_student()
        if len(new_student) > 0:
            student = [luis, Eduardo, Ana, Milena, new_student]
            print(student)
            op = mn.menu_dos()
            return student,op
    elif opcion == 3:
        exit(0)








