# Pedir al usuario que ingrese la dirección IP y la cantidad de sub redes con nombre y hosts necesarios
ip = input("Ingrese la dirección IP con el segmento determinado: ")
hosts = int(input("Ingrese la cantidad de subredes: "))
# Iteraremos para llenar el diciconario de subredes
i = 0
print("Ingrese la cantidad de hosts necesarios para cada subred de manera decendente")
subRedes = {}
#ciclo para llenar el diccionario
while i < hosts:
    NOMBRE_SUBRED = "Subred-{"+str(i)+"}"
    HOSTS = int(input("Ingrese la cantidad de hosts necesarios para la Subred-{"+str(i)+"}"+": "))
    subRedes[NOMBRE_SUBRED] = HOSTS
    i = i + 1
#separamos la ip para poder trabajar con ella
ArrayIP = ip.split(".")
ArrayIP = ArrayIP[:-1] + ArrayIP[-1].split("/")
#imprimimos la ip 
print("La dirección IP es: "+ip)
# imprimimos la ip separada
print(ArrayIP)

#imprimimos el diccionario 
print("La cantidad de subredes es: "+str(hosts)) 
print(subRedes)
