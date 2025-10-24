class Cuenta:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
        else:
            print("El saldo no puede ser negativo.")

    def extraer(self, cantidad):
        if self.saldo > cantidad:
            self.saldo -= cantidad
        else:
            print("No hay suficiente saldo")

    def obtener_saldo(self):
        return f"Saldo actual: ${self.saldo}"

    def __add__(self, otra):
        if self.saldo >= 10:
            self.saldo -= 10
            otra.saldo += 10
        return self

    def __str__(self, otra):
        if self.saldo >= 10:
            self.saldo -= 10
            otra.saldo += 10
        return self


class CuentaAhorro(Cuenta):
    def __init__(self, tasa_interes: float):
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes

class CuentaCorriente(Cuenta):
    def __init__(self, limite_descubierto: float):
        self.limite_descubierto = limite_descubierto


    def permitir_descubierto(self):
        if self.saldo < 0 and abs(self.saldo) <= self.limite_descubierto:
            print("Descubierto permitido.")
        elif self.saldo < 0:
            print(f" {self.titular} excede el límite de descubierto")
        else:
            print(f"{self.titular} no está en descubierto")


class Banco:
    def __init__(self, nombre: str, clientes: list, total_depositado: float):
        self.nombre = nombre
        self.clientes = clientes
        self.total_depositado = total_depositado

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)

    def deposito_total_del_dia(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.saldo
        return total

    def resumen_del_dia(self):
        print(f"Banco: {self.nombre}")
        print(f"Clientes: {len(self.clientes)}")
        print(f"Total depositado: {self.deposito_total_del_dia():.2f}")


def mostrar_menu():
    print("\n--- MENÚ DEL SISTEMA BANCARIO ---")
    print("1. Crear Cuenta (ahorro o corriente)")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Transferir Dinero")
    print("5. Consultar Saldo")
    print("6. Aplicar Interés (solo ahorro)")
    print("7. Permitir Descubierto (solo corriente)")
    print("8. Resumen del Día")
    print("9. Salir")

#Funciones para el menu
#1
clientes = []

def crear_cuenta():
    tipo = input("¿Qué tipo de cuenta quieres crear? (ahorro/corriente): ").lower()
    titular = input("Nombre del titular: ")
    saldo = float(input("Saldo inicial: "))

    if tipo == "ahorro":
        tasa = float(input("Tasa de interés (ej. 0.05 para 5%): "))
        cuenta = CuentaAhorro(titular, saldo, tasa)
    elif tipo == "corriente":
        limite = float(input("Límite de descubierto permitido: "))
        cuenta = CuentaCorriente(titular, saldo, limite)
    else:
        print("Tipo de cuenta no válido.")
        return

    clientes.append(cuenta)
    print(f"Cuenta creada para {titular}.")

#2
def depositar_dinero():
    nombre = input("Nombre del titular de la cuenta: ")
    dinero = float(input("Ingrese la cantidad de dinero que quiere depositar: "))
    for cuenta in clientes:
        if cuenta.titular == nombre:
            cuenta.depositar(dinero)
            print(f"Se depositaron ${dinero:.2f} en la cuenta de {nombre}.")
            return


#3
def retirar_dinero():
    nombre = input("Nombre del titular de la cuenta: ")
    dinero = float(input("Ingrese la cantidad de dinero que quiere retirar: "))
    for cuenta in clientes:
        if cuenta.titular == nombre:
            cuenta.retirar(dinero)
            print(f"Se retiraron ${dinero:.2f} en la cuenta de {nombre}.")
            return

#4
def transferir_dinero():
    cuentaOrigen = input("Nombre del titular de la cuenta: ")
    cuentaDestino = input("Nombre del titular de la cuenta a tranferir: ")
    for cuenta in clientes:
        if cuenta.titular == cuentaOrigen:
            cuenta.__add__(cuentaDestino)
        elif cuentaOrigen == cuentaDestino:
            print("Por favor selecciona cuentas diferentes.")
            return

#5
def consultar_saldo():
    nombre = input("Nombre del titular de la cuenta: ")
    for cuenta in clientes:
        if cuenta.titular == nombre:
            cuenta.consultar_saldo()
        else:
            print("No se ha encontrado la cuenta")

#6
def aplicar_interes():
    for cuenta in clientes:
        if isinstance(cuenta, CuentaAhorro):
            cuenta.aplicar_interes()
            print(f"Interés aplicado a la cuenta de {cuenta.titular}.")


#7
def permitir_descubierto():
    for cuenta in clientes:
        if isinstance(cuenta, CuentaCorriente):
            cuenta.permitir_descubierto()

#8
def obtener_resumen_del_dia():
    obtener_resumen_del_dia()






# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        depositar_dinero()
    elif opcion == "3":
        pass


    else:
        print("Opción no válida. Intenta de nuevo.")



