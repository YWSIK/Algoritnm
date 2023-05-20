#15652
n, m = map(int, input().split())
arr = []

def back(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(start, n+1):
        arr.append(i)
        back(i)
        arr.pop()

back(1)