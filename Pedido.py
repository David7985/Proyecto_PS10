from ElementoMenu import CrearMenu
from typing import List

class Pedido:
    def __init__(self):
        self.menus = []  # Lista de menús en el pedido

    def agregar_menu(self, menu: CrearMenu): # Agrega un menú al pedido.
        for m in self.menus:
            if m.nombre.lower() == menu.nombre.lower():
                m.cantidad += 1  # Si el menú ya existe, incrementa su cantidad.
                return
        menu.cantidad = 1  # Asumimos que al agregar un menú nuevo, la cantidad inicial es 1
        self.menus.append(menu)

    def eliminar_menu(self, nombre_menu: str): # Elimina un menú del pedido por su nombre.
        for i, m in enumerate(self.menus):
            if m.nombre.lower() == nombre_menu.lower():
                if m.cantidad > 1:
                    m.cantidad -= 1
                else:
                    del self.menus[i]
                return True
        return False

    def mostrar_pedido(self) -> List[CrearMenu]: # Retorna la lista de menús en el pedido.
        return self.menus

    def calcular_total(self) -> int:
        total = 0.0
        for menu in self.menus:
            total += menu.precio * menu.cantidad
        return total

    def limpiar_pedido(self): # Limpia todos los menús del pedido.
        self.menus.clear() 
