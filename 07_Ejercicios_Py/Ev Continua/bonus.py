import sys

def rectangle(x, y, string):
    """
    Crea un rectangulo donde X es el numero de Columnas e Y el numero de files y STRING tipo de de rectangulo
    X: Int
    Y: Int
    String: Str (A, B, C)
    """
    if ((x < 1 or y < 1) or (string != 'A' and string != 'B' and string != 'C')):
        print("ERROR")
        return
    for row in range(y):
        if (string == "A"): # CASO A
            if (row == 0 or row == (y - 1)):
                # Primera y Última fila
                if (x == 1):
                    print('o')
                else:
                    print("o" + '-' * (x - 2) + "o")
            else:
                # Filas intermedias
                if (x == 1):
                    print('|')
                else:
                    print("|" + " " * (x - 2) + "|")
        elif (string == "B"): # CASO B
            if (row == 0 or row == (y - 1)):
                # Primera y ultima fila
                if (x == 1):
                    print("B")
                else:
                    print("B" + "/" * (x - 2) + "B")
            else:
                # Filas intermedias
                if (x == 1):
                    print("/")
                else:
                    print("/" + " " * (x - 2) + "/")
        else: # CASO C
            if (row == 0 or row == (y - 1)):
                # Primera y utlima linea
                if (x == 1):
                    print("0")
                elif (x == 2):  # xx
                    print("xx")
                elif (x == 3): # x0x
                    print("x0x")
                else:
                    print("0x" + "A" * (x - 4) + "x0")
            else:
                # Filas intermedias
                if (x == 1):
                    print("x")
                elif (x == 2):  # xx
                    print("xx")
                elif (x == 3): # x0x
                    print("x0x")
                else:
                    print("x" + "0" +  "B" * (x - 4) + "0" + "x") # ERROR



def main():
    if len(sys.argv) == 4:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            string = str(sys.argv[3])
            rectangle(x, y, string)
        except ValueError:
            print("Los ARGV tienen que ser Ints (1, 2) y STR (3)")
    else:
        print("Uso: python bonus.py <ancho> <alto> <tipo rect>")

if __name__ == "__main__":
    main()
