import pygame

from piece import Piece


class Tile:
    def __init__(self, piece: Piece) -> None:
        self.piece = piece
    
    def draw(self) -> None:
        pass