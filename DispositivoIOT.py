# Definimos la clase base para un dispositivo IoT genérico
class DispositivoIoT:
    def __init__(self, id, ubicacion):
        # Atributos protegidos para la abstracción
        self._id = id  
        self._ubicacion = ubicacion
        self._estado = "apagado"
    
    def encender(self):
        """Método para encender el dispositivo."""
        self._estado = "encendido"
        print(f"Dispositivo {self._id} en {self._ubicacion} encendido.")
    
    def apagar(self):
        """Método para apagar el dispositivo."""
        self._estado = "apagado"
        print(f"Dispositivo {self._id} en {self._ubicacion} apagado.")

    def monitorear(self):
        """Método polimórfico que se comportará diferente en cada subclase."""
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Subclase que hereda de DispositivoIoT
class SensorTemperatura(DispositivoIoT):
    def __init__(self, id, ubicacion, umbral_alerta):
        super().__init__(id, ubicacion)
        self._temperatura = 0.0
        self._umbral_alerta = umbral_alerta

    def medir_temperatura(self, valor):
        self._temperatura = valor
        print(f"Sensor {self._id}: Temperatura actual {self._temperatura}°C.")
        if self._temperatura > self._umbral_alerta:
            print("🚨 ¡Alerta de temperatura alta!")
    
    def monitorear(self):
        """Polimorfismo: Comportamiento específico para el sensor de temperatura."""
        print(f"Monitoreando sensor de temperatura {self._id} en {self._ubicacion}.")
        return self._temperatura

# Subclase para un sensor de movimiento
class SensorMovimiento(DispositivoIoT):
    def __init__(self, id, ubicacion):
        super().__init__(id, ubicacion)
        self._movimiento_detectado = False

    def detectar_movimiento(self, detectado):
        self._movimiento_detectado = detectado
        if self._movimiento_detectado:
            print(f"Sensor {self._id}: ¡Movimiento detectado!")
        else:
            print(f"Sensor {self._id}: Sin movimiento.")

    def monitorear(self):
        """Polimorfismo: Comportamiento específico para el sensor de movimiento."""
        print(f"Monitoreando sensor de movimiento {self._id} en {self._ubicacion}.")
        return self._movimiento_detectado

# Subclase para una cámara de seguridad
class CamaraSeguridad(DispositivoIoT):
    def __init__(self, id, ubicacion):
        super().__init__(id, ubicacion)
        self._grabando = False

    def iniciar_grabacion(self):
        if not self._grabando:
            self._grabando = True
            print(f"Cámara {self._id}: Grabación iniciada.")

    def detener_grabacion(self):
        if self._grabando:
            self._grabando = False
            print(f"Cámara {self._id}: Grabación detenida.")
    
    def monitorear(self):
        """Polimorfismo: Comportamiento específico para la cámara."""
        print(f"Monitoreando cámara de seguridad {self._id} en {self._ubicacion}.")
        return self._grabando