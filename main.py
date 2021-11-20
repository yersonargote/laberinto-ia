import sys
from laberinto import Laberinto

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python laberinto.py laberinto.txt")
    laberinto = Laberinto(sys.argv[1])
    print("Laberinto: ")
    laberinto.imprimir()
    print("Resolviendo...")
    laberinto.resolver()
    print("Estados Explorados: ", laberinto.num_explorados)
    print("Solucion: ")
    laberinto.imprimir()