# board.py

from config import (
    ROWS, 
    COLUMNS, 
    EMPTY, 
    P_PLAYER, 
    P_CPU,
)

from utils import terminal_clean

class Board:
    """
    Constructor de tablero:
    - Imprime el tablero
    - Insertar ficha
    - check de columnas validas
    - revisar si lleno
    - comprobar victoria
    """

    def __init__(self):
        # self._grid = [
        #     [
        #         EMPTY # "."
        #         # Rellena columnas de "."
        #         for _ in range(COLUMNS)
        #     ]
        #     # Salta a la siguiente fila
        #     for _ in range(ROWS)
        # ]
        self._grid = [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


    def print_board(self):
        # Crear funcion utils limpiar pantalla
        terminal_clean()
        print(" " + " ".join(str(i) for i in range(COLUMNS))) # Imprime en string la iteracion de las columnas
        
        for row in self._grid: # Imprime la lista sin los corchetes y añade un espacio al inicio
            print(" " + " ".join(row))
        print()


    def insert_piece(self, column, piece):
        """
        Invertimos las rows donde row[0] => row[ROWS]
        para poder poner la pieza de abajo hacia arriba
        Comprobamos si en cada row esta vacio o esta lleno
        """

        for row in reversed(range(ROWS)):
            if self._grid[row][column] == EMPTY:
                self._grid[row][column] = piece
                return True
        return False


    def valid_column(self, column):
        """
        Devuelve si la columna es valida para insertar pieza
        - column: tiene que estar comprendido entre un numero que 0 es el menor numero que hay y menor que COLUMNS
        - ADEMAS (and): la columna tiene que estar vacia
        """
        return 0 <= column < COLUMNS and self._grid[0][column] == EMPTY
        # into_range = 0 <= column < COLUMNS
        # empty_space = self._grid[0][column] == EMPTY
        # # result = into_range and empty_space
        # # return result
        # if (into_range == True) and (empty_space == True):
        #     return True
        # else:
        #     return False 


    def check_columns(self):
        """
        Devuelve una lista de numeros donde de puede insertar pieza
        """
        # column = []
        # for n_col in range(COLUMNS):
        #     if self.valid_column(n_col):
        #         column.append(n_col)
        # return column
        return [n_col for n_col in range(COLUMNS) if self.valid_column(n_col)]

    def check_full(self):
        """
        Checkear si el tablero esta lleno
        - Si esta lleno => TRUE
        - ELSE => FALSE

        all: devuelve TRUE si todas las columnas estan llenas
        self._grid != EMPTY: Comprueba si esta vacia
        for column in range: Recorre todas las columnas
        """
        # for column in range(COLUMNS):
        #     if self._grid[0][column] == EMPTY:
        #         return False
        # return True

        return all(self._grid[0][column] != EMPTY for column in range(COLUMNS))


    def check_win(self, piece):

        grid = self._grid

        # Comprobacion Horizontal (-)
        for row in range(ROWS):
            for column in range(COLUMNS - 3):
                """
                Recorre todas las rows y las columns hasta 4 antes del final
                Comprobamos si hay 4 fichas seguidas en horizontal
                grid[row][column], grid[row][column+1], grid[row][column+2], grid[row][column+3] 
                """
                # con = True # Coincidencia de piezas
                # for i in range(4): # columnas en una misma row
                #     if grid[row][column + i] != piece: # Si cualquier columna no tiene la pieza
                #         con = False # NO EXISTE COINCIDENCIA
                #         break # Sal del bucle

                # if con: # Si coincidencia de pieza == TRUE
                #     return True # Devuelve True
                
                if all(grid[row][column + i] == piece for i in range(4)): 
                    return True

        # Comprobacion en vertical (|)
        for row in range(ROWS - 3):
            for column in range(COLUMNS):
                if all(grid[row + i][column] == piece for i in range(4)): 
                    return True
        
        # Comprobacion en diagonal descendente (\)
        for row in range(ROWS - 3):
            for column in range(COLUMNS - 3):
                if all(grid[row + i][column + i] == piece for i in range(4)): 
                    return True
        
        # Comprobacion en diagonal ascendete (/)
        for row in range(3, ROWS):
            for column in range(COLUMNS - 3):
                if all(grid[row - i][column + i] == piece for i in range(4)): 
                    return True

        return False





if __name__ == '__main__':
    board = Board()
    print(board._grid)
    board.print_board()