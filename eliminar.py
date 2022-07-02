
def eliminar(lista):
    nombre = input("cual es tu nombre: ")
    for i in range(len(lista)):
        if lista[i].nombres == nombre:
            lista.pop(i)
            print(lista)
            break
    
       
            

