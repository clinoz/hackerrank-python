if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    i = 0
    while i<n:
        if winner == max(arr):
            arr.remove(max(arr))
        i = i+1
    print(max(arr))

