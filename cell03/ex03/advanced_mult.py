import sys
inp = sys.argv[1:]
if len(inp) == 0:
    num1 = 0
    while num1 <= 10:
        num2 = 0
        print("Table de", str(num1)+": ", end="")
        while num2 <= 10:
            print(num2*num1, "", end="")
            num2 += 1
        print()
        num1 += 1
else:
    print("none")
