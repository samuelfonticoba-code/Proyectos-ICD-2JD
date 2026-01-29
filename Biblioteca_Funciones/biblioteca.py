import json
import os
import matplotlib.pyplot as plt
import numpy as np
import squarify


archivos_json = "Prueba.json"

ruta_de_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cargar_datos(archivos_json):
    # Se agrega la coma faltante y se usa el nombre del archivo pasado por parámetro
    ruta_completa = os.path.join(ruta_de_proyecto, 'Data', archivos_json)

    try: 
        with open (ruta_completa, 'r') as archivo:
            datos = json.load(archivo)
        print("Datos cargados exitosamente")
        return datos 
    except FileNotFoundError:
        print("Error: Archivo json no encontrado")

# Se simplifica la llamada ya que la función ya construye la ruta a 'Data' internamente
resultado = cargar_datos(archivos_json)

datos_productos = [item['Mipyme']['productos de venta(analizados)'] for item in resultado]

def obtener_lista_promedios(datos_productos):

    productos = ['aceite', 'arroz', 'azucar', 'frijoles negros', 'higado', 'huevo', 'leche', 'picadillo', 'pure', 'pollo']

    promedio_total = []
    for nombre in productos:
        total = 0 
        contador = 0 
        
        for i in datos_productos:
            if nombre in i:
                total += i[nombre] # Aseguramos que sea número
                contador += 1
        
        # Corregimos la indentación y evitamos división por cero
        if contador > 0:
            promedio = total / contador
            promedio_total.append(round(promedio))
        else:
            promedio_total.append(0) 

    return promedio_total

# Llamada a la función
Lista_De_Todos_los_Promedios = obtener_lista_promedios(datos_productos)
print(Lista_De_Todos_los_Promedios)


def graficar_indice_glucemia():
    """Muestra el impacto de los productos en el azúcar en sangre."""
    colores = []

    productos = [
    'Arroz Blanco', 'Azúcar', 'Puré de Tomate', 'Leche', 
    'Frijoles Negros', 'Hígado', 'Pollo', 'Carne Picada', 
    'Huevo', 'Aceite'
]
    valores_ig = [73, 65, 40, 34, 25, 0, 0, 0, 0, 0]

    for valor in valores_ig:
        if valor > 55: colores.append('#FF4C4C') # Rojo intenso
        elif valor > 0: colores.append('#FFCC00') # Amarillo
        else: colores.append('#D3D3D3') # Gris

    fig, ax = plt.subplots(figsize=(10, 6))
    # esto invierte la barra osea va de mayor a menos lo tuve que buscar en inter :)
    p_rev, v_rev, c_rev = productos[::-1], valores_ig[::-1], colores[::-1]
    
    ax.barh(p_rev, v_rev, color=c_rev)
    ax.set_title('Impacto en la Glucemia: Índice Glucémico por Producto', fontsize=15, pad=20)
    ax.set_xlabel('Valor del Índice Glucémico (0-100)')
    ax.set_xlim(0, 100)

    for i, v in enumerate(v_rev):
        ax.text(v + 1, i, str(v), color='black', va='center', fontweight='bold')
    plt.tight_layout()
    plt.show()

def graficar_composicion_nutricional():
    """Compara los 3 macronutrientes (El albañil, la gasolina y la reserva)."""

    productos_nutricion = ['Hígado', 'Pollo', 'Arroz', 'Pure Tomate', 'Frijoles', 'Azúcar', 'Leche', 'Aceite', 'picadillo', 'Huevo']
    proteinas = [20.0, 31.0, 2.7, 1.5, 8.0, 0.0, 3.2, 0.0, 18.0, 12.6]
    grasas = [5.0, 3.6, 0.3, 0.2, 0.5, 0.0, 3.3, 100.0, 15.0, 10.6]
    carbohidratos = [4.0, 0.0, 28.0, 8.0, 21.0, 100.0, 4.8, 0.0, 0.0, 1.1]

    x = np.arange(len(productos_nutricion)) 
    ancho = 0.25
    fig, ax = plt.subplots(figsize=(14, 8))

    ax.bar(x - ancho, proteinas, ancho, label='Proteínas', color='firebrick')
    ax.bar(x, grasas, ancho, label='Grasas', color="#f78f34")
    ax.bar(x + ancho, carbohidratos, ancho, label='Carbohidratos', color="#0077ff")

    ax.set_ylabel('Gramos por cada 100g')
    ax.set_title('Composición Nutricional: El Balance de la Dieta')
    ax.set_xticks(x)
    ax.set_xticklabels(productos_nutricion, rotation=45)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

def graficar_edad_vs_peligro():
    """Muestra la aceleración del riesgo por edad y diabetes."""
    
    rangos_edad = ['30-39', '40-49', '50-59', '60-69', '70-79']
    tasa_sin_diabetes = [0.5, 1.2, 3.5, 8.0, 15.0]
    tasa_con_diabetes = [1.5, 3.8, 9.2, 18.5, 32.0]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(rangos_edad ,tasa_con_diabetes, marker='o', linewidth=3, color='#e74c3c', label='Población con Diabetes')
    ax.plot(rangos_edad ,tasa_sin_diabetes, marker='*', linewidth=2, color='#95a5a6', label='Población General', linestyle='--')
    
    ax.set_title('Aceleración del Riesgo Cardiovascular por Edad', fontsize=14, fontweight='bold')
    ax.set_xlabel('Rango de Edad (Años)')
    ax.set_ylabel('Tasa de Mortalidad Estimada (%)')
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    plt.show()

def graficar_analisis_costos():
     # Analiza qué productos superan el promedio de costo

    productos = ['aceite', 'arroz', 'azucar', 'frijoles negros', 'higado', 'huevo', 'leche', 'picadillo', 'pure', 'pollo']
    precios = Lista_De_Todos_los_Promedios
    

    promedio_gral = sum(precios) / len(precios)
    datos = sorted(zip(productos, precios), key=lambda x: x[1])
    prod_ord, prec_ord = zip(*datos)

    fig, ax = plt.subplots(figsize=(12, 7))
    colores = ['lawngreen' if p < promedio_gral else 'red' for p in prec_ord]
    barras = ax.barh(prod_ord, prec_ord, color=colores, alpha=0.8)

    ax.axvline(promedio_gral, color='black', linestyle='--', linewidth=2, label=f'Promedio: ${int(promedio_gral)}')
    ax.set_title('Análisis de Costos: ¿Qué supera el promedio?', fontsize=16, fontweight='bold')
    ax.set_facecolor("#EFF1FC")

    for barra in barras:
        width = barra.get_width()
        ax.text(width + 20, barra.get_y() + barra.get_height()/2, f'${int(width)}', va='center', fontweight='bold')
    ax.legend(loc='lower right')
    plt.tight_layout()
    plt.show()

def grafica_vista_Presupuesto():
    #Distribución visual del presupuesto (Treemap)

    productos = ['aceite', 'arroz', 'azúcar', 'frijoles negros', 'higado', 'huevo', 'leche', 'picadillo', 'pure', 'pollo']
    precios = Lista_De_Todos_los_Promedios

    etiquetas = [f'{p}\n${v}' for p, v in zip(productos, precios)]
    colores = ["#dfd661", "#f1ede9", "#98e2f5", "#4f5554", "#5f0906", "#e6ba29", "#e6acd5", "#e06f2d", "#fc6234", "#FF1E00E8"]
    
    plt.figure(figsize=(12, 8))
    squarify.plot(sizes=precios, label=etiquetas, color=colores, alpha=0.8, text_kwargs={'fontsize':10, 'fontweight':'bold'})
    plt.title('Distribución del Presupuesto: ¿Quién se lleva tu dinero?', fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.show()

def graficar_cuadrantes_eficiencia():
    # Matriz de Valor Estratégico: Dieta vs Bolsillo
    productos = ['aceite', 'arroz', 'azucar', 'frijoles', 'higado', 'huevo', 'leche', 'picadillo', 'pure', 'pollo']
    precios = Lista_De_Todos_los_Promedios

    importancia = [4, 5, 2, 8, 9, 10, 7, 9, 3, 10] 
    media_precio = sum(precios) / len(precios)
    media_imp = sum(importancia) / len(importancia)

    plt.figure(figsize=(12, 8))
    plt.scatter(precios, importancia, s=100, color='blue', edgecolors='black', zorder=5)
    plt.axvline(x=media_precio, color='gray', linestyle='--', alpha=0.5)
    plt.axhline(y=media_imp, color='gray', linestyle='--', alpha=0.5)

    for i, txt in enumerate(productos):
        plt.annotate(txt, (precios[i], importancia[i]), xytext=(7, 7), textcoords='offset points', fontweight='bold')

    plt.text(media_precio - 500, 9.5, 'LAS JOYAS\n(Barato y Nutritivo)', color='green', fontweight='bold', ha='center')
    plt.text(media_precio + 500, 9.5, 'INVERSIONES\n(Caro pero Vital)', color='darkorange', fontweight='bold', ha='center')
    
    plt.title('Matriz de Valor Estratégico: Dieta vs Bolsillo', fontsize=16)
    plt.xlabel('Precio por Envase ($)')
    plt.ylabel('Importancia Nutricional (1-10)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()