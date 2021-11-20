"""
Cree una clase PilaFrontera con los métodos:
    • constructor: Incializa un atributo frontera como una lista vacia
    • vacia: Retorna True si la lista frontera está vacía, False en caso contrario
    • adicionar: recibe un nodo y lo adiciona al final de la lista.
      Utilice el médoto append
    • contiene_estado: recibe un estado y recorre la lista frontera buscando el estado.
      Devuelve True si el estado está en la frontera y False en caso contrario.
    • eliminar: Remueve y devuelve el último elemento en la lista.
      Si la lista está vacía retorna una excepción con el mensaje así:
"""

from nodo import Nodo


class PilaFrontera:
    def __init__(self) -> None:
        self.frontera = list()    

    def vacia(self) -> bool:
        return not len(self.frontera)

    def adicionar(self, nodo) -> None:
        self.frontera.append(nodo)

    def contiene_estado(self, estado) -> bool:
        for elemento in self.frontera:
            if elemento.estado == estado:
                return True
        return False

    def eliminar(self) -> Nodo:
        if self.vacia():
            raise Exception("Frontera vacía")
        return self.frontera.pop()