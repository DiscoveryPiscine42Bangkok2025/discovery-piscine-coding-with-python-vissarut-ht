import sys
arr = sys.argv[1:]
if len(arr) == 2:
    arr = [int(i) for i in arr]
    if arr[0] < arr[1]:
        print([i for i in range(arr[0], arr[1]+1)])
    else:
        print([i for i in range(arr[0], arr[1]-1, -1)])
else:
    print("none")