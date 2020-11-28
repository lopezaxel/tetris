#! python3

import pygame
from pygame.locals import *

class Board:
    '''This class starts and manages the game.'''
    def __init__(self):
        self.board = self.create_board()        

    def create_board(self):
        board = []
        for n in range(20):
            line = ["", "", "", "", "", "", "", "", "", ""] 
            board.append(line)
        return board

game = Game()
