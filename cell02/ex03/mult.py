first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
mult = first_num * second_num
print(first_num, "x", second_num, "=", mult)
if mult < 0:
    print("The result is negative.")
elif mult > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")