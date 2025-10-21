class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, cantidad):
        self.saldo += cantidad

    def extraer(self, cantidad):
        if self.saldo > cantidad:
            self.saldo -= cantidad
        else:
            print("No hay suficiente saldo")

    def obtener_saldo(self):
        return self.saldo

class CuentaAhorro(Cuenta):
    def __init__(self, tasa_interes):
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        self.tasa_interes -= self.tasa_interes