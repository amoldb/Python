import sys

if len(sys.argv) != 2:
    print("Usage: pattern01.py <int>")
    exit(0)
n = int(sys.argv[1])
step = 1
incrementFlag = True

for i in range(1, n*2 + 1):
    print("*"*step)
    if i == n:
        incrementFlag = False
    if incrementFlag:
        step = step + 1
    else:
        step = step - 1

