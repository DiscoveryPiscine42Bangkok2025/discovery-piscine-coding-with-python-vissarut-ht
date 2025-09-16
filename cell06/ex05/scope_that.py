class main:
    def add_one(num):
        if isinstance(num, list):
            num[0] += 1
        else:
            num += 1
add_one = main.add_one

my_num = 1
my_arr = [1]
print("initial number: ", my_num)
print("initial array: ", my_arr)
add_one(my_num)
add_one(my_arr)
print("processed number: ", my_num)
print("processed array: ", my_arr)