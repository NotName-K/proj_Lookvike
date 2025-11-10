class Moto:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.cilindraje = 0
        self.suspension = ""
        self.peso = 0.0
        self.precio = 0.0
        self.vel_crucero = 0.0
        self.lanzamiento = None
        self.seguridad = []
        self.accesorios = []
        self.transmision = ""
        self.iluminacion = ""
        self.relacionPP = 0.0
        self.topSpeed = 0.0
        self.caracteristicaDestacada = ""
        self.fallosComunes = []
        self.tipo = ""
        self.kilometraje = 0
        self.year = 0
        self.color = ""
        self.combustible = ""
        self.potencia = 0
        self.torque = 0.0
        self.frenos_delanteros = ""
        self.frenos_traseros = ""
        self.neumaticos = ""
        self.capacidad_tanque = 0.0
        self.consumo = 0.0


    def calcular_score(self):
        pass

    def mostrar_ficha(self):
        pass

    def tipo_conduccion(self):
        pass


class MotoNaked(Moto):
    def __init__(self):
        super().__init__()
        self.manillar_ancho = ""
        self.posicion_conduccion = ""
        self.versatilidad_urbana = 0

class MotoDeportiva(Moto):
    def __init__(self):
        super().__init__()
        self.carenado = ""
        self.velocidad_maxima = 0
        self.aceleracion_0a100 = 0.0
        self.modos_conduccion = []

class MotoTouring(Moto):
    def __init__(self):
        super().__init__()
        self.capacidad_maletas = 0
        self.pantalla_infotainment = False
        self.control_crucero = False
        self.calefaccion_asientos = False
        self.protection_bajas = ""

class MotoScooter(Moto):
    def __init__(self):
        super().__init__()
        self.espacio_baul = 0
        self.porta_casco = False
        self.gancho_transporte = False
        self.consumo_urbano = 0.0