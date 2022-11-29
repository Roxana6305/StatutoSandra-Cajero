###########################################################################
# Simular cajero
###########################################################################

def cajero():
    print("Hola Bienvenido al cajero de codo a codo")
    idioma = int(input("ingresa \n 1 para elegir el idioma en español \n 2 para ingles \n 3 para portugues: "))
    if idioma == 1:
        print("has seleccionado el idioma español")
        print("ingresa tu clave para acceder a tu cuenta \n la clave es 1234 ")
        clave = int(input("ingresa tu clave: "))
        nombre = str(input("ingresa tu nombre: "))
        saldo = float(85200)
        saldoDolar = float(100)
        if clave == 1234:
            print("#########################################")
            print("Bienvenido a tu cuenta", nombre, "!!")
            print("#########################################")
            print("seleciona una opcion y presiona lo siguiente: ")
            print("#########################################")
            print("     #1  consultar saldo")
            print("     #2  depositar dinero")
            print("     #3  extraer dinero")
            print("     #4  transferir dinero")
            print("     #5  comprar dolares")
            print("     #6  vender dolares")
            print("     #7  crear plazo fijo")
            print("     #8  ver ultimos movimientos")
            print("     #9  salir de la cuenta")
            print("#########################################")
            opcion = int(input("ingresa tu opcion: "))
            #1consultar saldo
            if opcion == 1:
                print("tu saldo actual en pesos es de: $" ,saldo)
            #2depositar dinero
            elif opcion == 2:
                print("#########################################")
                ingreso = int(input("digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
                print("#########################################")
                saldoActual = saldo + ingreso
                print("--Gracias por ingresar su dinero, su saldo actual es de: $",saldoActual, "--")
            #3extraer dinero
            elif opcion == 3:
                extraccion = int(input("ingresa el monto a extraer: "))
                saldoActual = saldo - extraccion
                print("gracias por extraer, tu saldo restante es: $" , saldoActual)
            #4transferir dinero
            elif opcion == 4:
                tranferir = int(input("ingrese el cbu de la cuenta a la cual deseas tranferir: "))
                monto = int(input("ingresa el monto a tranferir: "))
                print("#########################################################")
                print("Estas por realizar una transferencia al numero de cuenta ", tranferir , "con el siguiente monto: ", monto, "estas seguro que deseas realizar esta accion ?")
                print("#########################################################")
                saldoActual = saldo - monto
                confirmar = str(input("ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
                if confirmar == "si":
                    print("gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $" , saldoActual )
                elif confirmar == "no":
                    print("has cancelado tu transferencia")
                else:
                    print("has ingresado un valor invalido")
            #5comprar dolares
            elif opcion == 5:
                print("#####################################")
                print("    el precio del dolar es de $160")
                print("    tu saldo es el siguiente: " , saldo)
                print("#####################################")
                compraDolar = float(input("ingresa el monto de dolares a comprar: "))
                print("#####################################")
                print("estas seguro de comprar : u$s" , compraDolar, " dolares ?")
                confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                print("#####################################")
                if confirma == "si":
                    conversion = compraDolar * 160
                    saldoActual = saldo - conversion
                    saldoDolar = saldoDolar + compraDolar
                    print("#####################################################")
                    print("tu saldo en tu cuenta pesos es de: $" , saldoActual)
                    print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu compra")            
            #6vender dolares
            elif opcion == 6:
                print("#####################################")
                print("    el precio del dolar es de $320")
                print("    tu saldo es el siguiente: " , saldoDolar)
                print("#####################################")
                venderDolar = float(input("ingresa el monto de dolares a vender: "))
                print("#####################################")
                print("estas seguro de vender : u$s" , venderDolar, " dolares ?")
                confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                print("#####################################")
                if confirma == "si":
                    conversion = venderDolar * 320
                    saldoActual = saldo + conversion
                    saldoDolar = saldoDolar - venderDolar
                    print("#####################################################")
                    print("tu saldo en tu cuenta pesos es de: $" , saldoActual)
                    print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu venta")  
            #7crear plazo fijo
            elif opcion == 7:
                print ("#######################")
                print ("La tasa de interes es de 85 anual")
                print ("En tu cuenta tienes", saldo "Cuanto deseas invertir?")
                print ("#######################")
                crearPlazoFijo = float(input("ingrese el monto: "))
                print ("#######################")
                print("estas seguro de invertir en un plazo fijo" , crearPlazoFijo, "con interes de 85 anual")
                confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
                if confirma == "si":
                    gananciaPlazoFijo = crearPlazoFijo * (85/100)
                    plazoFijoTotal = crearPlazoFijo + gananciaPlazoFijo
                    saldoActual = saldo - crearPlazoFijo
                    print("#####################################################")
                    print("El saldo en tu cuenta pesos es de: $" , saldoActual)
                    print("El plazo fijo ha recibir es de" , plazoFijoTotal )
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu plazo fijo")                 
            #8ver ultimos movimientos
            #9salir de la cuenta
        else:
            print("clave incorrecta")
    elif idioma == 2:
        print("has seleccionado ingles")
    elif idioma == 3:
        print("has seleccionado portugues")
    else:
        print("opcion incorrecta")
cajero()
