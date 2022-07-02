#No se visualiza las graficas 4.3
import lista_user as ls
import modificar as md
import eliminar as el
import ordenar as od
import buscar as bc
import graficos as gf
import menu as mn
def main():
    oc=mn.menu_uno()
    lista, opcion = ls.student(oc)
    while True: 
        if opcion == 1:
          md.modificar_student(lista)
          main()
          
        elif opcion == 2:
            el.eliminar(lista)
            main()
        elif opcion == 3:
            od.ordenar(lista)
            main()
        elif opcion == 4:
            bc.buscar(lista)
            main()
        elif opcion == 5:
            gf.grafico(lista)
            main()

main()

