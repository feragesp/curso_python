# game.py

from board import Board
from player import HumanPlayer, CPUPlayer
from config import P_CPU, P_PLAYER, CPU_LEVEL
from utils import terminal_clean

class Game:
    
    terminal_clean()
    
    def __init__(self):
        self._board = Board()
        self._human = HumanPlayer(input("Tu nombre: "), P_PLAYER)
        self._dificulty = self.choose_dificulty()
        self._cpu = CPUPlayer(P_CPU, self._dificulty, self._human._piece)
        self._shift = 1
        self._finished = False

    def choose_dificulty(self):
        while True:
            level = input("Elige dificultad [easy], [normal], [hard]: ").strip().lower()
            if level in CPU_LEVEL:
                return level
            print("-> [ERROR] Elige entre 'easy', 'normal', 'hard'")

    def to_play(self):
        while not self._finished:
            self._board.print_board() # Imprimir talero
            
            actual = self._human if self._shift % 2 != 0 else self._cpu
            """
            Alterna turno:
            - Si el turno es par, juega el humano
            - Si el turno es impar, juego el CPU
            """
            column = actual.choose_column(self._board)
            self._board.insert_piece(column, actual._piece)

            if self._board.check_win(actual._piece):
                self._board.print_board()
                print(f"{actual._name} ({actual._piece}) WIN")
                print(f"Se ha jugado: {self._shift} turnos")
                self._finished = True
            elif self._board.check_full():
                self._board.print_board()
                print("EMPATE PRINGADILL@")
                print(f"Se ha jugado: {self._shift} turnos")
                self._finished = True
            else:
                self._shift += 1