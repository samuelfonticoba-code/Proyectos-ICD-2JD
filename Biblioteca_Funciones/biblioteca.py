import json
import os
import matplotlib.pyplot as plt
import numpy as np



archivos_json = "Prueba.json"

ruta_de_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cargar_datos(archivos_json):
    # Se agrega la coma faltante y se usa el nombre del archivo pasado por parametro
    ruta_completa = os.path.join(ruta_de_proyecto, 'Data', archivos_json)

    try: 
        with open (ruta_completa, 'r') as archivo:
            datos = json.load(archivo)
        print("Datos cargados exitosamente")
        return datos 
    except FileNotFoundError:
        print("Error: Archivo json no encontrado")

# Se simplifica la llamada ya que la funcion ya construye la ruta a 'Data' internamente
resultado = cargar_datos(archivos_json)



def obtener_lista_promedios(datos_productos):

    productos = ['aceite', 'arroz', 'azucar', 'frijoles negros', 'higado', 'huevo', 'leche', 'picadillo', 'pure', 'pollo']

    promedio_total = []
    for nombre in productos:
        total = 0 
        contador = 0 
        
        for i in datos_productos:
            if nombre in i:
                total += i[nombre] # Aseguro que sea número
                contador += 1
        
        # Corregimos la indentación y evitamos division por cero
        if contador > 0:
            promedio = total / contador
            promedio_total.append(round(promedio))
        else:
            promedio_total.append(0) 

    return promedio_total

def graficar_indice_glucemia():
    # """Muestra el impacto de los productos en el azucar en sangre."""
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
    #compara los 3 pilare de nutricion 

    productos_nutricion = ['Hígado', 'Pollo', 'Arroz', 'Pure Tomate', 'Frijoles', 'Azúcar', 'Leche', 'Aceite', 'picadillo', 'Huevo']
    proteinas = [20.0, 31.0, 2.7, 1.5, 8.0, 0.0, 3.2, 0.0, 18.0, 12.6]
    grasas = [5.0, 3.6, 0.3, 0.2, 0.5, 0.0, 3.3, 100.0, 15.0, 10.6]
    carbohidratos = [4.0, 0.0, 28.0, 8.0, 21.0, 100.0, 4.8, 0.0, 0.0, 1.1]

    x = np.arange(len(productos_nutricion)) 
    ancho = 0.25
    fig, ax = plt.subplots(figsize=(12, 8))

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

def graficar_metas_diabeticas():
    # Usamos los puntos medios de los rangos de la ADA
    etiquetas = ['Carbohidratos (45-50%)', 'Proteínas (15-20%)', 'Grasas (30-35%)']
    porcentajes = [47.5, 17.5, 35] 
    colores = ["#b31a1a", "#0f68c2", "#24cc24"] # Rojo , Azul, Verde
    explode = (0.1, 0, 0)  # Resaltamos los Carbohidratos porque es lo que más deben cuidar

    plt.figure(figsize=(8, 8))
    plt.pie(porcentajes, explode=explode, labels=etiquetas, autopct='%1.1f%%',
            shadow=True, startangle=140, colors=colores)

    plt.title('Distribución Calórica Diaria Recomendada (ADA)', fontsize=14, pad=20)
    
    # Nota al pie para aclarar que son rangos
    plt.figtext(0.5, 0.01, 
                "Nota: Los rangos varían según la actividad física y el estado renal del paciente.", 
                ha="center", fontsize=10, bbox={"facecolor":"orange", "alpha":0.1, "pad":5})

    plt.show()

def procesar_analisis_nutricional(json_cargado):
    resultado = []
    base_datos = json_cargado["datos"]
    info_productos = base_datos["datos_tecnicos"]

    for numero,item in enumerate(base_datos["precios_Mipymes"]):
        nombre_mypime = f"Mipyme_{numero + 1}"
        productos_tienda = item["Mipyme"]["productos de venta(analizados)"]
        analisis_tienda = {
            "numero": nombre_mypime,
            "analisis_productos": {}
        }
        for producto, precio in productos_tienda.items():
            # Solo procesamos si el precio es mayor a 0 (
            if precio > 0:
                ficha = info_productos[producto]
                # PASO 1: Cuanto cuesta 1 gramo?
                precio_por_gramo = precio / ficha["venta_g"]
                # PASO 2: Cuanto cuesta la racion oficial del INHEM?
                costo_porcion = precio_por_gramo * ficha["porcion_g"]

                # PASO 3: Cuanta proteina hay en esa racion?
                # Dividimos prot_100g entre 100 para tener proteina por gramo
                proteina_porcion = (ficha["prot_100g"] / 100) * ficha["porcion_g"]

                # PASO 4: Cuantos carbohidratos hay en esa racion?
                carbos_porcion = (ficha["carb_100g"] / 100) * ficha["porcion_g"]

                # PASO 5: Indice de Eficiencia (CUP pagados por cada gramo de proteina)
                if proteina_porcion > 0:
                    eficiencia = costo_porcion / proteina_porcion
                else:
                    eficiencia = float('inf') # Para azúcar/aceite que no tienen proteína

                analisis_tienda["analisis_productos"][producto] = {
                "costo_plato": round(costo_porcion, 2),
                "proteina_g": round(proteina_porcion, 2),
                "carbos_g": round(carbos_porcion, 2),
                "eficiencia_cup_x_g_prot": round(eficiencia, 2)
                }
        resultado.append(analisis_tienda)
    return resultado

def obtener_promedios_eficiencia(analisis_completo):
    # Diccionarios para acumular las sumas de cada nutriente y costo
    datos_acumulados = {} # Aqui guardaremos { 'producto': {'costo': suma, 'prot': suma, ...} }
    conteos = {}

    for tienda in analisis_completo:
        for producto, datos in tienda["analisis_productos"].items():
            if producto not in datos_acumulados:
                datos_acumulados[producto] = {"costo": 0, "prot": 0, "carb": 0}
                conteos[producto] = 0
            
            # Sumamos cada valor individual
            datos_acumulados[producto]["costo"] += datos["costo_plato"]
            datos_acumulados[producto]["prot"] += datos["proteina_g"]
            datos_acumulados[producto]["carb"] += datos["carbos_g"]
            conteos[producto] += 1
    
    # Ahora calculamos el promedio de cada uno y armamos el diccionario final
    promedios_finales = {}
    for prod in datos_acumulados:
        n = conteos[prod]
        promedios_finales[prod] = {
            "costo_plato": round(datos_acumulados[prod]["costo"] / n, 2),
            "proteina_g": round(datos_acumulados[prod]["prot"] / n, 2),
            "carbos_g": round(datos_acumulados[prod]["carb"] / n, 2)
        }
    
    return promedios_finales


def generar_visualizacion_eficiencia(datos_promediados):
    """
    Recibe un diccionario con {producto: {costo_plato, proteina_g, carbos_g}} 
    y genera el gráfico de barras comparativo basado en la eficiencia.
    """ 
    # 1. calculamos la eficiencia para poder ordenar
    # creamos una lista de tuplas: (nombre, valor_eficiencia)
    lista_eficiencia = []
    for producto, datos in datos_promediados.items():
        if datos["proteina_g"] > 0:
            eficiencia = datos["costo_plato"] / datos["proteina_g"]
            lista_eficiencia.append((producto, eficiencia))
    
    # 2. Ahora  ordenar 
    items_ordenados = sorted(lista_eficiencia, key=lambda x: x[1])
    
    productos = [item[0].capitalize() for item in items_ordenados]
    valores = [item[1] for item in items_ordenados]

    # 3. Crear el grafico
    plt.figure(figsize=(12, 7))
    colores = plt.cm.RdYlGn_r([i/len(valores) for i in range(len(valores))])
    barras = plt.bar(productos, valores, color=colores, edgecolor='black', alpha=0.8)

    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.5, 
                 f'{yval:.2f}', ha='center', va='bottom', fontweight='bold')

    plt.title('Costo de Nutrición: CUP necesarios para obtener 1g de Proteína', fontsize=15, pad=20)
    plt.ylabel('Costo (CUP)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()


def analizar_menus_para_el_diario(promedios_eficiencia,configuracion):
    meta_prot = configuracion["meta_diaria_proteina_g"]
    limite_carb = configuracion["limite_diario_carbos_g"]
    # pongo posibles menus con los productos en los que una persona puede comer en el dia 

    menus_a_probar = {
        "Dieta Tradicional": ["arroz", "arroz", "frijoles negros", "azucar", "aceite"],
        "Dieta Stigler (Sugerida)": ["pollo", "arroz", "frijoles negros", "huevo", "aceite"],
        "Dieta Proteica": ["pollo", "higado", "huevo", "leche"]
    }

    Menu_Alt_prot = []
    Menu_Stigler = []
    Menu_ineficiente = []

    for nombre_menu, ingredientes in menus_a_probar.items():
        total_costo = 0
        total_prot = 0
        total_carb = 0
        
        # Sumamos los valores de cada ingrediente usando los PROMEDIOS
        for ing in ingredientes:
            datos_ing = promedios_eficiencia[ing]
            total_costo += datos_ing["costo_plato"]
            total_prot += datos_ing["proteina_g"]
            total_carb += datos_ing["carbos_g"]

        ficha_resumen = (nombre_menu, round(total_costo, 2), round(total_prot, 2), round(total_carb, 2))

        # Si cumple la proteina y no se pasa de carbos (EL IDEAL)
        if total_prot >= meta_prot and total_carb <= limite_carb:
            # Si además es barato (digamos, menos de 900 CUP), es Stigler
            if total_costo < 900:
                Menu_Stigler.append(ficha_resumen)
            else:
                Menu_Alt_prot.append(ficha_resumen)

                # Si falla en algo (mucha azucar pcoa proteina)
        else:
            Menu_ineficiente.append(ficha_resumen)

    return Menu_Stigler, Menu_Alt_prot, Menu_ineficiente


def graficar_analisis_platos(stigler, alta_prot, ineficiente):
    # 1. Unimos todos los resultados en una sola lista
    todos_los_menus = stigler + alta_prot + ineficiente
    
    # Extraemos los datos usando listas simples
    nombres = [m[0] for m in todos_los_menus]
    costos = [m[1] for m in todos_los_menus]
    proteinas = [m[2] for m in todos_los_menus]
    carbos = [m[3] for m in todos_los_menus]

    # 2. Creamos el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    # Dibujamos las barras de Proteína
    barras_p = ax.barh(nombres, proteinas, label='Proteína (g)', color="#120fcce8")
    
    # Dibujamos las barras de Carbohidratos empezando donde terminan las de proteina
    # El parametro 'left' hace el efecto de "apilado" sin usar numpy
    barras_c = ax.barh(nombres, carbos, left=proteinas, label='Carbohidratos (g)', color="#fc5000", alpha=0.6)

    # 3. Añadimos etiquetas de Costo y detalles
    for i, costo in enumerate(costos):
        ax.text(proteinas[i] + carbos[i] + 5, i, f"{costo} CUP", va='center', fontweight='bold', color='blue')

    # Líneas de referencia para que el profe vea los límites
    ax.axvline(x=75, color='purple', linestyle='--', alpha=0.5, label='Meta Proteína (75g)')
    ax.axvline(x=250, color='red', linestyle='--', alpha=0.5, label='Máximo Carbos (250g)')

    # Ajustes finales
    ax.set_title('Analisis Nutricional por Menu Diario', fontsize=14)
    ax.set_xlabel('Gramos Totales (Proteina + Carbohidratos)')
    ax.legend(loc='upper left',bbox_to_anchor=(1,1),fontsize="small",title="Referencias")
    
    plt.tight_layout()
    plt.show()