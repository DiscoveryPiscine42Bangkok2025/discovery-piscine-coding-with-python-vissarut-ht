import sys

def downcase_it(var: str):
    return var.lower()

arr = sys.argv[1:]
if len(arr) != 0:
    for i in arr:
        print(downcase_it(i))
else:
    print("none")