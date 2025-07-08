import random
from board import Board
from config import ROWS, COLUMNS, EMPTY


def board_copy(board):
    return [row[:] for row in board.grid]

def cpu_easy(board):
    return random.choice(board.check_column())

def cpu_normal(board, cpu_piece, human_piece):
    """
    # Ganar si puede de forma inmediata
    # Bloquear al jugador si este va a ganar en su proxima jugada
    # Si no aplica las dos anteriores => cpu_easy
    """
    # Ganar en el siguiente turno
    for column in board.check_column():
        """
        Recorre las columnas validas
        Simula si puede ganar para columna
        Verifica si poniendo ficha en cada columna la cpu puede ganar
        """
        copy_board = Board()
        copy_board._grid = copy_board(board)
        copy_board.insert_piece(column, cpu_piece)
        if copy_board.check_win(cpu_piece):
            return column
    
    # ¿Puede ganar el jugador?
    for column in board.check_column():
        """
        Simula si el humano pone una ficha en cada columna
        Verifica si el humana gana poniendo la ficha en cada columna
        """
        copy_board = Board()
        copy_board._grid = copy_board(board)
        copy_board.insert_piece(column, human_piece)
        if copy_board.check_win(human_piece):
            return column
        
    return cpu_easy(board)

def cpu_hard(board, cpu_piece, human_piece):
    """
    # Intenta ganar en el siguiente turno
    # Si no puede ganar, bloquea al jugador si este va a ganar
    # Evalua la posicion más ventajosa para tener mejor puntuación 
    """
    # Inicializa una lista con tuplas de (Puntuacion, columna)
    best_pos = []
    for column in board.check_column():
        copy_board = Board()
        copy_board._grid  = board_copy(board)
        copy_board.insert_piece(column, cpu_piece)

        if copy_board.check_win(cpu_piece):
            return column
        
        """
        Evalua la jugada
        score(copy_board, cpu_piece) # Mide lo buena que es la jugada
        score(copy_board, human_piece) # Mide si mi jugada es buena para el humano
        Resta de los dos score
        """

def score(board, piece):
    points = 0
    grid = board.grid

    def evaluator(plays):
        """
        Evalua una lista de 4 jugadas
        asigna una puntuación dependiendo de fichas propias y espacios vacios
        """
        if plays.count(piece) == 4:
            return 100
        elif plays.count(piece) == 3 and plays.count(EMPTY) == 1:
            return 10
        elif plays.count(piece) == 2 and plays.count(EMPTY) == 2:
            return 5
        else:
            return 0
        
        # Horizontal (izquierda - derecha)
        for row in range(ROWS):
            for column in range(COLUMNS - 3):
                points += evaluator(grid[row][column:column + 4])

        # Vertical (Arriba - Abajo)
        for column in range(COLUMNS):
            for row in range(ROWS - 3):
                points += evaluator([grid[row + i][column] for i in range(4)])

        # Diagonal \
        for row in range(ROWS - 3):
            for column in (COLUMNS - 3):
                points += evaluator([grid[row + i][column + i] for i in range(4)])
        
        # Diagonal /
        for row in (3, ROWS):
            for column in range(COLUMNS - 3):
                points += evaluator([grid[row - i][column + i] for i in range(4)])

        return points