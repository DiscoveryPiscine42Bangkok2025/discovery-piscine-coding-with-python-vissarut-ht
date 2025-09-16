class main:
    def array_of_names(dic):
        return [i[0].capitalize()+" "+i[1].capitalize() for i in dic.items()]
array_of_names = main.array_of_names   
 
persons = { 
           "jean": "valjean", 
           "grace": "hopper", 
           "xavier": "niel", 
           "fifi": "brindacier" 
} 
print(array_of_names(persons))