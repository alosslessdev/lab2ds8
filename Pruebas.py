# Crear una lista de dispositivos para nuestra simulación
dispositivos_iot = [
    SensorTemperatura("ST-01", "Cocina", 25.0),
    CamaraSeguridad("CS-01", "Entrada principal"),
    SensorMovimiento("SM-01", "Pasillo"),
    SensorTemperatura("ST-02", "Sala", 22.5),
    CamaraSeguridad("CS-02", "Jardín")
]

# Encender y configurar dispositivos
print("--- Iniciando dispositivos ---")
for dispositivo in dispositivos_iot:
    dispositivo.encender()

# Usar el método polimórfico 'monitorear' para cada tipo de dispositivo
print("\n--- Monitoreo de estado de los dispositivos ---")
for dispositivo in dispositivos_iot:
    dispositivo.monitorear()

# Configurar valores específicos para los sensores
dispositivos_iot[0].medir_temperatura(26.0) # ¡Esto debería generar una alerta!
dispositivos_iot[3].medir_temperatura(20.0)
dispositivos_iot[2].detectar_movimiento(True)
dispositivos_iot[1].iniciar_grabacion()

# Usar la función que recibe otra función como parámetro
procesar_dispositivos(dispositivos_iot, verificar_estado)

# Usar la función recursiva para simular 3 ciclos de monitoreo
print("\n--- Inciando simulación de monitoreo ---")
simulacion_recursiva(3)

# Usar las funciones de gestión y lambda
gestionar_dispositivos(dispositivos_iot)

# Apagar todos los dispositivos
print("\n--- Apagando todos los dispositivos ---")
for dispositivo in dispositivos_iot:
    dispositivo.apagar()
    