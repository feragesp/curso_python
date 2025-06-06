import sys

def rectangle(x, y):
    """
    Dibujar un rectangulo de X columnas e Y filas
    X: Int
    Y: Int
    No retorna nada
    """
    if (x <= 0 or y <= 0):
        return
    
    for row in range(y):
        if (row == 0 or row == y - 1):
            if (x == 1):
                print('o')
            else:
                print('o' + '-' * (x - 2) + 'o')
        else:
            if (x == 1):
                print('|')
            else:
                print('|' + ' ' * (x - 2) + '|')

def main():
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rectangle(x,y)
        except ValueError:
            print("Los argumentos deben ser Int")
    else:
        print("Uso: python main.py <ancho> <alto>")

if __name__ == "__main__":
    main()