
def modificar_student(lista):
    nombre = input("cual es tu nombre: ")
    for i in range(len(lista)):
        if lista[i].nombres == nombre:
            listan = [lista[i]]
            print(f"""
                  {nombre} puedes modificar los siguentes datos
                  [1]para genero
                  [2]para correo
                  [3]para ciclo""")
            opcion = input("Igrese la Accion que desea realizar: ")
            if opcion.isdigit():
                opcion = int(opcion)
                lis = [opcion == 1, opcion == 2, opcion == 3]
                llamar = []
                modificar = []
                li = []
                for k in range(len(listan)):
                    for j in range(len(lis)):
                        if lis[j] and j == 0:
                            genero = input("Ingrese su nuevo género: ")
                            modificar.append(genero)
                            llamar.append(listan[k]._replace(genero=genero))
                            li.append(listan[k].genero)
                        elif lis[j] and j == 1:
                            correo = input(
                                "Ingrese su nuevo correo electrónico: ")
                            modificar.append(correo)
                            llamar.append(listan[k]._replace(correo=correo))
                            li.append(listan[k].correo)
                        elif lis[j] and j == 2:
                            ciclo = [
                                input("Ingrese el nuevo ciclo al que pertenece: ")]
                            modificar.append(ciclo)
                            llamar.append(listan[k]._replace(ciclo=ciclo))
                            li.append(listan[k].ciclo)

                    listan[k] = llamar[k] if li[k] != modificar[k] else listan[k]
                    lista.pop(k)
                    lista.insert(k, listan[k])
                    print(lista[k])
