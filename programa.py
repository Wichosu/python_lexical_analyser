import os

os.chdir(os.getcwd()+"/test")
    
archivos = os.listdir()

while(True):
    iterador = 1
    print("Selecciona el archivo para abrirlo (0 para salir):")
    if len(archivos) != 0:
        for i in archivos:
            print(f"[{iterador}] {i}")
            iterador += 1
    entrada = int(input())
    if entrada == 0:
        break
    seleccion = open(archivos[entrada-1], "r")
    for i in seleccion:
        print(i)
    seleccion.close()
    input("--------------------------------\nPresiona ENTER para continuar:")