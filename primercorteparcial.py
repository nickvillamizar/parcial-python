#codigo para identificar la inteligencia de un numero
# entonces tenemos lo siguiente 27 (1,3,9)tener en cuenta lo siguiente:
#se debe solicitar la cantidad de numero a validar
# se deben generar de forma aleatoria los numeros y deben ser enteros positivos
#se debe mostrar en pantalla los numeros a validar separados por comas
#mostrar si o no en caso de que este sea inteligente o no respectivamente
numero=int (input("ingrese el numero a evaluar"))
print("el numero a evaluar es", numero)
def descomponer(numero):
    primos=[]
    for i in range (2,numero+1):
        while numero % i== 0:
            primos.append(i)
            numero=numero/i
    return(primos)
print(descomponer(numero))
#la verdad no pude administar bien los ciclos profe por ende solo pude descomponer un solo numero

    



