class main:
    def average(dic):
        total_score = sum(list(dic.values()))
        num_student = len(list(dic.values()))
        return total_score/num_student
average = main.average

class_3B = { "marine": 18, "jean": 15, "coline": 8, "luc": 9 } 
class_3C = { "quentin": 17, "julie": 15, "marc": 8, "stephanie": 13 } 
print(f"Average for class 3B: {average(class_3B)}.") 
print(f"Average for class 3C: {average(class_3C)}.")