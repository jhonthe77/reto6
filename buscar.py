
def buscar(lista):
    oc = input("""
        Puedes Buscar un estudiante por Nombre, Apellido, Documento
        [1] para nombre 
        [2] para Apellido
        [3] para Documento
        """)
    if oc.isdigit():
        oc = int(oc)
        if oc > 0 and oc <= 3:
            for i in range(len(lista)-1):
                if oc == 1:
                    nombre = input("cual es tu nombre: ")
                if lista[i].nombres == nombre:
                    print(lista[i])
                    break
                if oc == 2:
                    apellido = input("Ingrese su apellido: ")
                if lista[i].apellidos == apellido:
                    print(lista[i])
                    break
                if oc == 3:
                    documento = input("Ingrese su Cédula: ")
                if lista[i].documento == documento:
                    print(lista[i])
                    break


