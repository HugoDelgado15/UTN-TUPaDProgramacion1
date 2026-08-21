#Ejercicio 1
notas= [5,10,8,9,2,3,3,4,7,5]
suma_promedio= 0
nota_min=10
nota_max= 0
for i in range(10):
    print(notas[i])
    suma_promedio+= notas[i]
    if notas[i] > nota_max:
        nota_max= notas[i]
    elif notas[i] < nota_min:
        nota_min= notas[i]
    
prom= suma_promedio/10
print(f"el promedio de todas las notas es: {prom}")
print(f"la nota mas alta es: {nota_max} y la nota mas baja es: {nota_min}")

#Ejercicio 2

productos =[]

for i in range(5):
    producto= input(f"ingrese el producto {i+1}")
    productos.append(producto)

lista_ordenada= sorted(productos)
print(f"lista ordenada alfabeticamente: {lista_ordenada}")

eliminar= input(f"ingrese el prducto que deasea eliminar")

if eliminar in productos:
    productos.remove(eliminar)
    print(f"Producto eliminado")
    print(f"ista actualizada {productos}")

else:
    print("el producto que desea eliminar no se encuentra en la lista")


#Ejercicio 3
import random
numeros =[]
lista_par =[]
lista_impar=[]
contador_par= 0
contador_impar= 0

for i in range (15):
    numeros.append(random.randint(1, 100))
    if (numeros[i] % 2) == 0 :
        lista_par.append(numeros[i])
        contador_par+=1
    else:
        lista_impar.append(numeros[i])
        contador_impar+=1
print(f"la cantidad de numeros pares es de {contador_par} y la de numeros impares es de {contador_impar}")

#Ejercicio 4

lista_sin_repetidos=[]
datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]

for i in range(9):
    if not datos[i] in lista_sin_repetidos:
        lista_sin_repetidos.append(datos[i])
    else:
        pass
print(f"lista sin repetidos {lista_sin_repetidos}")

#Ejercicio 5
estudiantes = ["Juan", "Ana", "Pedro", "Lucia", "Carlos", "Maria", "Sofia", "Diego"]

opcion = input("¿Querés agregar (A) o eliminar (E) un estudiante? ")

opcion = opcion.lower()

if opcion == "a" :
    nuevo= input("ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
elif opcion == "e":
    eliminar= input("ingrese el nombre del estudiante a borrar: ") 
    if eliminar in estudiantes :
        estudiantes.remove(eliminar)
    else: 
        print("ingrese nombre valido del estudiante")
else:
    print("ingrese una opcion valida")
print(f"lista de estudiantes actualizada {estudiantes}")

#Ejericio 6
rotar_numeros=[1, 2, 3, 4, 5, 6, 7]

numero_eliminado = rotar_numeros.pop()

rotar_numeros.insert(0, numero_eliminado)
print(rotar_numeros)

#Ejericio 7
temperaturas = [ [9, 20], [12, 22], [8, 18], [15, 25], [11, 21], [9, 19], [14, 24] ]
suma_max= 0
suma_min= 0
mayor_amplitud= 0
for i in range(7):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]

    suma_min += minima
    suma_max += maxima

    amplitud = maxima - minima

    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1 

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print(f"Promedio de temperaturas mínimas: {promedio_min:.2f}")
print(f"Promedio de temperaturas máximas: {promedio_max:.2f}")
print(f"Dia con mayor amplitud termica: {dia_mayor}")

#Ejericio 8

notas = [ [7, 8, 6], [9, 6, 7], [5, 7, 8], [10, 9, 8], [6, 6, 7] ] 
materia1=0
materia2=0
materia3=0

for i in range(5):
    suma_estudiante= 0
    for j in range(3):
        suma_estudiante+= notas[i][j]

    materia1+= notas[i][0]
    materia2+= notas[i][1]
    materia3+= notas[i][2]
    promedio_estudiante= suma_estudiante / 3 
    print(f"el promedio del estdiante {i+1} es de: {promedio_estudiante}")

promedio_materia1= materia1 / 5

promedio_materia2= materia2 / 5

promedio_materia3= materia3 / 5

print(f"el promedio de la materia 1 es: {promedio_materia1}\nel promedio de la materia 2 es: {promedio_materia2}\nel promedio de la materia 3 es: {promedio_materia3}")


#Ejericio 9
ta_te_ti=[["-", "-", "-"],["-", "-", "-"], ["-", "-", "-"]]

for i in range(9):
   turno= input("ingrese X o O segun corresponda")
   fila= int(input("ingrese la fila 1-3: "))
   columna= int(input("ingrese la columna 1-3: "))
   
   ta_te_ti[fila-1][columna-1]= turno

   for fila in ta_te_ti:
      print(*fila)

#Ejercicio 10

ventas = [ [10, 12, 8, 9, 15, 7, 11], [5, 7, 6, 8, 10, 9, 4], [20, 18, 25, 22, 19, 30, 28], [3, 4, 2, 5, 6, 4, 3] ]

print("Totales por producto:")
totales_productos = []

for i in range(4):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")

print()

mayor_total_dia = 0
dia_mayor = 0

for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    
    if suma_dia > mayor_total_dia:
        mayor_total_dia = suma_dia
        dia_mayor = j

print(f"Día con más ventas: Día {dia_mayor+1} con {mayor_total_dia}")
print()

mayor_producto = 0
indice_producto = 0

for i in range(4):
    if totales_productos[i] > mayor_producto:
        mayor_producto = totales_productos[i]
        indice_producto = i

print(f"Producto más vendido: Producto {indice_producto+1} con {mayor_producto}")


#Ejercicio 11

estudiantes10 = ["Juan", "Ana", "Pedro", "Lucia", "Carlos", "Maria", "Sofia", "Diego", "Pedro", "Laura"]

nombre_a_buscar= input("ingrese un nombre: ")

if nombre_a_buscar in estudiantes10:
    indice=estudiantes10.index(nombre_a_buscar)
    print(f"se encontro el nombre: {nombre_a_buscar} en la posicion {indice+1}")
else:
    print(f"no se encontro el nombre: {nombre_a_buscar} en la lista")


#Ejercicio 12

lista_ocho_numeros= []

for i in range(8):
    numero= int(input("ingrese un numero para agregar a la lista"))
    lista_ocho_numeros.append(numero)    
lista_menor_mayor= sorted(lista_ocho_numeros)
lista_mayor_menor= sorted(lista_ocho_numeros, reverse= True)  
print(f"lista original: {lista_ocho_numeros}\n lista de mayor a menor{lista_mayor_menor}\n lista de menor a mayor{lista_menor_mayor}")  


#Ejercicio 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_mayor_menor= sorted(puntajes, reverse=True)
print(f"puntajes ranking:")
print(*puntaje_mayor_menor, sep='\n')

puntaje_min=99999
puntaje_max=0

for i in range(len(puntajes)):
    if puntajes[i] > puntaje_max:
        puntaje_max= puntajes[i]
    elif puntajes[i] < puntaje_min :
        puntaje_min= puntajes[i]
    else: 
        pass

indice= puntajes.index(990)

print(f"puntaje mas alto: {puntaje_max} \npuntaje mas bajo: {puntaje_min}\nel numero 990 se encuentra en la posicion {indice+1}")