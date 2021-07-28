def fill_matrix(x,filas):
	for i in range(filas):
		j=0
		x[i][j]=input("\nIngrese el nombre de la empresa: ")
		x[i][j+1]=input(f"\nIngrese el código de la empresa {x[i][j]}: ")
		x[i][j+2]=input(f"\nIngrese las visitas del website de la empresa {x[i][j]} del día Lunes: ")
		x[i][j+3]=input(f"\nIngrese las visitas del website de la empresa {x[i][j]} del día Martes : ")
		x[i][j+4]=input(f"\nIngrese las visitas del website de la empresa {x[i][j]} del día Miércoles: ")
		x[i][j+5]=input(f"\nIngrese las visitas del website de la empresa {x[i][j]} del día Jueves: ")
		x[i][j+6]=input(f"\nIngrese las visitas del website de la empresa {x[i][j]} del día Viernes: ")
	return x

def total_amount(x,filas):
    for i in range(filas):
        suma = 0
        for j in range(2,7):
            suma = suma + float(x[i][j])
        print(f"La cantidad de sitios web visitados semanalmente por la empresa {x[i][j]} son {suma}")
    return total_amount
  
def lunes(x,filas):
    lunes = 0
    for i in range(filas):
        lunes += int(x[i][2])
    return lunes
    
def martes(x,filas):
    martes = 0
    for i in range(filas):
        martes += int(x[i][3])
    return martes
    
def miercoles(x,filas):
    miercoles = 0
    for i in range(filas):
        miercoles += int(x[i][4])
    return miercoles
    
def jueves(x,filas):
    jueves = 0
    for i in range(filas):
        jueves += int(x[i][5])
    return jueves
    
def viernes(x,filas):
    viernes = 0
    for i in range(filas):
        viernes += int(x[i][6])
    return viernes
    

def modify_matrix(x,filas):
	j=1
	cod=input("Ingrese el código de la empresa que desea modificar: ")
	nombre=input("Ingrese el nombre de la empresa que desea modificar")
	for i in range(filas):
		if x[i][0]==cod or x[i][0]==nombre:
			x[i][j]=input(f"Ingrese el nombre de la empresa {x[i][j]}: ")
			x[i][4]=input(f"Ingrese la visitas de la empresa {x[i][j]}: ")
	print(f"El nuevo nombre de la empresa es {x[i][j]} y el nuevo numero de visitas es {x[i][4]}")
	return modify_matrix
	
	
def promedio_jueves (x,filas):
    suma = 0
    for i in range(filas):
        suma = suma + float(x[i][5])
    promedio = suma / filas
    return promedio
    
def promedio_viernes (x,filas):
    suma = 0
    for i in range(filas):
        suma = suma + float(x[i][5])
    promedio2 = suma / filas
    return promedio2

    

