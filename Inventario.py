inventario={

}
#Banderas que controlan los ciclos
flag_0=True
flag_1=True
flag_11=True
flag_12=True
flag_2=True
#Ciclo principal
while flag_0:
    print("""
    =============================
    1. Agregar nuevo producto
    2. Mostrar inventario
    3. Calcular estadísticas
    4. Salir
    =============================""")
    option=input("\nIngrese una opción(#): ")
    if option.isspace() or not option or not option.isnumeric():
        print("\n Ingrese valor válido")
        continue
    option=int(option)
    if option==1:
            while flag_1:
                producto=input("\nIngrese el nuevo producto: ").lower()
                #Condicional para asegurar datos
                if producto.isspace() or not producto:
                    print("\nNo deje el espacio en blanco")
                    continue
                if producto in inventario:
                        print("\nYa existe ese producto en la lista")
                else:
                    while flag_11:
                        #Solicitando cantidad
                        cantidad=input("Ingrese la cantidad de existencias que hay del producto: ")
                        if cantidad.isspace() or not cantidad or not cantidad.isnumeric():
                            print("\nDigite un precio válido")
                            continue
                        cantidad=int(cantidad)
                        #Condicional para asegurarse que el usuario ingreso un valor aceptable
                        if cantidad <= 0:
                                #Mensaje que notifica al usuario que ingreso un valor erroneo
                                print("Digite una cantidad válida (mayor a 0)")
                                continue
                        while flag_12:
                                #try-except para asegurar buen ingreso de datos
                                try:
                                    #Solicita al usuario el precio por unidad del producto
                                    precio=float(input("Digite el costo por unidad del producto: "))
                                    #Condicional para asegurarse que el usuario ingreso un valor aceptable
                                    if precio<=0:
                                        #Mensaje que notifica al usuario que ingreso un valor erroneo
                                        print("Digite un precio válido (mayor a 0)")
                                    else:
                                        #Se realiza la multiplicación del precio y la cantidad para saber el valor total
                                        costo_total = float(precio*cantidad)
                                        break #Se cierra el ciclo
                                except ValueError:
                                    print("\nIngrese un valor válido")
                        break

                        valor=input("\nIngrese su precio: ")
                        if valor.isspace() or not valor or not valor.isnumeric():
                            print("\nDigite un precio válido")
                            continue
                        valor=int(valor)
                        if valor<=0:
                            print("\nIngrese un número válido")
                            continue
                        else:
                            inventario[producto]=valor
                            print("\nSe registro con exito el nuevo producto")
                            cantidad = len(inventario)
                            promedio = sum(inventario.values()) / cantidad
                            print(f"\nEstadísticas actuales:")
                            print(f"\nProductos en inventario: {cantidad}")
                            print(f"\nPrecio promedio: ${promedio:.2f}")
                            break
                    break
    elif option==2:
        while flag_2:
                if not inventario:
                    print("\nEl diccionario está vacio")
                    break
                print("\n",inventario)
                algo=input("\nIngrese el producto que desea verificar: ").lower()
                if algo.isspace() or not algo:
                    print("\nNo deje el espacio en blanco")
                    continue
                if algo in inventario:
                    print(f"\nEl precio de {algo} es: ",inventario[algo])
                    cantidad = len(inventario)
                    promedio = sum(inventario.values()) / cantidad
                    print(f"\nEstadísticas actuales")
                    print(f"\nProductos en inventario: {cantidad}")
                    print(f"\nPrecio promedio: ${promedio:.2f}")
                    break
                else:
                    print("\nNo exite este producto en el inventario")
    elif option==3:
        print
    elif option==4:
        print("Se finalizó el proceso, adios")
        flag_0=False
    else:
        print("\nSeleccione una opción válida")







#Valores que controlan los ciclos
n=-1
n2=-1
#Solicita el nombre del producto al usuario
nombre = input("Bienvenido por favor ingrese el nombre del producto que desea ingresar: ")
#Inicia un ciclo para asegurarse de que el usuario ingrese bien los datos
while n != 0:
    #Se solicita al usuario la cantidad de unidades que quiere ingresar del producto
    cantidad=int(input("Ingrese la cantidad de existencias que hay del producto: "))
    #Condicional para asegurarse que el usuario ingreso un valor aceptable
    if cantidad <= 0:
            #Mensaje que notifica al usuario que ingreso un valor erroneo
            print("Digite una cantidad válida (mayor a 0)")
    else:
        #Ciclo anidado para no repetir el proceso anterior
        while n2 != 0:
            #Solicita al usuario el precio por unidad del producto
            precio=float(input("Digite el costo por unidad del producto: "))
            #Condicional para asegurarse que el usuario ingreso un valor aceptable
            if precio<=0:
                #Mensaje que notifica al usuario que ingreso un valor erroneo
                print("Digite un precio válido (mayor a 0)")
            else:
                #Se realiza la multiplicación del precio y la cantidad para saber el valor total
                costo_total = float(precio*cantidad)
                #Imprime la información que se le solicitó al usuario, más el precio total del producto
                print("Producto:",nombre,"/ Precio por unidad:",precio,"/ unidades disponibles:",cantidad,"/ Precio total:",costo_total)
                #se cambia el valor para cerrar el ciclo
                n2 = 0
        #se cambia el valor para cerrar el ciclo
        n=0
#El algoritmo le solicita al usuario ingresar el nombre del producto, luego entra en un ciclo controlado para evitar que el usuario ingrese valores incorrectos
#Dentro del ciclo solicita la cantidad de unidades del producto, si ingresa un valor incorrecto y vuelve a preguntar hasta que el valor ingresado sea satisfactorio
#Luego ingresa en un ciclo anidado donde pregunta por el precio del producto, donde se repite el proceso anterior, al ingresar un valor satisfactorio realiza una multiplicación entre el precio y la cantidad
#Para finalizar imprime los datos ingresados por el usuario junto al precio total y se cierran los ciclos cambiando el valor de la condicional
