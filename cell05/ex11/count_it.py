import sys
arr = sys.argv[1:]
if len(arr) != 0:
    print(f"parameters: {len(arr)}")
    for i in arr:
        print(f"{i}: {len(i)}")
else:
    print("none")