
def menu_uno():
    contador=0
    if contador<=1:
        contador+=2
        print("""
Bienvenidos a la Plataforma de MisiónTIC 2022
[1] para Ingresar
[2] para Registrarme
[3] para Salir
""")
    opcion = input("Igrese la Accion que desea realizar: ")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion > 0 and opcion <= 3:
            
            return opcion
    else:
        print("Datos invalidos intenetlo de nuevo")
        menu_uno()


def menu_dos():
    print("""
    [1] para Modificar o actualizar estudiante
    [2] para Eliminar estudiante
    [3]Ordenar lista de estudiantes(Numero de documento o por Nonbre o apellidos)
    [4]Buscar estudiante por nombre, apellido, documento
    [5]Realizar gráficas por edad y ciclo
    """)
    opcion = input("Igrese la Accion que desea realizar: ")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion > 0 and opcion <= 5:
            return opcion
    else:
        print("Datos invalidos intenetlo de nuevo")
        menu_uno()

def menu_tres():
    print("""
Puedes realizar un grafico po Edad y Por Ciclo
[1] para Edad
[2] para Ciclo
""")
    opcion = input("Igrese la Accion que desea realizar: ")
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion > 0 and opcion <= 2:
            return opcion
    else:
        print("Datos invalidos intenetlo de nuevo")
        menu_tres()
