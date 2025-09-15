import sys
arr = sys.argv[1:]
if len(arr) >= 2:
    for i in arr[::-1]:
        print(i)
else:
    print("none")