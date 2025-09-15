import sys
arr = sys.argv[1:]
if len(arr) == 1:
    inp = input("What was the parameter? ")
    if inp == arr[0]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none") 