import sys

# Comentario fuera de funcion

def is_negative(n):
    """
    Función para determinar el signo del INT
    N: int
    Print: N (negativo) o P (positivo o nulo)
    No retorna
    """
    if (n < 0):
        print("N") # Print N
    else:
        print("P")

def main():
    # print(len(sys.argv))
    # print(len(sys.argv[0]))
    # print(len(sys.argv[2]))
    # print(len(sys.argv[4]))
    if len(sys.argv) < 5:
        try:
            string = str(sys.argv[0])
            print("argv0", string)
            n = int(sys.argv[1])
            is_negative(n)
        except ValueError:
             print("ERROR")
    else:
         print("ERROR")

if __name__ == "__main__":
    main()