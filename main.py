import numpy as np
import website as boss

print("SISTEMA DE LOGISTICA\n")
filas = int(input("Ingrese la cantidad de registros que llevará a cabo: "))

# Instancias en el main UNA MATRIZ
matrix = np.empty([filas,7],"U10")
print(matrix)
clientes = boss.fill_matrix(matrix,filas)
print(clientes)


menu=("1. CONSULTA DE SITIOS WEB VISITADOS SEMANALMENTE POR  EMPRESA\n\n2. CONSULTA DE SITIOS WEB VISITADOS DIARIAAMENTE\n\n3. MODIFICAR NOMBRE Y NUMEROS DE VISITAS\n\n4. PROMEDIO DE SITIOS VISITADOS POR TODAS LAS EMPRESAS LOS DÍAS JUEVES & VIERNES\n\n5. SALIR ")
while True:
	print(menu)
	opc=int(input("Ingrese una opción: "))
	if(opc==1):
		suma_empresa=boss.total_amount(clientes,filas)		
	
	elif(opc==2):
		dia=input("Ingrese el día que desea visualizar: ")
		if(dia=='LUNES' or dia=='Lunes' or dia=='lunes'):
			lunes = boss.lunes(clientes,filas)
			print(f"Lunes: {lunes}")
		elif(dia=='MARTES' or dia=='Martes' or dia=='martes' ):
			martes = boss.martes(clientes,filas)
			print(f"Martes: {martes}")
		elif(dia=='MIERCOLES' or dia=='Miercoles' or dia=='miercoles' or dia=='MIÉRCOLES' or dia=='Miércoles' or dia=='miércoles'):
			miercoles = boss.miercoles(clientes,filas)
			print(f"Miércoles: {miercoles}")
		elif(dia=='JUEVES' or dia=='Jueves'  or dia=='jueves'):
			jueves = boss.jueves(clientes,filas)
			print(f"Jueves: {jueves}")
		elif(dia=='VIERNES' or dia=='Viernes' or dia=='viernes'):
			viernes = boss.viernes(clientes,filas)
			print(f"Viernes: {viernes}")
		else:
			print(f"El dia {dia} no existe.\nIntente nuevamente")
	elif(opc==3):
		dia=input("Ingrese el día que desea modificar: ")
		if(dia=='LUNES' or dia=='Lunes' or dia=='lunes'):
			mlunes= boss.modify_matrix(clientes,filas)
			print(f"Lunes: {mlunes}")
		elif(dia=='MARTES' or dia=='Martes' or dia=='martes' ):
			mmartes= boss.modify_matrix(clientes,filas)
			print(f"Martes: {mmartes}")
		elif(dia=='MIERCOLES' or dia=='Miercoles' or dia=='miercoles' or dia=='MIÉRCOLES' or dia=='Miércoles' or dia=='miércoles'):
			mmiercoles= boss.modify_matrix(clientes,filas)
			print(f"Miércoles: {mmiercoles}")
		elif(dia=='JUEVES' or dia=='Jueves'  or dia=='jueves'):
			mjueves= boss.modify_matrix(clientes,filas)
			print(f"Jueves: {mjueves}")
		elif(dia=='VIERNES' or dia=='Viernes' or dia=='viernes'):
			mviernes= boss.modify_matrix(clientes,filas)
			print(f"Viernes: {mviernes}")
		else:
			print(f"El dia {dia} no existe.\nIntente nuevamente")
	elif(opc==4):
		pjueves=boss.promedio_jueves(clientes,filas)
		pviernes= boss.promedio_viernes(clientes,filas)
		print(f"El promedio del día jueves y viernes es {pjueves+pviernes}")
	elif(opc==5):
		print("FIN DEL PROGRAMA")
		break
	else:
		print("La opción ingresada no es válida.\nIntente nuevamente")


