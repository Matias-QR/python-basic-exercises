#ServiExpress

patente=[]
marca=[]
modelo=[]
año_fabricacion=[]
tipo_vehiculo=['b','d','e','h']
registros=[]

#menu 1.registrar automovil 2.registro mantenimiento 3.consultar automovil 4.salir

"""Crear una lista para almacenar las patentes de autos

    #patentes de autos
    patentes_autos=[]

    #funcion para cargar una patente en la lista
    def cargar_patente():
    patente=input("ingrese una patente de auto: ")
    patentes_autos.append(patente)
    print(f"la patente '{patente}' ha sido registrada")

    #funcion para buscar una patente
    patente_a_buscar=input("ingrese una patente de auto: ")
    if patente_a_buscar in patentes_autos:
        print(f"la patente '{patente_a_buscar}' se encuentra en la lista"
    else:
    print(f"la patente '{patente_a_buscar}' no se encuentra en la lista")



    bucle principal del programa While True:
    print(\nMenu:")
    print("1.Cargar patente")
    print("2.Buscar patente")
    print("3.Salir")

    opcion = input("seleccione una opción: ")

    if opcion == "1":
        cargar_patente()
    elif opcion == "2":
        buscar_patente()
    elif opcion == "3#:
        print("¡hasta luego!")
        break
    else:
        print("Opción incorrecta. Por favor, seleccione una opción correcta del menu.")
        
