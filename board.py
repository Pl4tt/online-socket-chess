from piece import King, Queen, Rook, Bishop, Knight, Pawn


class Board:
    def __init__(self, wp_name: str, bp_name: str) -> None:
        self.wp_name = wp_name
        self.bp_name = bp_name

        self.previous_move = None
        self.turn = wp_name

        self.board = [[None for _ in range(8)] for _ in range(8)]
        
        # Black 1st row
        self.board[0][0] = Rook(0, 0, "b", "")
        self.board[0][1] = Knight(0, 1, "b", "")
        self.board[0][2] = Bishop(0, 2, "b", "")
        self.board[0][3] = King(0, 3, "b", "")
        self.board[0][4] = Queen(0, 4, "b", "")
        self.board[0][5] = Bishop(0, 5, "b", "")
        self.board[0][6] = Knight(0, 6, "b", "")
        self.board[0][7] = Rook(0, 7, "b", "")
        # Black pawn row
        self.board[1] = [Pawn(1, i, "b", "") for i in range(8)]

        # White 1st row
        self.board[7][0] = Rook(7, 0, "w", "")
        self.board[7][1] = Knight(7, 1, "w", "")
        self.board[7][2] = Bishop(7, 2, "w", "")
        self.board[7][4] = Queen(7, 3, "w", "")
        self.board[7][3] = King(7, 4, "w", "")
        self.board[7][5] = Bishop(7, 5, "w", "")
        self.board[7][6] = Knight(7, 6, "w", "")
        self.board[7][7] = Rook(7, 7, "w", "")
        # White pawn row
        self.board[6] = [Pawn(6, i, "w", "") for i in range(8)]
    
    def move(self, p_name: str, pos_before: tuple[int], pos_after: tuple[int]) -> bool:
        bx, by = pos_before
        ax, ay = pos_after

        if p_name == self.wp_name:
            if self.board[bx][by].color == "w":
                if self.board[bx][by].move(*pos_after):
                    self.board[ax][ay] = self.board[bx][by]
                    self.board[bx][by] = None
                    return True

        if p_name == self.bp_name:
            if self.board[bx][by].color == "b":
                if self.board[bx][by].move(*pos_after):
                    self.board[ax][ay] = self.board[bx][by]
                    self.board[bx][by] = None
                    return True
        
        return False

    def draw(self) -> None:
        pass
