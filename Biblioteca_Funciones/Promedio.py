
def calcular_promedio_precios(datos):
    
    productos = datos.get('Mipyme','productos de venta (analizados)',{})
    
    total = 0 
    contador = 0 
    
    for producto in productos:
        if 'nombre' in producto:   #nombre seria el nombre del producto que promedio en mis jsons
            total += producto['nombre'] 
            contador += 1
            promedio = total / contador
        
        return round(promedio,2)
    
