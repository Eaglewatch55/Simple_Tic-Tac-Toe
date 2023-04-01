def matrix_generator(input_string):
    dict_ = {}

    mat = [[input_string[0], input_string[1], input_string[2]],
              [input_string[3], input_string[4], input_string[5]],
              [input_string[6], input_string[7], input_string[8]]]

    for char_ in input_string:
        if char_ not in accepted_char:
            raise ValueError(f"Character '{char_}' not accepted")

        if char_ not in dict_.keys():
            dict_[char_] = 1

        else:
            dict_[char_] += 1

    return mat, dict_


def print_matrix(temp_matrix):
    print("---------")
    print(f"| {temp_matrix[0][0]} {temp_matrix[0][1]} {temp_matrix[0][2]} |")
    print(f"| {temp_matrix[1][0]} {temp_matrix[1][1]} {temp_matrix[1][2]} |")
    print(f"| {temp_matrix[2][0]} {temp_matrix[2][1]} {temp_matrix[2][2]} |")
    print("---------")


def update_matrix(temp_matrix, cord):
    temp_matrix[cord[0]][cord[1]] = "X"
    return temp_matrix

input_ = input()
accepted_char = ("X", "O", "_")

matrix, dict_count = matrix_generator(input_)

print_matrix(matrix)

while True:
    input_ = input()
    coordinates = []

    try:
        for char_ in input_:
            if char_ == " ":
                continue
            else:
                coordinates.append(int(char_) - 1)
    except ValueError:
        print("You should enter numbers!")
        continue

    valid_num = [0, 1, 2]

    if coordinates[0] not in valid_num or coordinates[1] not in valid_num:
        print("Coordinates should be from 1 to 3!")
        continue

    if matrix[coordinates[0]][coordinates[1]] != "_":
        print("This cell is occupied! Choose another one!")
        continue

    break

matrix = update_matrix(matrix, coordinates)
print_matrix(matrix)

# VALIDATION AND STATUS CHECKER

# if abs(dict_count["X"] - dict_count["O"]) >= 2:
#     print("Impossible")
#     exit()
#
# winner = []
#
# for i in range(3):
#     if matrix[i][0] == matrix[i][1] and matrix[i][0] == matrix[i][2]:
#         winner.append(matrix[i][0])
#
#     if matrix[0][i] == matrix[1][i] and matrix[0][i] == matrix[2][i]:
#         winner.append(matrix[0][i])
#
# if matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
#     winner.append(matrix[i][0])
#
# if matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[0][2]:
#     winner.append(matrix[i][0])
#
#
# if len(winner) == 1:
#     print(f"{winner[0]} wins")
#     exit()
# elif len(winner) > 1:
#     print("Impossible")
#     exit()
#
# if "_" in dict_count.keys():
#     print("Game not finished")
# else:
#     print("Draw")

