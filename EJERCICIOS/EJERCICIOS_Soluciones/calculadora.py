print('1- mostrar numeros\n2- sumar\n3- restar\n4- Dividir\n5- multiplicar\n6- salir')

while True:
    opcion = int(input('Elija el numero de opercaion que quiere realizar\n'))
    num1 = float(input('ingrese el primer valor'))
    num2 = float(input('ingrese el segundo valor'))
    if int(opcion) == 1:
        print(f'valor 1: {num1} valor 2: {num2}')
    elif int(opcion) == 2:
        resultado = num1 + num2
    elif int(opcion) == 3:  
        resultado = num1 - num2
    elif int(opcion) == 4:
        if float(num1) == 0 or float(num2) == 0:
            print ('No se puede dividir con cero')
        else:
            resultado = num1 / num2 
    elif int(opcion) == 5:
        resultado = num1 * num2
    elif int(opcion) == 6:
        break
    else: 
        break
    print(resultado)