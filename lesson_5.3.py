class chess:
    def __init__(self, x, y, name, color, IsBlack):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.IsBlack = IsBlack
#Returns x and y
    def x_axis(self, x):
        return x
    def y_axis(self, y):
        return y
    def __repr__(self):
        self.name = self.name.lower()
        if self.name == "pawn" and self.IsBlack:
            return "♟️"
        elif self.name == "rook" and self.IsBlack:
            return "♜"
        elif self.name == "knight" and self.IsBlack:
            return "♞"
        elif self.name == "bishop" and self.IsBlack:
            return "♝"
        elif self.name == "queen" and self.IsBlack:
            return "♛"
        elif self.name == "king" and self.IsBlack:
            return "♚"
        elif self.name == "pawn" and self.IsBlack:
            return "♙"
        elif self.name == "horse" and self.IsBlack:
            return "♘"
        elif self.name == "bishop" and self.IsBlack:
            return "♗"
        elif self.name == "king" and self.IsBlack:
            return "♔"
        elif self.name == "queen" and self.IsBlack:
            return "♕"
        elif self.name == "rook" and self.IsBlack:
            return "♖"
        else:
            return "You didn't enter a chess piece"

chess_piece = chess("a", 1, "pawn", "white", True)
print(chess_piece)