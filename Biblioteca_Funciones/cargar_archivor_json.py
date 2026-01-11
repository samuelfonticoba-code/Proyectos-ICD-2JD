import json
import os

archivos_json = "Prueba.json"
def cargar_datos(archivos_json):
            try: 
                # file = os.path.join(folder, archivos_json)
                with open (archivos_json,'r') as archivo:
                    datos = json.load(archivo)
                print("Datos cargados exitosamente")
                return datos 
            except FileNotFoundError:
                print("Error:Archivo json no encontrado")

print("probando la funcion") 
resultado = cargar_datos(os.path.join('Data', archivos_json))
print(resultado) 


