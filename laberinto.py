from nodo import Nodo
from pila_frontera import PilaFrontera

class Laberinto:
    def __init__(self, archivo) -> None:
        
        # leer el archivo y configurar el alto y el ancho del laberinto
        with open(archivo) as f:
            contenido = f.read()
            type(contenido)

        # Validar inicio y objetivo
        if contenido.count("A") != 1:
            raise Exception("El laberinto debe tener solo un punto de inicio")
        if contenido.count("B") != 1:
            raise Exception("El laberinto debe tener solo un punto de salida")

        # Calcular el alto y el ancho del laberinto
        contenido = contenido.splitlines()
        self.alto = len(contenido)
        self.ancho = max(len(line) for line in contenido)

        # Calcular los muros del laberinto
        self.muros = []
        for i in range(self.alto):
            fila = []
            for j in range(self.ancho):
                try:
                    if contenido[i][j] == "A":
                        self.inicio = (i, j)
                        fila.append(False)
                    elif contenido[i][j] == "B":
                        self.objetivo = (i, j)
                        fila.append(False)
                    elif contenido[i][j] == " ":
                        fila.append(False)
                    else:
                        fila.append(True)
                except IndexError:
                    fila.append(False)
            self.muros.append(fila)
        self.solucion = None

    def imprimir(self):
        solucion = self.solucion[1] if self.solucion is not None else None
        print()
        for i, fila in enumerate(self.muros):
            for j, columna in enumerate(fila):
                if columna:
                    print("█", end="")
                elif (i, j) == self.inicio:
                    print("A", end="")
                elif (i, j) == self.objetivo:
                    print("B", end="")
                elif solucion is not None and (i, j) in solucion:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def hijos(self, estado):
        """
            Devuelve una lista resultado de tuplas donde cada tupla es una acción y una
            celda vacia en el laberinto a la que se puede llegar desde el estado actual. 
            Cada tupla contiene el nombre de la accion y la coordenada (r,c) de una celda que no es un muro.
        """
        fila, columna = estado
        candidatos = [
            ("arriba", (fila - 1, columna)),
            ("abajo", (fila + 1, columna)),
            ("izquierda", (fila, columna - 1)),
            ("derecha", (fila, columna + 1)),
        ]

        # TODO: Cree una lista resultado para almacenar los nodo hijos.
        resultado = []

        # Recorra la lista de tuplas candidatos y verifique que la acción es posible
        # (este dentro de los limites del laberinto) y que no sea un muro.
        # Return la lista resultado.
        for accion, coordenada in candidatos:
            if self.es_posible(coordenada):
                if not self.muros[coordenada[0]][coordenada[1]]:
                    resultado.append((accion, coordenada))
        return resultado


    def es_posible(self, coordenada):
        """
            Devuelve True si la coordenada esta dentro de los limites del laberinto.
        """
        return 0 <= coordenada[0] < self.alto and 0 <= coordenada[1] < self.ancho


    def resolver(self):
        # Guardar el numero de estados explorados
        # TODO: Cree un atributo entero para Guardar los nodos explorados
        self.num_explorados = 0
        num_nodos_exp = 0

        # Inicializar la frontera en la posición inicial
        # TODO: Cree el nodo inicial llamando al contructor de Nodo enviando los párametros adecuados.
        # Recuerde que en el constructor de Laberintos se inicializó un atributo inicio.
        inicio = Nodo(self.inicio, None, None)

        # TODO: cree una pila frontera y adicione el nodo que creo en el paso anterior.
        frontera = PilaFrontera()
        # frontera = ColaFrontera()
        frontera.adicionar(inicio)

        # Inicializar en vacio el conjunto de nodos explorados.
        self.explorados = set()

        # Iterar hasta encontrar la solución
        while True:
            # Si la frontera está vacía, entonces no hay un camino.
            if frontera.vacia():
                raise Exception("No hay solución")

            # Escoja un nodo de la frontera
            nodo = frontera.eliminar()
            self.num_explorados += 1

            # Si el nodo es el objetivo, se encontró la solución.
            if nodo.estado == self.objetivo:
                acciones = []
                celdas = []
                while nodo.padre is not None:
                    acciones.append(nodo.accion)
                    celdas.append(nodo.estado)
                    nodo = nodo.padre
                acciones.reverse()
                celdas.reverse()
                self.solucion = (acciones, celdas)
                return
            
            # Marca el nodo como explorado.
            # TODO: agregue al conjunto de explorados el nodo con el estado.
            self.explorados.add(nodo.estado)

            # Agregar los hijos al frontera
            for accion, estado in self.hijos(nodo.estado):
                if not frontera.contiene_estado(estado) and estado not in self.explorados:
                    hijo = Nodo(estado=estado, padre=nodo, accion=accion)
                    frontera.adicionar(hijo)