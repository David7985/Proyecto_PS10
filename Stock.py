from Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        """
        Agrega un ingrediente al stock.
        Si el ingrediente ya existe, actualiza su cantidad.
        """
        for ing in self.lista_ingredientes:
            if ing.nombre.lower() == ingrediente.nombre.lower():
                ing.cantidad = str(int(ing.cantidad) + int(ingrediente.cantidad))
                return
        self.lista_ingredientes.append(ingrediente)

    def eliminar_ingrediente(self, nombre_ingrediente):
        """
        Elimina un ingrediente del stock por su nombre.
        """
        for i, ing in enumerate(self.lista_ingredientes):
            if ing.nombre.lower() == nombre_ingrediente.lower():
                del self.lista_ingredientes[i]
                return True
        return False

    def verificar_stock(self):
        """
        Verifica si hay ingredientes en el stock.
        Retorna True si hay ingredientes, False si está vacío.
        """
        return len(self.lista_ingredientes) > 0

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        """
        Actualiza la cantidad de un ingrediente en el stock.
        Retorna True si se actualizó, False si no se encontró el ingrediente.
        """
        for ing in self.lista_ingredientes:
            if ing.nombre.lower() == nombre_ingrediente.lower():
                ing.cantidad = str(nueva_cantidad)
                return True
        return False

    def obtener_ingrediente(self, nombre_ingrediente):
        """
        Busca y retorna un ingrediente por su nombre.
        Retorna None si no lo encuentra.
        """
        for ing in self.lista_ingredientes:
            if ing.nombre.lower() == nombre_ingrediente.lower():
                return ing
        return None

    def obtener_elementos_menu(self):
        """
        Retorna una lista de todos los ingredientes en el stock.
        """
        return self.lista_ingredientes

    def restar_stock(self, nombre_ingrediente, cantidad_a_restar):
        """
        Resta una cantidad específica de un ingrediente en el stock.
        Retorna True si se pudo restar, False si no hay suficiente stock.
        """
        for ing in self.lista_ingredientes:
            if ing.nombre.lower() == nombre_ingrediente.lower():
                if int(ing.cantidad) >= int(cantidad_a_restar):
                    ing.cantidad = str(int(ing.cantidad) - int(cantidad_a_restar))
                    return True
                else:
                    return False
        return False

