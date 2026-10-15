import sys

def main():
    data = sys.stdin.read().split()

    data = [int(x) for x in data]

    arr_len = data.pop(0)
    target = data.pop(0)

    first, last = -1, -1

    for num in range(arr_len):
        if data[num] == target and first == -1:
            first = num
            last = num
            firstFound = True
        if data[num] == target:
            last = num

        if data[num] > target:
            break

    print(first, last)

main()
