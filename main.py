class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, new_position):
        print(f"Piace {self.__class__.__name__}  {self.color}  move {self.position} на {new_position}")
        self.position = new_position


class Pawn(Piece):
    pass


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass

pawn = Pawn("white", (2, 'e'))
pawn.move((4, 'e'))

rook = Rook("black", (1, 'a'))
rook.move((1, 'h'))

knight = Knight("white", (1, 'b'))
knight.move((3, 'c'))

bishop = Bishop("black", (1, 'c'))
bishop.move((4, 'f'))

queen = Queen("white", (1, 'd'))
queen.move((1, 'h'))

king = King("black", (8, 'e'))
king.move((7, 'd'))
