def efectivo(billete):
    mil  = (billete // 1000)
    m    = (billete % 1000)
    quinientos  = (m // 500)
    m    = (m % 500)
    doscientos  = (m // 200)
    m    = (m % 200)
    cien = (m // 100)
    m    = (m % 100)
    cincuenta   = (m // 50)
    m    = (m % 50)
    veinte   = (m // 20)
    m    = (m % 20)
    d[0]+= mil
    d[1]+= quinientos
    d[2]+= doscientos
    d[3]+= cien
    d[4]+= cincuenta
    d[5]+= veinte

#solo movi esta parte del codigo para crear un funcion la cula resive un parametro llamado "empleados" (punto 1)(punto 2)
def sueldos(empleados):
	for i in range (empleados):
		sueldos = int(input("Ingresa el sueldo"+str(i)+": \n $"))
		listas.append(sueldos)
		efectivo(sueldos)
		i += 1
#esta parte tambien la hice una funcion y pide como entrada dos parametros pero eta funcion retorna el resultado de nomina hacia la misma variable que entro (punto 1)(punto 3)
def liata_de_empleados(empleados, nomina):
	for i in range (empleados) :
		print("Empleado",i,"->$",listas[i])
		nomina += listas[i] 
		i += 1
	return nomina

i = int(1) 
d=[0,0,0,0,0,0]
listas = []
empleados = int(input("¿Cuántos emplados recibirán sueldo?\n"))
sueldos(empleados)
nomina = int(0)
print ("\n Nomina \n")
nomina = liata_de_empleados(empleados, nomina)

print("\n Total de nomina: $",nomina, "pesos.")

#dicionario que solo representa los valores de la lista ya establecida "d"(punto 4)
Diccionario = {
	"$1000": d[0],
	"$500" : d[1],
	"$200" : d[2],
	"$100" : d[3],
	"$50"  : d[4],
	"$20"  : d[5],
	}

#en lugar de imprimir la lista, imprime el diccionario el cual contiene guardada la lista "d"
print ("\n Desgloce de efectivo \n ")
print("Billetes de  $1000 --> ",Diccionario["$1000"]) 
print("Billetes de  $500  --> ",Diccionario["$500"]) 
print("Billetes de  $200  --> ",Diccionario["$200"]) 
print("Billetes de  $100  --> ",Diccionario["$100"]) 
print("Billetes de  $50   --> ",Diccionario["$50"]) 
print("Billetes de  $20   --> ",Diccionario["$20"])