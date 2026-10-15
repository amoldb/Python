import sys

def main():
    data = sys.stdin.read().split()
    size = int(data[0])
    data.pop(0)
    data = [int(c) for c in data]

    for i in range(size):
        while data[i] != i and data[i] != -1:
            value = data[i]
            data[i] = data[value]
            data[value] = value 
            print(value, data[i])

    print(data)

main()

