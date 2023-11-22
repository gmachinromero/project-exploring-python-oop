
# 1. Clases
class Persona:
    # Atributo de instancia
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    # Atributo de instancia
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"- Cliente: {self.nombre} {self.apellido} \n- Balance de Cuenta {self.numero_cuenta}: {self.balance} €"

    def consultar_saldo(self):
        print(f"El balance actual es de {self.balance} €.")
        print("")

    def depositar(self):
        cantidad = float(input("¿Qué cantidad quiere depositar?: "))
        self.balance = self.balance + cantidad
        print(f"Ha depositado {cantidad} €. El balance actual es de {self.balance} €.")
        print("")

    def retirar(self):
        cantidad = float(input("¿Qué cantidad quiere depositar?: "))
        if cantidad > self.balance:
            print(f"Fondos insuficentes: {self.balance} €")
        else:
            self.balance = self.balance - cantidad
            print(f"Ha retirado {cantidad} €. El balance actual es de {self.balance} €.")
        print("")


# 2. Funciones
def crear_cliente():
    nombre = str(input("Introduzca el nombre del cliente: "))
    apellido = str(input("Introduzca el apellido del cliente: "))
    numero_cuenta = str(input("Introduzca el numero_cuenta del cliente: "))
    balance = float(input("Introduzca el balance del cliente: "))
    cliente = Cliente(nombre, apellido, numero_cuenta, balance)
    return cliente


def opciones_usuario():
    print("Las opciones disponible son: ")
    print(40*"-")
    print("[1]: Consultar saldo")
    print("[2]: Ingresar una cantidad")
    print("[3]: Retirar una cantidad")
    print("[4]: Finalizar ejecución")
    print("")

    opcion_usuario = 0
    lim_inf = 1
    lim_superior = 4

    while opcion_usuario not in range(lim_inf, lim_superior+1):
        opcion_usuario = int(input("¿Qué acción quiere realizar?: "))
        if opcion_usuario not in range(lim_inf, lim_superior+1):
            print(f"Valor no válido, introduzca una opción del {lim_inf} al {lim_superior}.")
        else:
            pass

    return opcion_usuario


def iniciar_cajero():

    # Crear cliente
    cliente = crear_cliente()
    print(cliente)

    # Incializar cajero
    while True:

        # Solicitar acción del usuario
        opcion_usuario = opciones_usuario()

        if opcion_usuario == 1:
            # Consultar saldo
            cliente.consultar_saldo()
        elif opcion_usuario == 2:
            # Ingresar una cantidad
            cliente.depositar()
        elif opcion_usuario == 3:
            # Retirar una cantidad
            cliente.retirar()
        else:
            # Finalizar ejecución
            print("Saliendo del Python-Bank.")
            break


# 3. Inicializar cajero
if __name__ == "__main__":
    iniciar_cajero()
