from __future__ import annotations
import os
from concurrent.futures.thread import ThreadPoolExecutor
import pygame

from constants import BLACK, PIECE_GREEN_BG, RED, TILE_LENGTH
from utils import coordinate_builder


king_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((0, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
king_img_w.set_colorkey(BLACK)
king_img_ws = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((0, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
king_img_ws.set_colorkey(BLACK)
king_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((0, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
king_img_b.set_colorkey(PIECE_GREEN_BG)
king_img_bs = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((0, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
king_img_bs.set_colorkey(BLACK)

queen_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((256, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
queen_img_w.set_colorkey(BLACK)
queen_img_ws = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((256, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
queen_img_ws.set_colorkey(BLACK)
queen_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((256, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
queen_img_b.set_colorkey(PIECE_GREEN_BG)
queen_img_bs = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((256, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
queen_img_bs.set_colorkey(BLACK)

rook_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((384, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
rook_img_w.set_colorkey(BLACK)
rook_img_ws = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((384, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
rook_img_ws.set_colorkey(BLACK)
rook_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((384, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
rook_img_b.set_colorkey(PIECE_GREEN_BG)
rook_img_bs = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((384, 256, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
rook_img_bs.set_colorkey(BLACK)

bishop_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((128, 0, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
bishop_img_w.set_colorkey(BLACK)
bishop_img_ws = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((128, 0, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
bishop_img_ws.set_colorkey(BLACK)
bishop_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((256, 0, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
bishop_img_b.set_colorkey(PIECE_GREEN_BG)
bishop_img_bs = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((256, 0, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
bishop_img_bs.set_colorkey(BLACK)

knight_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((128, 128, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
knight_img_w.set_colorkey(BLACK)
knight_img_ws = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((128, 128, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
knight_img_ws.set_colorkey(BLACK)
knight_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((256, 128, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
knight_img_b.set_colorkey(PIECE_GREEN_BG)
knight_img_bs = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((256, 128, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
knight_img_bs.set_colorkey(BLACK)

pawn_img_w = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "white_pieces.png")).subsurface((0, 384, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
pawn_img_w.set_colorkey(BLACK)
pawn_img_ws = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((0, 384, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
pawn_img_ws.set_colorkey(BLACK)
pawn_img_b = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "black_pieces.png")).subsurface((0, 384, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
pawn_img_b.set_colorkey(PIECE_GREEN_BG)
pawn_img_bs = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "selected_pieces.png")).subsurface((0, 384, 128, 128)), (TILE_LENGTH, TILE_LENGTH))
pawn_img_bs.set_colorkey(BLACK)

valid_move_dot = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "valid_move_dot.png")), (TILE_LENGTH, TILE_LENGTH))

images = {
    "king_w": king_img_w,
    "king_b": king_img_b,
    "queen_w": queen_img_w,
    "queen_b": queen_img_b,
    "rook_w": rook_img_w,
    "rook_b": rook_img_b,
    "bishop_w": bishop_img_w,
    "bishop_b": bishop_img_b,
    "knight_w": knight_img_w,
    "knight_b": knight_img_b,
    "pawn_w": pawn_img_w,
    "pawn_b": pawn_img_b,
    
    "king_ws": king_img_ws,
    "king_bs": king_img_bs,
    "queen_ws": queen_img_ws,
    "queen_bs": queen_img_bs,
    "rook_ws": rook_img_ws,
    "rook_bs": rook_img_bs,
    "bishop_ws": bishop_img_ws,
    "bishop_bs": bishop_img_bs,
    "knight_ws": knight_img_ws,
    "knight_bs": knight_img_bs,
    "pawn_ws": pawn_img_ws,
    "pawn_bs": pawn_img_bs,
}



class Piece:
    def __init__(self, row: int, col: int, color: str, piece_name: str) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.piece_name = piece_name
        self.img_name = f"{piece_name}_{color}"
        self.is_selected = False
        self.valid_moves = set()

        self.first_move = True
    
    def select(self, window: pygame.Surface=None) -> None:
        self.is_selected = True

        if window is not None:
            self.draw(window)

    def unselect(self, window: pygame.Surface=None) -> None:
        self.is_selected = False
        if window is not None:
            self.draw(window)

    def one_direction(self, board: list[list[Piece, None]], candidates: set, row_change: int, col_change: int) -> None:
        row, col = self.row, self.col

        while row >= 0 and col < len(board[row]):
            row += row_change
            col += col_change

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
                return

            if board[row][col] is None:
                candidates.add((row, col))
            elif board[row][col].color != self.color:
                candidates.add((row, col))
                return
            elif board[row][col].color == self.color:
                return

    def update_valid_moves(self, board: list[list[Piece, None]]) -> None:
        self.valid_moves = self.all_valid_moves(board)

    def move(self, row: int, col: int, board: list[list[Piece, None]], window: pygame.Surface=None) -> bool:
        if (row, col) not in self.valid_moves:
            return False
            
        self.first_move = False
        
        board[row][col] = board[self.row][self.col]
        board[self.row][self.col] = None
        
        self.row = row
        self.col = col

        self.is_selected = False

        if window is not None:
            self.draw(window)

        return True
    
    def draw(self, window: pygame.Surface) -> tuple[int]:
        x, y = coordinate_builder(self.row, self.col)
        
        if not self.is_selected:
            img = images.get(self.img_name)
        else:
            img = images.get(self.img_name + "s")

            for row, col in self.valid_moves:
                dotx, doty = coordinate_builder(row, col)
                
                dot_rect = valid_move_dot.get_rect()
                dot_rect.left = dotx
                dot_rect.top = doty

                window.blit(valid_move_dot, dot_rect)
    
        img_rect = img.get_rect()
        img_rect.left = x
        img_rect.top = y

        window.blit(img, img_rect)



class King(Piece):
    def all_valid_moves(self, board: list[list[Piece, None]]) -> set:
        candidates = set()

        for x in range(self.row-1, self.row+2):
            for y in range(self.col-1, self.col+2):
                if x < len(board) and y < len(board[x]) and (x, y) != (self.row, self.col) and (board[x][y] is None or board[x][y].color != self.color):
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        candidates.add((x, y))

        return candidates

class Queen(Piece):
    def all_valid_moves(self, board: list[list[Piece, None]]) -> set:
        candidates = set()

        change = [-1, 0]

        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(4):
                change[int(i!=0)] *= -1

                executor.submit(self.one_direction, board, candidates, *change)

                change[int(i!=0)] *= -1

                executor.submit(self.one_direction, board, candidates, *change)
                
                if i == 0:
                    change = change[::-1]
                if i == 1:
                    change[0] = -1
                
                change[0] *= -1


        return candidates

class Rook(Piece):
    def all_valid_moves(self, board: list[list[Piece, None]]) -> set:
        candidates = set()

        change = [1, 0]

        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(1, 5):
                executor.submit(self.one_direction, board, candidates, *change)
                
                change = change[::-1]
                if i%2 == 0:
                    change[0] *= -1

        return candidates

class Bishop(Piece):
    def all_valid_moves(self, board: list[list[Piece, None]]) -> set:
        candidates = set()

        change = [1, 1]

        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(1, 5):
                executor.submit(self.one_direction, board, candidates, *change)
                
                change[1] *= -1
                if i%2 == 0:
                    change[0] *= -1

        return candidates

class Knight(Piece):
    def all_valid_moves(self, board: list[list[Piece, None]]) -> set:
        candidates = set()

        change = [1, -2]

        for i in range(8):
            if i%2 == 0:
                change = change[::-1]
            if i%4 == 0:
                change[0] *= -1

            x = self.row + change[0]
            y = self.col + change[1]

            if x >= 0 and x < len(board) and y >= 0 and y < len(board[x]):
                if board[x][y] is None or board[x][y].color != self.color:
                    candidates.add((x, y))
            
            change[int(i%4 in (0, 1))] *= -1

        return candidates

class Pawn(Piece):
    def all_valid_moves(self, board: list[list[Piece, None]]) -> set:
        candidates = set()
    
        direction = -1 if self.color == "w" else 1

        for i in range(1, 2+int(self.first_move)):  # going forward
            if self.row + i*direction >= 0 and self.row + i*direction < len(board):
                if board[self.row+i*direction][self.col] is None:
                    candidates.add((self.row+i*direction, self.col))
            else:
                break
        
        if self.row+1*direction < 0 or self.row+i*direction >= len(board):
            return candidates

        # diagonal kill
        if self.col + 1 < len(board[self.row+1*direction]) and board[self.row+1*direction][self.col+1] is not None and board[self.row+1*direction][self.col+1].color != self.color:
            candidates.add((self.row+1*direction, self.col+1))
        if self.col - 1 >= 0 and board[self.row+1*direction][self.col-1] is not None and board[self.row+1*direction][self.col-1].color != self.color:
            candidates.add((self.row+1*direction, self.col-1))

        return candidates

