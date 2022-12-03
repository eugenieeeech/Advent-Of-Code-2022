total = 0


def asciitoTask1Value(x):
    if ord(x) >= 97:
        return ord(x) - 97 + 1
    else:
        return ord(x) - 65 + 27
    # Task 1


with open("input.txt") as f:
    for line in f.readlines():
        if (line != "") & (line != "\n"):
            first_half = list(line[:len(line) // 2])
            second_half = list(line[len(line) // 2:])
            same = first_half[0]
            for i in first_half:
                for j in second_half:
                    if i == j:
                        same = i
            total += asciitoTask1Value(same)
#   Task 2
# counter = 0
# badge: list
# with open("input.txt") as f:
#     for line in f.readlines():
#         if (line != "") & (line != "\n"):
#             if counter == 0:
#                 firstLine = list(line)
#                 counter += 1
#             elif counter == 1:
#                 secondLine = list(line)
#                 counter += 1
#             elif counter == 2:
#                 thirdLine = list(line)
#                 # compare array logic
#                 for i in firstLine:
#                     for j in secondLine:
#                         if (i == j)&(i != "") & (i != "\n"):
#                             for k in thirdLine:
#                                 if k == i:
#                                     same = i
#                 counter = 0
#
#                 total += asciitoTask1Value(same)
print(total)
