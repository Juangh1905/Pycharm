class Cuenta:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def extraer(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad

    def obtener_saldo(self):
        return f"Saldo actual: ${self.saldo:.2f}"

    def __add__(self, otra):
        if isinstance(otra, Cuenta) and self.saldo >= 10:
            self.saldo -= 10
            otra.saldo += 10
        return self

    def __sub__(self, otra):
        if isinstance(otra, Cuenta) and otra.saldo >= 5:
            otra.saldo -= 5
            self.saldo += 5
        return self


class CuentaAhorro(Cuenta):
    def __init__(self, titular: str, saldo: float, tasa_interes: float):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes


class CuentaCorriente(Cuenta):
    def __init__(self, titular: str, saldo: float, limite_descubierto: float):
        super().__init__(titular, saldo)
        self.limite_descubierto = limite_descubierto

    def permitir_descubierto(self):
        if self.saldo < 0 and abs(self.saldo) <= self.limite_descubierto:
            print("Descubierto permitido.")
        elif self.saldo < 0:
            print(f"{self.titular} excede el límite de descubierto")
        else:
            print(f"{self.titular} no está en descubierto")


class Banco:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.clientes = []
        self.total_depositado = 0

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.titular} creado.")

    def eliminar_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            print(f"Cliente {cliente.titular} eliminado.")
        else:
            print("Cliente no encontrado.")

    def deposito_total_del_dia(self):
        total = 0
        for cliente in self.clientes:
            total += cliente.saldo
        return total

    def resumen_del_dia(self):
        print(f"Banco: {self.nombre}")
        print(f"Clientes: {len(self.clientes)}")
        print(f"Total depositado: ${self.deposito_total_del_dia():.2f}")
        for c in self.clientes:
            print(f"{c.titular}: ${c.saldo:.2f}")


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


banco = Banco("Banco Talavera")


def crear_cuenta():
    tipo = input("Tipo de cuenta (ahorro/corriente): ").lower()
    titular = input("Titular: ")
    saldo = float(input("Saldo inicial: "))
    if tipo == "ahorro":
        tasa = float(input("Tasa de interés: "))
        cuenta = CuentaAhorro(titular, saldo, tasa)
    elif tipo == "corriente":
        limite = float(input("Límite de descubierto: "))
        cuenta = CuentaCorriente(titular, saldo, limite)
    else:
        print("Tipo no válido.")
        return
    banco.agregar_cliente(cuenta)
    print("Cuenta creada.")


def depositar_dinero():
    nombre = input("Titular: ")
    cantidad = float(input("Cantidad a depositar: "))
    for c in banco.clientes:
        if c.titular == nombre:
            c.depositar(cantidad)
            print("Depósito realizado.")
            return
    print("Cuenta no encontrada.")


def retirar_dinero():
    nombre = input("Titular: ")
    cantidad = float(input("Cantidad a retirar: "))
    for c in banco.clientes:
        if c.titular == nombre:
            c.extraer(cantidad)
            print("Retiro realizado.")
            return
    print("Cuenta no encontrada.")


def transferir_dinero():
    origen = input("Titular origen: ")
    destino = input("Titular destino: ")
    for c1 in banco.clientes:
        if c1.titular == origen:
            for c2 in banco.clientes:
                if c2.titular == destino and origen != destino:
                    c1 + c2
                    print("Transferencia realizada.")
                    return
    print("Cuentas no válidas.")


def consultar_saldo():
    nombre = input("Titular: ")
    for c in banco.clientes:
        if c.titular == nombre:
            print(c.obtener_saldo())
            return
    print("Cuenta no encontrada.")


def aplicar_interes():
    for c in banco.clientes:
        if isinstance(c, CuentaAhorro):
            c.aplicar_interes()
            print(f"Interés aplicado a {c.titular}.")


def permitir_descubierto():
    for c in banco.clientes:
        if isinstance(c, CuentaCorriente):
            c.permitir_descubierto()


def obtener_resumen_del_dia():
    banco.resumen_del_dia()


while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        depositar_dinero()
    elif opcion == "3":
        retirar_dinero()
    elif opcion == "4":
        transferir_dinero()
    elif opcion == "5":
        consultar_saldo()
    elif opcion == "6":
        aplicar_interes()
    elif opcion == "7":
        permitir_descubierto()
    elif opcion == "8":
        obtener_resumen_del_dia()
    elif opcion == "9":
        print("Fin del programa.")
        break
    else:
        print("Opción no válida.")
