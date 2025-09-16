class main:
    def find_the_redheads(dic):
        red_dic = {key: value for key, value in dic.items() if value == "red"}
        return list(red_dic.keys())
find_the_redheads = main.find_the_redheads  
    
dupont_family = { 
                 "florian": "red", 
                 "marie": "blond", 
                 "virginie": "brunette", 
                 "david": "red", 
                 "franck": "red" 
}
print(find_the_redheads(dupont_family))