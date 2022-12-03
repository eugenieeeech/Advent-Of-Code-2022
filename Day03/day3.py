total = 0


def asciitoTask1Value(x):
    if ord(x) >= 97:
        return ord(x) - 97 + 1
    else:
        return ord(x) - 65 + 27


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
print(total)
