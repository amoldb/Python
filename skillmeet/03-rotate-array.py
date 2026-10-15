import sys

def main():
#    data = sys.stdin.read().split()
#    data = [int(c) for c in data]
    # TODO: read input and print the answer
    data = [5, 1, 2, 3, 4, 5]
    data.pop(0)
    last = data.pop(-1)
    data.insert(0, last)
    print(" ".join([str(c) for c in data]))

main()

def rotate():
    data = sys.stdin.read().split()
    data = [int(c) for c in data]

    if not data:
        print()
        return

    n = data[0]
    if n == 0:
        print()
        return

    last = data[-1]

    for i in range(n-1, 0, -1):
        data[i] = data[i-1]

    data[0] = last
    print(" ".join([str(i) for i in data]))

rotate()
