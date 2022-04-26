


class Piece:
    def __init__(self, row: int, col: int, color: tuple[int], img_source) -> None:  # TODO: img_source type
        self.row = row
        self.col = col
        self.color = color
        self.img_source = img_source
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

    def draw(self) -> None:
        pass


class King(Piece):
    def all_valid_moves(self) -> set:
        pass

class Queen(Piece):
    def all_valid_moves(self) -> set:
        pass

class Rook(Piece):
    def all_valid_moves(self) -> set:
        pass

class Bishop(Piece):
    def all_valid_moves(self) -> set:
        pass

class Knight(Piece):
    def all_valid_moves(self) -> set:
        pass

class Pawn(Piece):
    def all_valid_moves(self) -> set:
        pass


