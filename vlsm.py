# Autores: Jesus Haans Lopez Hernandez  31124548-8
#          Axel Casas Espinoza          31621884-9


#Funcion que encuentra la N de la formula
def findN(host):
    i = 0
    while (2**i) < host:
        i += 1
    return i 

#funcion que encuentra la mascara de subred como Sufijo
def mascaraRedS(n):
    return (32 - n)

#funcion que encuentra la mascara de subred como Decimal
def mascaraRedDec(mrs):
    i = 0
    cadenaResultado = "0.0.0.0"
    if(mrs == 0):
        return cadenaResultado
    else:
        cadenaResultado = ""
        pocteto = ""
        socteto = ""
        tocteto = ""
        cocteto = ""
        while i < 8:
            if(i < mrs):
                pocteto = pocteto + "1"
            else:
                pocteto = pocteto + "0"
            i += 1
        while i < 16:
            if(i < mrs):
                socteto = socteto + "1"
            else:
                socteto = socteto + "0"
            i += 1
        while i < 24:
            if(i < mrs):
                tocteto = tocteto + "1"
            else:
                tocteto = tocteto + "0"
            i += 1
        while i < 32:
            if(i < mrs):
                cocteto = cocteto + "1"
            else:
                cocteto = cocteto + "0"
            i += 1
        #debug utilizado para encontrar el error en como llenar los octetos.
        #print("aaa" + pocteto + "bbb" + socteto + "ccc" + tocteto + "ddd" + cocteto)
        # se convierte el binario a decimal si se desea la mascara en binario simplemente hay que concatenar los octetos
        cadenaResultado = str(int(pocteto,2)) + "." + str(int(socteto,2)) + "." + str(int(tocteto,2)) + "." + str(int(cocteto,2))
    return cadenaResultado

#funciion para imprimir el id de la red  dado un array de ip y un sufijo
def toString(arrayIP):
    i = 0
    cadenaResultado = ""
    while i < 4:
        if(i == 3):
            cadenaResultado = cadenaResultado + str(arrayIP[i])
        else:
            cadenaResultado = cadenaResultado + str(arrayIP[i]) + "."
        i += 1
    return cadenaResultado

def toInt(arrayIP):
    i = 0
    while i < len(arrayIP):
        arrayIP[i] = int(arrayIP[i])
        i += 1
    return arrayIP







# Pedir al usuario que ingrese la dirección IP y la cantidad de sub redes con nombre y hosts necesarios
ip = input("Ingrese la dirección IP del segmento de red: ")
hosts = int(input("Ingrese la cantidad de subredes: "))

# Iteraremos para llenar el diciconario de subredes
i = 0
print("Ingrese la cantidad de hosts necesarios para cada subred de manera decendente")
subRedes = {}

#separamos la ip para poder trabajar con ella
arrayIP = ip.split(".")
arrayIP = arrayIP[:-1] + arrayIP[-1].split("/")
arrayIP = toInt(arrayIP)


#ciclo para llenar el diccionario
while i < hosts:
    NOMBRE_SUBRED = "Subred-{"+str(i)+"}"
    HOSTS = int(input("Ingrese la cantidad de hosts necesarios para la Subred-{"+str(i)+"}"+": "))
    subRedes[NOMBRE_SUBRED] = HOSTS
    i = i + 1
renglon = ""


#imprimimos la tabla
# la tabla constara de la siguiente informacion:
# nombre de la subred con cantidad de host | id de la subred con Mascara  | rango util | direccion de broadcast |
for subRed in subRedes:
    n = findN(subRedes[subRed])
    mascaraSufijo = mascaraRedS(n)
    mascaraDecimal = mascaraRedDec(mascaraSufijo)
    numeroMagico = 2**n
    # Añadimos al Renglon el nombre de la subred y la cantidad de hosts necesarios
    renglon = " | " + renglon + subRed + " : " + str(subRedes[subRed])
    # Añadimos al Renglon el id de la subred, la mascara de subred en sufijo y decimal
    renglon = renglon + " | " + toString(arrayIP) + "/" + str(mascaraSufijo) + "----" + mascaraDecimal
    # Añadimos al Renglon el rango util de la subred
    # inicio
    arrayIP[3] = arrayIP[3] + 1
    renglon = renglon + " | " + toString(arrayIP)
    # fin
    arrayIP[3] = arrayIP[3] + numeroMagico - 3
    renglon = renglon + " - " + toString(arrayIP)
    # Añadimos al Renglon la direccion de broadcast
    arrayIP[3] = arrayIP[3] + 1
    renglon = renglon + " | " + toString(arrayIP) + " | "
    #dejamos la IP de la red en el inicio de la siguiente subred
    arrayIP[3] = arrayIP[3] + 1
    print(renglon)
    renglon = ""

















#Zona de pruebas de codigo.
'''


#imprimimos la ip 
print("La dirección ID de la red es: "+ip)

# imprimimos la ip separada
print(toString(arrayIP))

#imprimimos el diccionario 
print("La cantidad de subredes es: "+str(hosts)) 
print(subRedes)

Pruebas de componentes de codigo

prueba de componente que saca nuestra n de la dormula 2^n > S:

host = int(input("ingreese cantidad de host necesarios"))
print(str(findN(host)))

pruebas para hacer las mascaras de red

n = int(input("ingreese la n que nos dio la formula "))
#print("La mascara de red asociada en sufijo es: " + str(mascaraRedS(n)))
print("La mascara de res asociada en decimal es: " + mascaraRedDec(n))

'''

