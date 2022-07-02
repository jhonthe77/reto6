
def ordenar(lista):
    nombre = input("cual es tu nombre: ")

    for i in range(len(lista)):
        if lista[i].nombres == nombre:
            oc = input(f"""
    {nombre} Puesdes ordenar por Nombre y Documento
    [1] para nombre 
    [2] para Documento
    Igrese la Accion que desea realizar: """)
    if oc.isdigit():
        oc = int(oc)
        if oc == 1:
            print(sorted(lista, key=lambda x: x.nombres))
        elif oc == 2:
            print(sorted(lista, key=lambda x: x.documento))


