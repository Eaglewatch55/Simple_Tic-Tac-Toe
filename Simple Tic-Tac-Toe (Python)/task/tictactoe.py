class Matrix:
    def __init__(self):
        self.line0 = [" ", " ", " "]
        self.line1 = [" ", " ", " "]
        self.line2 = [" ", " ", " "]
        self.mtx = [self.line0, self.line1, self.line2]

    def __str__(self):
        to_print = "---------\n"

        for line in self.mtx:
            to_print += f"| {line[0]} {line[1]} {line[2]} |\n"

        to_print += "---------"

        return to_print

    def get_value(self, coordinates: list):
        return self.mtx[coordinates[0]][coordinates[1]]

    def set_value(self, coordinates: list, player):
        self.mtx[coordinates[0]][coordinates[1]] = player

    def all_filled(self):

        for line in self.mtx:
            if " " in line:
                return False

        return True


def coordinate_validation(coordinate):
    coordinates = []
    try:
        for char_ in coordinate:
            if char_ == " ":
                continue
            else:
                coordinates.append(int(char_) - 1)
    except ValueError:
        print("You should enter numbers!")
        return None

    valid_num = [0, 1, 2]

    if coordinates[0] not in valid_num or coordinates[1] not in valid_num:
        print("Coordinates should be from 1 to 3!")
        return None

    return coordinates


# def matrix_generator(input_string):
#     """Creates the matrix and counts each character"""
#
#     mat = [[input_string[0], input_string[1], input_string[2]],
#               [input_string[3], input_string[4], input_string[5]],
#               [input_string[6], input_string[7], input_string[8]]]
#
#     for char_ in input_string:
#         if char_ not in accepted_char:
#             raise ValueError(f"Character '{char_}' not accepted")
#
#     return mat



# VALIDATION AND STATUS CHECKER
def winner_checker(mat: Matrix, player):
    winner = []
    cond1 = cond2 = False

    for i in range(3):

        if player == mat.get_value([i, 0]) == mat.get_value([i, 1]) == mat.get_value([i, 2]):
            cond1 = True
            break

        if player == mat.get_value([0, i]) == mat.get_value([1, i]) == mat.get_value([2, i]):
            cond2 = True
            break

    cond3 = player == mat.get_value([0, 0]) == mat.get_value([1, 1]) == mat.get_value([2, 2])
    cond4 = player == mat.get_value([0, 2]) == mat.get_value([1, 1]) == mat.get_value([2, 0])

    return any([cond1, cond2, cond3, cond4])


# MAIN EXECUTION
if __name__ == "__main__":

    matrix = Matrix()
    counter = 0
    players = {0: "X", 1: "O"}
    print(matrix)

    while True:
        coord = None
        player = players[counter % 2]

        while coord is None:
            input_ = input()
            coord = coordinate_validation(input_)

        if matrix.get_value(coord) == " ":
            matrix.set_value(coord, player)
        else:
            print("This cell is occupied! Choose another one!")
            continue

        print(matrix)

        if winner_checker(matrix, player):
            print(f"{player} wins")
            exit()
        if matrix.all_filled():
            print("Draw")
            exit()

        counter += 1

