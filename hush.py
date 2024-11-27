class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_modulo(self, key):
        """Hash basado en módulo."""
        return key % self.size

    def hash_exponencial(self, key):
        """Hash basado en exponenciación."""
        return (key ** 2) % self.size

    def insertar(self, key, value, metodo):
        if metodo == "modulo":
            index = self.hash_modulo(key)
            print(f"[Modulo] Clave {key} -> Índice calculado: {index}")
        elif metodo == "exponencial":
            index = self.hash_exponencial(key)
            print(f"[Exponencial] Clave {key} -> Índice calculado: {index}")
        else:
            print("Método no válido")
            return
        
        # Manejo básico de colisiones (lineal)
        original_index = index
        iteration = 0
        while self.table[index] is not None:
            print(f"Colisión en índice {index} (Iteración {iteration}). Probando el siguiente índice...")
            index = (index + 1) % self.size
            iteration += 1
            if index == original_index:
                print("Tabla llena, no se puede insertar.")
                return
        self.table[index] = (key, value)
        print(f"Valor {value} insertado en el índice {index} después de {iteration} iteraciones.\n")

    def buscar(self, key, metodo):
        if metodo == "modulo":
            index = self.hash_modulo(key)
            print(f"[Modulo] Clave {key} -> Índice calculado: {index}")
        elif metodo == "exponencial":
            index = self.hash_exponencial(key)
            print(f"[Exponencial] Clave {key} -> Índice calculado: {index}")
        else:
            print("Método no válido")
            return "Error en búsqueda"
        
        # Manejo básico de búsqueda con manejo de colisiones
        original_index = index
        iteration = 0
        while self.table[index] is not None:
            stored_key, value = self.table[index]
            if stored_key == key:
                print(f"Clave encontrada en índice {index} después de {iteration} iteraciones.")
                return value
            print(f"No coincide en índice {index} (Iteración {iteration}). Probando el siguiente índice...")
            index = (index + 1) % self.size
            iteration += 1
            if index == original_index:
                break
        print("Clave no encontrada en la tabla.")
        return "No encontrado"

    def mostrar_tabla(self):
        print("\nEstado actual de la tabla:")
        for i, entry in enumerate(self.table):
            print(f"Índice {i}: {entry}")
        print()


def menu():
    # Crear la tabla hash con tamaño definido
    tamaño_tabla = 10
    hash_table = HashTable(tamaño_tabla)

    while True:
        print("\n--- Menú ---")
        print("1. Insertar valor")
        print("2. Buscar valor")
        print("3. Mostrar tabla")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            key = int(input("Ingresa la clave numérica (entero): "))
            value = input("Ingresa el valor asociado: ")
            metodo = input("Elige el método (modulo/exponencial): ").lower()
            hash_table.insertar(key, value, metodo)
        elif opcion == "2":
            key = int(input("Ingresa la clave a buscar (entero): "))
            metodo = input("Elige el método (modulo/exponencial): ").lower()
            resultado = hash_table.buscar(key, metodo)
            print(f"Resultado de la búsqueda: {resultado}")
        elif opcion == "3":
            hash_table.mostrar_tabla()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
