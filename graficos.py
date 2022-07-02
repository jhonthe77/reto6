
import menu as mn
import datetime as dt
from datetime import datetime
import matplotlib.pyplot as plt
def grafico(lista):
    op=mn.menu_tres()
    if len(lista)==4:
      lista_expl = (0.1, 0.1, 0.1, 0.1)
    elif len(lista) == 5:
        lista_expl = (0.1, 0.1, 0.1, 0.1,0.1)
    nombre = input("cual es tu nombre: ")
    for k in range(len(lista)):
        if lista[k].nombres == nombre:
            lista_eda = []
            nombre = []
            lista_ciclo=[]
            dates = dt.date.today()
            year = dates.strftime("%Y")
            year = int(year)
            agos = []
            for i in range(len(lista)):
                nombre.append(lista[i].nombres)
                lista_eda.append(datetime.strptime(
                    lista[i].fecha_nacimiento, '%d/%m/%Y'))
                lista_ciclo.append(lista[i].ciclo)
                dates = lista_eda[i]
                agos.append(year-int(dates.strftime("%Y")))

            if op==1:
                plt.title("Grafico de Edades")
                plt.pie(agos, labels=nombre, autopct='%0.1f %%',
                     explode=lista_expl)
                plt.show()
            elif op==2:
                plt.title("Grafico de Ciclos")
                plt.pie(lista_ciclo, labels=nombre, autopct='%0.1f %%',
                        explode=lista_expl)
                plt.show()
