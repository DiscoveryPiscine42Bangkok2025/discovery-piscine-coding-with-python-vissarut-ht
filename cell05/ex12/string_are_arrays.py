import sys
arr = sys.argv[1:]
if (len(arr) == 1) and ("z" in arr[0]):
    print("z"*arr[0].count("z"))
else:
    print("none")