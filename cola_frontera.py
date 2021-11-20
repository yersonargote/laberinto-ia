"""Cola frontera"""

from pila_frontera import PilaFrontera
from Nodo import Nodo

class ColaFrontera(PilaFrontera):

    def eliminar(self) -> Nodo:
        return self.frontera.pop(0)