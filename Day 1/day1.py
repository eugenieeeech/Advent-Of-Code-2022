# read input textfile from same path
sum = 0
arr = []
with open("input.txt") as f:
    for line in f.readlines():
        if (line != "") & (line != "\n"):
            sum = sum + int(line)

        else:
            arr.append(sum)
            sum = 0
arr.sort(reverse=True)
# Task 1
print(max(arr))
# Task 2
print(arr[0] + arr[1] + arr[2])
