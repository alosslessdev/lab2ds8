# Función recursiva para simular ciclos de monitoreo
def simulacion_recursiva(ciclos):
    if ciclos <= 0:
        print("✅ Fin de la simulación.")
        return
    else:
        print(f"Monitoreo en curso... Ciclos restantes: {ciclos}")
        simulacion_recursiva(ciclos - 1)

# Función que recibe otra función como parámetro para procesar dispositivos
def procesar_dispositivos(lista_dispositivos, funcion_a_aplicar):
    """Aplica una función dada a cada dispositivo de la lista."""
    print("\nProcesando todos los dispositivos...")
    for dispositivo in lista_dispositivos:
        funcion_a_aplicar(dispositivo)

# Función para aplicar a los dispositivos
def verificar_estado(dispositivo):
    print(f"Estado de {dispositivo._id}: {dispositivo._estado}")

# Función lambda para filtrar dispositivos
def filtrar_por_tipo(dispositivos, tipo):
    """Usa una función lambda para filtrar por el tipo de clase."""
    return list(filter(lambda d: isinstance(d, tipo), dispositivos))

# Ejemplo de uso de las funciones integradas
def gestionar_dispositivos(dispositivos):
    print("\n--- Estadísticas de dispositivos ---")
    print(f"Número total de dispositivos: {len(dispositivos)}")

    # Usamos filter y lambda para obtener solo las temperaturas
    temperaturas = [d.monitorear() for d in filtrar_por_tipo(dispositivos, SensorTemperatura)]
    
    if temperaturas:
        print(f"Temperatura mínima registrada: {min(temperaturas)}°C")
        print(f"Temperatura máxima registrada: {max(temperaturas)}°C")
        print(f"Suma de todas las temperaturas: {sum(temperaturas)}°C")
        
    # Ordenamos los dispositivos por su ID para una mejor visualización
    dispositivos_ordenados = sorted(dispositivos, key=lambda d: d._id)
    print("\nDispositivos ordenados por ID:")
    for d in dispositivos_ordenados:
        print(f"  - {d._id}: Tipo {d.__class__.__name__}") 
        