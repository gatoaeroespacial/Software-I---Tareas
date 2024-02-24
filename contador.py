import os
import re
class Carpeta:
    def __init__(self, nombre, ruta, archivos):
        self.nombre = nombre
        self.ruta = ruta
        self.archivos = archivos

class Archivo:
    def __init__(self, nombre, carpeta):
        self.nombre = nombre
        self.carpeta = carpeta
        self.extension = os.path.splitext(nombre)[1]
     

class Contador:
    def __init__(self, nombre_carpeta, nombre_archivo, palabra, conteo):
        self.nombre_carpeta = nombre_carpeta
        self.nombre_archivo = nombre_archivo
        self.palabra = palabra
        self.conteo = conteo

    def buscar_palabra(archivo, palabra):
        conteo = 0
        for linea in archivo.splitlines():
            conteo += len(re.findall(r"\b{}\b".format(palabra), linea.lower()))
        return conteo
    
def main():

    ruta_carpeta = input("Escriba la ruta de la carpeta: ")
    palabra = input("Escriba la palabra a buscar: ")


    archivos = []
    try:
        os.listdir(ruta_carpeta)
    except FileNotFoundError:
        print("La carpeta no existe")
        return
    for archiv in os.listdir(ruta_carpeta):
        nombre_carpeta=os.path.basename(ruta_carpeta)
        extension = os.path.splitext(archiv)[1]
        if extension in (".txt", ".xml", ".json", ".csv"):
            archivo = Archivo(archiv,nombre_carpeta)
            archivos.append(archivo)
        else:
            print(f"El archivo {archiv} no es un archivo de texto")
    carpeta = Carpeta(nombre_carpeta,ruta_carpeta,archivos)

    conteo_total = 0
    
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta.ruta, archivo.nombre)
        with open(ruta_archivo, "r") as f:
           
           texto =f.read()
        conteo_archivo = Contador.buscar_palabra(texto, palabra)
        conteo_total += conteo_archivo


        print(f"Archivo: {archivo.nombre} - Conteo: {conteo_archivo}")


    print(f"Conteo total en la carpeta: {conteo_total}")


main()

