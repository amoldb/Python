import sys

def main():
#    data = int(sys.stdin.read().split()[0])
    data = 4
    if data < 2:
        print(data)
        return


    print(data)
    low = 1
    high = data
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= data:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    print(ans)


main()
