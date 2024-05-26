import numpy as np
import sympy as sp
from sympy import symbols, Eq, solve, sqrt
import time

# Función para calcular vector unitario
def vector_unitario(v):
    v_np = np.array(v)
    magnitud = np.linalg.norm(v_np)
    vector_unitario = v_np / magnitud
    return vector_unitario.tolist()

continuar = 'si'

while continuar.lower() == 'si':

    # Programa
    caso = input("Si desea la solución general en términos de W, coloque un 0. Si desea especificar una carga en particular, ingrese su valor en kg con punto decimal: ")

    if caso == '0':
        # Muestra la solución general en términos de W
        
        puntos = {
            'A': np.array([0, 0, 0]),
            'B': np.array([60, 0, 0]),
            'C': np.array([60, 0, -30]),
            'D': np.array([0, 0, 25]),
            'E': np.array([0, 25, 0]),
            'F': np.array([0, 25, -30]),
            'G': np.array([60,0,-15])
        }
        
        print("")
        print("Se inicia definiendo las coordenadas de cada punto")
        print("")
        print("")
        time.sleep(2)
        
        for nombre, coordenadas in puntos.items():
            coordenadas_str = ', '.join(map(str, coordenadas))
            print(f"El punto {nombre} tiene coordenadas [{coordenadas_str}]")
            print("")

        time.sleep(2)

        print("")
        print("Ahora se definen los radios que describen las cuerdas, sus magnitudes y se calcula el vector unitario correspondiente")
        print("")

        #Calculo de radios de interes BD, BE y CF. 
        BD = puntos['D'] - puntos['B']
        BE = puntos['E'] - puntos['B']
        CF = puntos['F'] - puntos['C']


        #Vectores unitarios BDu, BEu y CFu
        BD_u = vector_unitario(BD)
        BE_u = vector_unitario(BE)
        CF_u = vector_unitario(CF)


        print("El radio BD es D - B :" , BD, "de magnitud: ",sqrt(BD[0]**2+BD[1]**2+BD[2]**2),"su vector unitario es BD_u:", BD_u)
        print("")
        print("El radio BE es E - B :" , BE, "de magnitud: ",sqrt(BE[0]**2+BE[1]**2+BE[2]**2),"su vector unitario es BE_u:", BE_u)
        print("")
        print("El radio CF es F - C :" , CF, "de magnitud: ",sqrt(CF[0]**2+CF[1]**2+CF[2]**2),"su vector unitario es CF_u:", CF_u)
        print("")
        print("")


        #Definicion de la magnitud de las tensiones Tbd, Tbe, Tcf y la carga
        Tbd, Tbe, Tcf , W= sp.symbols('Tbd Tbe Tcf W')

        #Creacion de vectores: Se multiplican los vectores unitarios por las variables correspondientes.
        #La carga tambien se define en forma vectorial
        Tbd_Vector = np.array(BD_u) * Tbd
        Tbe_Vector = np.array(BE_u) * Tbe
        Tcf_Vector = np.array(CF_u) * Tcf
        W_Vector = np.array([0, -W, 0])

        print("El vector de tension Tbd es: Tbd * BD_u:", Tbd_Vector)  
        print("")
        print("El vector de tension Tbe es: Tbe * BE_u:", Tbe_Vector)  
        print("")
        print("El vector de tension Tcf es: Tcf * CF_u:", Tcf_Vector)  
        print("")
        print("El vector de la carga W es:", W_Vector)  
        print("")
        print("")


        #Calculo de productos cruz para los momentos respecto al punto A. puesto que A es el origen, los vectores de
        #posicion respecto a A son identicos a las coordenadas del punto correspondiente
        momento_bd = np.cross(puntos['B'], Tbd_Vector)
        momento_be = np.cross(puntos['B'], Tbe_Vector)
        momento_cf = np.cross(puntos['C'], Tcf_Vector)
        momento_carga = np.cross(puntos['G'], W_Vector)


        #Se aplica sumatoria de momentos igual a cero para cada componente de la ecuacion

        Sum_Momentos_A = momento_bd + momento_be + momento_cf + momento_carga

        Sum_Momentos_Ax = Eq(Sum_Momentos_A[0], 0)
        Sum_Momentos_Ay = Eq(Sum_Momentos_A[1], 0)
        Sum_Momentos_Az = Eq(Sum_Momentos_A[2], 0)

        print("Los momentos respecto al punto A son: Momento BD=>", momento_bd, "Momento BE =>", momento_be, "Momento_cf =>", momento_cf)
        print("")
        print("Aplicando sumatoria de momentos con respecto a A:  En x:", Sum_Momentos_Ax, "En y:", Sum_Momentos_Ay, "En z:", Sum_Momentos_Az)
        print("")
        print("")
        
        #Se resuelve el sistema de ecuaciones
        tensiones = solve((Sum_Momentos_Ax, Sum_Momentos_Ay, Sum_Momentos_Az), (Tbd, Tbe, Tcf))

        print("Al resolver el sistema, se obtiene la solución para Tbd, Tbe y Tcf en términos de W:", tensiones)

        #Redefinicion de la magnitud de la tension en cada cable en terminos de la carga

        Tbd_sol=tensiones[Tbd]
        Tbe_sol=tensiones[Tbe]
        Tcf_sol=tensiones[Tcf]

        #Redefinicion de los vectores de las tensiones en los cables en terminos de la carga
        Tbd_Vector_sol = np.array(BD_u) * Tbd_sol
        Tbe_Vector_sol = np.array(BE_u) * Tbe_sol
        Tcf_Vector_sol = np.array(CF_u) * Tcf_sol
        
        print("")
        print("")
        print("Se redefinen los vectores de tension como: Tbd =>", Tbd_Vector_sol, "Tbe =>", Tbe_Vector_sol, "Tcf =>", Tcf_Vector_sol)
        print("")
        print("")
        #Definicion de las componentes de reaccion en A
        Ax, Ay, Az = sp.symbols('Ax Ay Az')

        print("Sean las fuerzas de reaccion Ax, -Ay y -Az; segun el sistema de referencia")
        print("")
        print("")
        
        #Sumatoria de fuerzas en cada eje
        Sum_Fuerzas_x = Eq(Tbd_Vector_sol[0] + Tbe_Vector_sol[0] + Tcf_Vector_sol[0]+ Ax, 0)
        Sum_Fuerzas_y = Eq(Tbd_Vector_sol[1] + Tbe_Vector_sol[1] + Tcf_Vector_sol[1] + W_Vector[1] + Ay, 0)
        Sum_Fuerzas_z = Eq(Tbd_Vector_sol[2] + Tbe_Vector_sol[2] + Tcf_Vector_sol[2] - Az, 0)

        print("Aplicando sumatoria de fuerzas:  En x:", Sum_Fuerzas_x, "En y:", Sum_Fuerzas_y, "En z:", Sum_Fuerzas_z)
        print("")
        print("")

        #Se resuelve el sistema de ecuaciones
        reacciones = solve((Sum_Fuerzas_x, Sum_Fuerzas_y, Sum_Fuerzas_z), (Ax, Ay, Az))

        print("Al resolver el sistema, la solución para Ax, Ay y Az es:", reacciones)
        
    else:
        
        # Calcula datos concretos utilizando el valor de W especificado
        W_valor_kg = float(caso)
        W_valor = W_valor_kg * 9.77744


        puntos = {
            'A': np.array([0, 0, 0]),
            'B': np.array([60, 0, 0]),
            'C': np.array([60, 0, -30]),
            'D': np.array([0, 0, 25]),
            'E': np.array([0, 25, 0]),
            'F': np.array([0, 25, -30]),
            'G': np.array([60,0,-15])
        }
        
        print("")
        print("Se inicia definiendo las coordenadas de cada punto")
        print("")
        print("")
        time.sleep(2)
        
        for nombre, coordenadas in puntos.items():
            coordenadas_str = ', '.join(map(str, coordenadas))
            print(f"El punto {nombre} tiene coordenadas [{coordenadas_str}]")
            print("")

        time.sleep(2)

        print("")
        print("Ahora se definen los radios que describen las cuerdas, sus magnitudes y se calcula el vector unitario correspondiente")
        print("")

        #Calculo de radios de interes BD, BE y CF. 
        BD = puntos['D'] - puntos['B']
        BE = puntos['E'] - puntos['B']
        CF = puntos['F'] - puntos['C']


        #Vectores unitarios BDu, BEu y CFu
        BD_u = vector_unitario(BD)
        BE_u = vector_unitario(BE)
        CF_u = vector_unitario(CF)


        print("El radio BD es D - B :" , BD, "de magnitud: ",sqrt(BD[0]**2+BD[1]**2+BD[2]**2),"su vector unitario es BD_u:", BD_u)
        print("")
        print("El radio BE es E - B :" , BE, "de magnitud: ",sqrt(BE[0]**2+BE[1]**2+BE[2]**2),"su vector unitario es BE_u:", BE_u)
        print("")
        print("El radio CF es F - C :" , CF, "de magnitud: ",sqrt(CF[0]**2+CF[1]**2+CF[2]**2),"su vector unitario es CF_u:", CF_u)
        print("")
        print("")


        #Definicion de la magnitud de las tensiones Tbd, Tbe, Tcf y la carga
        Tbd, Tbe, Tcf = sp.symbols('Tbd Tbe Tcf')

        #Creacion de vectores: Se multiplican los vectores unitarios por las variables correspondientes.
        #La carga tambien se define en forma vectorial y con el valor correspondiente
        Tbd_Vector = np.array(BD_u) * Tbd
        Tbe_Vector = np.array(BE_u) * Tbe
        Tcf_Vector = np.array(CF_u) * Tcf
        
        W_Vector = np.array([0, -W_valor, 0])

        print("El vector de tension Tbd es: Tbd * BD_u:", Tbd_Vector)  
        print("")
        print("El vector de tension Tbe es: Tbe * BE_u:", Tbe_Vector)  
        print("")
        print("El vector de tension Tcf es: Tcf * CF_u:", Tcf_Vector)  
        print("")
        print("El vector de la carga W es:", W_Vector)  
        print("")
        print("")


        #Calculo de productos cruz para los momentos respecto al punto A. puesto que A es el origen, los vectores de
        #posicion respecto a A son identicos a las coordenadas del punto correspondiente
        momento_bd = np.cross(puntos['B'], Tbd_Vector)
        momento_be = np.cross(puntos['B'], Tbe_Vector)
        momento_cf = np.cross(puntos['C'], Tcf_Vector)
        momento_carga = np.cross(puntos['G'], W_Vector)


        #Se aplica sumatoria de momentos igual a cero para cada componente de la ecuacion

        Sum_Momentos_A = momento_bd + momento_be + momento_cf + momento_carga

        Sum_Momentos_Ax = Eq(Sum_Momentos_A[0], 0)
        Sum_Momentos_Ay = Eq(Sum_Momentos_A[1], 0)
        Sum_Momentos_Az = Eq(Sum_Momentos_A[2], 0)

        print("Los momentos respecto al punto A son: Momento BD=>", momento_bd, "Momento BE =>", momento_be, "Momento_cf =>", momento_cf)
        print("")
        print("Aplicando sumatoria de momentos con respecto a A:  En x:", Sum_Momentos_Ax, "En y:", Sum_Momentos_Ay, "En z:", Sum_Momentos_Az)
        print("")
        print("")
        
        #Se resuelve el sistema de ecuaciones
        tensiones = solve((Sum_Momentos_Ax, Sum_Momentos_Ay, Sum_Momentos_Az), (Tbd, Tbe, Tcf))

        print("Al resolver el sistema, se obtiene la solución (en N) para Tbd, Tbe y Tcf:", tensiones)

        #Redefinicion de la magnitud de la tension en cada cable en terminos de la carga

        Tbd_sol=tensiones[Tbd]
        Tbe_sol=tensiones[Tbe]
        Tcf_sol=tensiones[Tcf]

        #Redefinicion de los vectores de las tensiones en los cables en terminos de la carga
        Tbd_Vector_sol = np.array(BD_u) * Tbd_sol
        Tbe_Vector_sol = np.array(BE_u) * Tbe_sol
        Tcf_Vector_sol = np.array(CF_u) * Tcf_sol
        
        print("")
        print("")
        print("Se redefinen los vectores de tension como: Tbd =>", Tbd_Vector_sol, "Tbe =>", Tbe_Vector_sol, "Tcf =>", Tcf_Vector_sol)
        print("")
        print("")
        
        #Definicion de las componentes de reaccion en A
        Ax, Ay, Az = sp.symbols('Ax Ay Az')

        print("Sean las fuerzas de reaccion Ax, -Ay y -Az; segun el sistema de referencia")
        print("")
        print("")
        
        #Sumatoria de fuerzas en cada eje
        Sum_Fuerzas_x = Eq(Tbd_Vector_sol[0] + Tbe_Vector_sol[0] + Tcf_Vector_sol[0]+ Ax, 0)
        Sum_Fuerzas_y = Eq(Tbd_Vector_sol[1] + Tbe_Vector_sol[1] + Tcf_Vector_sol[1] + W_Vector[1] + Ay, 0)
        Sum_Fuerzas_z = Eq(Tbd_Vector_sol[2] + Tbe_Vector_sol[2] + Tcf_Vector_sol[2] - Az, 0)

        print("Aplicando sumatoria de fuerzas:  En x:", Sum_Fuerzas_x, "En y:", Sum_Fuerzas_y, "En z:", Sum_Fuerzas_z)
        print("")

        #Se resuelve el sistema de ecuaciones
        reacciones = solve((Sum_Fuerzas_x, Sum_Fuerzas_y, Sum_Fuerzas_z), (Ax, Ay, Az))

        print("Al resolver el sistema, la solución para Ax, Ay y Az es:", reacciones)
        print("")
        print("")

        continuar = input("¿Desea ingresar otro valor? (si/no): ")

