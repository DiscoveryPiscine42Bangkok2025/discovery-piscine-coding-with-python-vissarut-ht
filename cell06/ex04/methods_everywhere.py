def shrink(var: str):
    print(var[0:8])

def enlarge(var: str):
    var = var + "Z"*(8-len(var))
    print(var)

import sys
arr = sys.argv[1:]
if len(arr) >= 1:
    for i in arr:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)
else:
    print("none")
