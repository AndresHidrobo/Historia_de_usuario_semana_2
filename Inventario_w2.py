#Funcion que agrega el producto
def agregar_producto(name,precio,cantidad,costo_total):
    producto = {"nombre": name, "precio": precio, "cantidad": cantidad, "Precio_tótal": costo_total}
    inventario.append(producto)
    return
#Funcion que muestra el inventario
def mostrar_inventario():
    for i in inventario:
        print("\n",i)
    return

producto={}#Diccionario de productos
inventario=[]#Lista del inventario

#Banderas que controlan los ciclos
flag_0=True
flag_2=True
full_cantidad=0
full_precio=0
#Ciclo principal
while flag_0:
    flag_1=True
    print("""
    =============================
    1. Agregar nuevo producto
    2. Mostrar inventario
    3. Calcular estadísticas
    4. Salir
    =============================""")
    option=input("\nIngrese una opción(#): ")#Solicita dato para continuar
    if option.isspace() or not option or not option.isnumeric():#Valida que la opcion ingresada no sea espacio o vacia
        print("\n Ingrese valor válido")
        continue
    option=int(option)#Se convierte el dato en entero para compararlo
    if option==1:#Procede la opcion 1
            while flag_1:
                #banderas que controlan todos los ciclos de esta opcion
                flag_1=True
                flag_11=True
                flag_12=True
                flag_13=True
                #Solicita nombre del producto
                name=input("\nIngrese el nuevo producto: ").lower()
                #Condicional para asegurar datos
                if name.isspace() or not name:
                    print("\nNo deje el espacio en blanco")
                    continue
                #Si existe el producto en el diccionario le comenta que ya existe 
                if name in producto:
                        print("\nYa existe ese producto en la lista")
                        continue
                else:
                    while flag_11:
                        #Solicitando cantidad
                        cantidad=input("\nIngrese la cantidad de existencias que hay del producto: ")
                        if cantidad.isspace() or not cantidad or not cantidad.isnumeric():
                            print("\nDigite una cantidad válida")
                            continue
                        cantidad=int(cantidad)
                        #Condicional para asegurarse que el usuario ingreso un valor aceptable
                        if cantidad <= 0:
                                #Mensaje que notifica al usuario que ingreso un valor erroneo
                                print("\nDigite una cantidad válida (mayor a 0)")
                                continue
                        while flag_12:
                                #try-except para asegurar buen ingreso de datos
                                try:
                                    #Solicita al usuario el precio por unidad del producto
                                    precio=float(input("\nDigite el costo por unidad del producto: "))
                                    #Condicional para asegurarse que el usuario ingreso un valor aceptable
                                    if precio<=0:
                                        #Mensaje que notifica al usuario que ingreso un valor erroneo
                                        print("\nDigite un precio válido (mayor a 0)")
                                    else:
                                        #Se realiza la multiplicación del precio y la cantidad para saber el valor total
                                        costo_total = float(precio*cantidad)
                                        full_precio=full_precio+costo_total #Para obtener el precio total 
                                        full_cantidad=full_cantidad+cantidad #Para obtener la cantidad total
                                        agregar_producto(name,precio,cantidad,costo_total) #Llama la funcion para agregar el producto
                                        print("\n Se agregó con éxito el producto")
                                        while flag_13:
                                            #Validacion para saber si desea agregar otra opción
                                            verificacion=input("\nDesea agregar otro producto? (si/no): ").lower()
                                            if verificacion.isspace() or not verificacion:
                                                print("\nIngrese una respuesta válida")
                                                continue
                                            elif verificacion=="si":
                                                #Al querer ingresar otro producto cierra todos los ciclos encepto el primero
                                                flag_1=True
                                                flag_11=False
                                                flag_12=False
                                                flag_13=False
                                            elif verificacion=="no":
                                                #Al no querer ingresar otro producto cierra todos los ciclos
                                                flag_1=False
                                                flag_11=False
                                                flag_12=False
                                                flag_13=False
                                            else:
                                                print("\nIngrese una respuesta válida")
                                except ValueError:
                                    print("\nIngrese un valor válido")
    elif option==2: #Ingresa la opcion 2 para imprimir el inventario
        flag_2=True
        while flag_2:
            if not inventario: #en caso de que el inventario este vacio, notifica con mensaje y no procede
                print("\nEl inventario está vacio")
                break
            else:
                mostrar_inventario() #Llama a la función de mostrar inventario
            break
    elif option==3:
        flag_3=True
        while flag_3:
            #En la opcion 3 se imprime un sub-menu para validar la acción que desee hacer el usuario
            print("""
            =============================
            1. Valor total del inventario
            2. Cantidad total de productos registrados
            3. Regresar
            =============================""")
            second_option=input("\nSeleccione una opción: ")
            #En caso de que ingresar un valor inválido no procede
            if second_option.isspace() or not second_option or not second_option.isnumeric():
                print("\n Ingrese valor válido")
                continue
            second_option=int(second_option)
            if second_option==1:
                if not inventario: #En caso que el inventario esté vacio notifica y sale del proceso
                    print("\nEl inventario está vacio")
                    continue
                print(f"\nEl valor total del inventario es: {full_precio*full_cantidad}$")
            if second_option==2:
                if not inventario: #En caso que el inventario esté vacio notifica y sale del proceso
                    print("\nEl inventario está vacio")
                    continue
                print(f"\n La cantidad total de productos en el inventario es: {full_cantidad}")
            if second_option==3:
                break
    elif option==4: #La opción 4 es para terminar el proceso
        print("Se finalizó el proceso, adios")
        flag_0=False
    else: #si ingresa un número que no este en las opciones notifica el error y regresa al menú
        print("\nSeleccione una opción válida")