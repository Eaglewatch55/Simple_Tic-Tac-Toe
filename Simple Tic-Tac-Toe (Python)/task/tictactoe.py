def matrix_generator(string):
    dict_ = {}

    mat = [[input_string[0], input_string[1], input_string[2]],
              [input_string[3], input_string[4], input_string[5]],
              [input_string[6], input_string[7], input_string[8]]]

    for char in input_string:
        if char not in accepted_char:
            raise ValueError(f"Character '{char}' not accepted")

        if char not in dict_.keys():
            dict_[char] = 1

        else:
            dict_[char] += 1

    return mat, dict_

#XOOOXOXXO
input_string = input()
accepted_char = ("X", "O", "_")

matrix, dict_count = matrix_generator(input_string)

print("---------")
print(f"| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |")
print(f"| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |")
print(f"| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |")
print("---------")


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

