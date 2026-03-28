#Ejercicio1
nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    print("Error: el nombre solo debe contener letras.")
    nombre = input("Ingrese su nombre: ")

cantp = input("ingrese la cantidad de productos: ")

while not (cantp.isdigit() and int(cantp) > 0):
    print("Error: ingrese un número entero positivo.")
    cantp = input("Ingrese la cantidad de productos: ")
total_sin_descuento = 0
total_con_descuento = 0
for i in range(int(cantp)):
    precio= input("ingrese el precio del producto: ")
    while not(precio.isdigit()):
        precio= input("ingrese el precio del producto: ")
    descuento = input("Tiene descuento, inrgrese s en caso afirmativo, ingrese n en caso contrario: ")
    if (descuento == "s" or descuento == "S"):
        precio_desc = int(int(precio) * 0.9)
        total_con_descuento += precio_desc
        total_sin_descuento += int(precio)
    elif descuento == "n" or descuento == "N":
        total_sin_descuento += int(precio)
        total_con_descuento += int(precio)

ahorro = total_sin_descuento - total_con_descuento

promedio_productos = total_sin_descuento / int(cantp)
print(f"total sin descuento: {total_sin_descuento}")
print(f"total con descuento: {total_con_descuento}")
print(f"ahorro: {ahorro}")
print(f"Promedio por producto: {promedio_productos:.2f}")

#-----------------------------------------------------------------------
#Ejercicio2
usuario_correcto = "alumno"
clave_correcta = "python123"
usuario =input("ingrese usuario: ")
clave =input("ingrese la clave: ")
intentos = 0
acceso = False

while (usuario != usuario_correcto or clave!= clave_correcta) and intentos<3:
    intentos += 1
    print(f"Intento {intentos}/3 - Usuario: {usuario}\nClave: {clave}\nError: credenciales inválidas.")
    usuario =input("ingrese usuario: ")
    clave =input("ingrese la clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True   

if not acceso:
    print("Cuenta bloqueada")

while acceso:
    print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")

    if opcion == 1:
        print("Estado: Inscripto")

    elif opcion == 2:
        nueva_clave = input("Nueva clave: ")
        confirmacion = input("Confirmar clave: ")

        if len(nueva_clave) < 6:
            print("Error: la clave debe tener al menos 6 caracteres.")
        elif nueva_clave != confirmacion:
            print("Error: las claves no coinciden.")
        else:
            clave_correcta = nueva_clave
            print("Clave cambiada correctamente.")

    elif opcion == 3:
        print("¡Seguí así, vas por buen camino!")

    elif opcion == 4:
        print("Saliendo del sistema...")

#-----------------------------------------------------------------------
#Ejercicio3   
lunes1=""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""

operador= input("ingrese nombre: ")

while not operador.isalpha():
    operador= input("Error ingrese solo letras: ")
 
print("1. Reservar turno")
print("2. Cancelar turno")
print("3. Ver agenda del día")
print("4. Ver resumen general")
print("5. Cerrar sistema")

numero_menu= ("Elija una opcion 1-5: ")
numero_menu= int(numero_menu)
while (numero_menu<1) or (numero_menu>5):
    numero_menu= ("Elija una opcion valida 1-5: ")
if numero_menu == 1 :
    dia=input("Elegir día (1=Lunes, 2=Martes):")
    nombre_paciente= input("Ingrese el nombre del paciente: ")
    while not nombre_paciente.isalpha():
        nombre_paciente= input("Ingrese nombre valido solo letras: ")
    if dia == 1:
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print("Paciente ya tiene turno en Lunes.")
            else:
                if lunes1 == "":
                    lunes1 = nombre_paciente
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                else:
                    print("No hay turnos disponibles en Lunes.")

    else:
            if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                print("Paciente ya tiene turno en Martes.")
            else:
                if martes1 == "":
                    martes1 = nombre_paciente
                elif martes2 == "":
                    martes2 = nombre_paciente
                elif martes3 == "":
                    martes3 = nombre_paciente
                else:
                    print("No hay turnos disponibles en Martes.")
elif numero_menu == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in (1, 2):
            dia = input("Error. Ingrese 1 o 2: ")
        dia = int(dia)

        nombre = input("Ingrese nombre del paciente a cancelar: ")
        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")
        encontrado = False
        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True
        if encontrado:
            print("Turno cancelado.")
        else:
            print("Paciente no encontrado.")
elif numero_menu == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in (1, 2):
            dia = input("Error. Ingrese 1 o 2: ")
        dia = int(dia)

        if dia == 1:
            print("Lunes")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Martes")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")
elif numero_menu == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("RESUMEN")
        print("Lunes -> Ocupados:", ocupados_lunes, "| Libres:", 4 - ocupados_lunes)
        print("Martes -> Ocupados:", ocupados_martes, "| Libres:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Hay empate entre ambos días")
elif numero_menu == 5:
        print("Sistema cerrado.")

#-----------------------------------------------------------------------        
#Ejercicio4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

agente = input("Ingrese nombre del agente: ")
while not agente.isalpha():
    agente = input("Error. Solo letras: ")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("SISTEMA BLOQUEADO POR ALARMA")
        break

    print("ESTADO")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")

    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Elegir opción: ")
    while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
        opcion = input("Error. Elegir 1, 2 o 3: ")
    opcion = int(opcion)

    if opcion == 1:
        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            print("Forzaste demasiadas veces seguidas. La cerradura se trabó.")
            alarma = True

        else:
            if energia < 40:
                num = input("Riesgo de alarma! Elegí un número (1-3): ")
                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    num = input("Error. Elegí 1-3: ")
                if int(num) == 3:
                    alarma = True
                    print("Se activó la alarma!")

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura abierta!")

    elif opcion == 2:
        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta por hackeo!")

    elif opcion == 3:
        forzar_seguidas = 0 

        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("Descansar con alarma activa consume energía extra.")

print("RESULTADO")

if cerraduras_abiertas == 3:
    print("VICTORIA: Abriste la bóveda!")
elif alarma and tiempo <= 3:
    print("DERROTA: Sistema bloqueado por alarma.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: Te quedaste sin recursos.")
else:
    print("DERROTA.")
#-----------------------------------------------------------------------
#Ejercicio5
nombre = input("Ingrese nombre del Gladiador: ")
while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras: ")

hp_jugador = 100   
hp_enemigo = 100    
pociones = 3       

juego_activo = True 
turno_jugador = True 

while juego_activo:

    print("ESTADO")
    print(f"{nombre} HP: {hp_jugador}")
    print(f"Enemigo HP: {hp_enemigo}")
    print(f"Pociones: {pociones}")

    if turno_jugador:

        print("1. Atacar")
        print("2. Ataque crítico")
        print("3. Usar poción")

        opcion = input("Elegir opción: ")
        while not opcion.isdigit() or int(opcion) not in (1, 2, 3):
            opcion = input("Error. Elegir 1, 2 o 3: ")
        opcion = int(opcion)

        if opcion == 1:
            daño = 15
            hp_enemigo -= daño
            print(f"Atacaste e hiciste {daño} de daño")

        elif opcion == 2:
            daño = 15 * 1.5
            hp_enemigo -= int(daño)
            print(f"Golpe crítico! Hiciste {int(daño)} de daño")

        elif opcion == 3:
            if pociones > 0:
                hp_jugador += 20
                if hp_jugador > 100:
                    hp_jugador = 100
                pociones -= 1
                print("Usaste una poción (+20 HP)")
            else:
                print("No te quedan pociones")

        turno_jugador = False

    else:
        print("TURNO DEL ENEMIGO")

        if hp_enemigo > 30:
            daño = 12
            print("El enemigo ataca!")
        else:
            daño = 12 * 1.5
            print("El enemigo usa ataque crítico!")

        hp_jugador -= int(daño)
        print(f"Recibiste {int(daño)} de daño")

        turno_jugador = True

    if hp_jugador <= 0:
        print("DERROTA: Has sido vencido.")
        juego_activo = False

    elif hp_enemigo <= 0:
        print("VICTORIA: Derrotaste al enemigo!")
        juego_activo = False