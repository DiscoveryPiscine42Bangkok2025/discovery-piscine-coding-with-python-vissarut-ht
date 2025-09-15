import sys
arr = sys.argv[1:]
if len(arr) != 0:
    for i in arr:
        if not i.endswith("ism"):
            print(i+"ism")
else:
    print("none")