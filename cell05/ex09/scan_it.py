import sys
arr = sys.argv[1:]
if (len(arr) == 2) and (arr[0] in arr[1]):
    print(arr[1].count(arr[0]))
else:
    print("none")