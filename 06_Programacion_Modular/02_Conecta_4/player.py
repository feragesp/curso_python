# player.py

from config import P_CPU, P_PLAYER
# from ai import

class Player:
    """
    # Clase Abstracta que representa a cualquier jugador, Humano / CPU
    # Name: nombre del jugador ("NAME" o "CPU")
    # Piece: simbolo que se usa en el tablero ("X" / "0")
    # El método choose_column no está implementado
    """

    def __init__(self, name, piece):
        self._name = name
        self._piece = piece
    
    def choose_column(self, board): # Obliga a las subclases a definirlo
        raise NotImplementedError

class HumanPlayer(Player):
    """
    # Hereda de Player
    # Implementa choose_column:
    # - Pedir al Humano que elija columna
    # -  Verificamos si el número es válido y si la columna está disponible
    # -  Si todo OK, return column
    """
    def choose_column(self, board):
        while True:
            try:
                column = int(input(f"{self._name} ({self._piece}) Elige columna (0-6): "))
                if board.valid_column(column):
                    return column
                print("-> [ERROR] Columna no válida")
            except ValueError:
                print("-> [ERROR] No es número")


class CPUPlayer(Player):
    """
    # Hereda de Player
    # Tiene atributos adicionales:
    # - Dificultad: "Easy" "Normal" "Hard"
    # - Piece_Human: Ficha del Humano (Analizar jugadas)
    # - Elegir column automaticamente segun dificultad
    """
    def __init__(self, piece, dificulty, piece_human):
        super().__init__("CPU", piece)
        self._dificulty = dificulty
        self._piece_human = piece_human

    def choose_column(self, board):
        input(f"CPU ({self._piece}) [{self._dificulty}]... Pulsa ENTER")
        if self._dificulty == "easy":
            pass
            # return cpu_easy(board)
        elif self._dificulty == "normal":
            pass
        else:
            pass

    

if __name__ == "__main__":
    human = HumanPlayer("Xavi", "X")
    human.choose_column(6)