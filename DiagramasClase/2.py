
class Cliente:
    def __init__(self, codigo, dni, nombre, direccion, telefono):
        self.codigo = codigo
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.avalador = None

    def __str__(self):
        return f"Código: {self.codigo}\nDNI: {self.dni}\nNombre: {self.nombre}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

    def __str__(self):
        return f"Matrícula: {self.matricula}\nModelo: {self.modelo}\nColor: {self.color}\nMarca: {self.marca}\nGaraje: {self.garaje.nombre}"

class Reserva:
    def __init__(self, cliente, agencia, fecha_inicio, fecha_final, precio_total, entregado):
        self.cliente = cliente
        self.agencia = agencia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.precio_total = precio_total
        self.entregado = entregado

    def __str__(self):
        return f"Cliente:\n{self.cliente}\nAgencia: {self.agencia.nombre}\nFecha de inicio: {self.fecha_inicio}\nFecha final: {self.fecha_final}\nPrecio total: {self.precio_total}\nEntregado: {self.entregado}"

class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre

class Garaje:
    def __init__(self, nombre):
        self.nombre = nombre

# Ejemplo de uso:

cliente1 = Cliente("001", "12345678A", "Juan Perez", "Calle A, 123", "123456789")
cliente2 = Cliente("002", "87654321B", "Maria Rodriguez", "Calle B, 456", "987654321")
cliente2.avalador = cliente1

coche1 = Coche("ABC123", "Sedan", "Rojo", "Toyota", Garaje("Garaje A"))
coche2 = Coche("XYZ789", "SUV", "Azul", "Ford", Garaje("Garaje B"))

agencia1 = Agencia("Agencia 1")
agencia2 = Agencia("Agencia 2")

reserva1 = Reserva(cliente1, agencia1, "2023-09-21", "2023-09-25", 500, True)
reserva2 = Reserva(cliente2, agencia2, "2023-09-22", "2023-09-26", 600, False)

# Imprimir la información de los objetos
print("Información del Cliente 1:\n", cliente1)
print("\nInformación del Cliente 2:\n", cliente2)
print("\nInformación del Coche 1:\n", coche1)
print("\nInformación del Coche 2:\n", coche2)
print("\nInformación de la Reserva 1:\n", reserva1)
print("\nInformación de la Reserva 2:\n", reserva2)
