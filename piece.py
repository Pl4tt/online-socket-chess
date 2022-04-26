import os
import pygame

from constants import BLACK, PIECE_GREEN_BG, TILE_LENGTH
from utils import coordinate_builder


king_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((0, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
king_img_w.set_colorkey(BLACK)
king_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((0, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
king_img_b.set_colorkey(PIECE_GREEN_BG)

queen_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((256, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
queen_img_w.set_colorkey(BLACK)
queen_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((256, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
queen_img_b.set_colorkey(PIECE_GREEN_BG)

rook_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((384, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
rook_img_w.set_colorkey(BLACK)
rook_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((384, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
rook_img_b.set_colorkey(PIECE_GREEN_BG)

bishop_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((128, 0, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
bishop_img_w.set_colorkey(BLACK)
bishop_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((256, 0, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
bishop_img_b.set_colorkey(PIECE_GREEN_BG)

knight_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((128, 128, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
knight_img_w.set_colorkey(BLACK)
knight_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((256, 128, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
knight_img_b.set_colorkey(PIECE_GREEN_BG)

pawn_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((0, 384, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
pawn_img_w.set_colorkey(BLACK)
pawn_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((0, 384, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
pawn_img_b.set_colorkey(PIECE_GREEN_BG)



class Piece:
    def __init__(self, row: int, col: int, color: tuple[int]) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.is_selected = False
        self.valid_moves = set()

    def update_valid_moves(self) -> None:
        self.valid_moves = self.all_valid_moves()

    def move(self, row: int, col: int) -> bool:
        if not (row, col) in self.valid_moves:
            return False
        
        self.row = row
        self.col = col

        self.update_valid_moves()

        self.draw()

        return True


class King(Piece):
    def all_valid_moves(self) -> set:
        pass
    
    def draw(self, window: pygame.Surface) -> None:
        x, y = coordinate_builder(self.row, self.col)

        if self.color == "b":
            img = king_img_b
        else:
            img = king_img_w
        
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)

class Queen(Piece):
    def all_valid_moves(self) -> set:
        pass
    
    def draw(self, window: pygame.Surface) -> None:
        x, y = coordinate_builder(self.row, self.col)

        if self.color == "b":
            img = queen_img_b
        else:
            img = queen_img_w
        
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)

class Rook(Piece):
    def all_valid_moves(self) -> set:
        pass
    
    def draw(self, window: pygame.Surface) -> None:
        x, y = coordinate_builder(self.row, self.col)

        if self.color == "b":
            img = rook_img_b
        else:
            img = rook_img_w
        
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)

class Bishop(Piece):
    def all_valid_moves(self) -> set:
        pass
    
    def draw(self, window: pygame.Surface) -> None:
        x, y = coordinate_builder(self.row, self.col)

        if self.color == "b":
            img = bishop_img_b
        else:
            img = bishop_img_w
        
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)

class Knight(Piece):
    def all_valid_moves(self) -> set:
        pass
    
    def draw(self, window: pygame.Surface) -> None:
        x, y = coordinate_builder(self.row, self.col)

        if self.color == "b":
            img = knight_img_b
        else:
            img = knight_img_w
        
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)

class Pawn(Piece):
    def all_valid_moves(self) -> set:
        pass
    
    def draw(self, window: pygame.Surface) -> None:
        x, y = coordinate_builder(self.row, self.col)

        if self.color == "b":
            img = pawn_img_b
        else:
            img = pawn_img_w
        
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)


