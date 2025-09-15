def famous_births(dic):
    sorted_dic = dict(sorted(women_scientists.items(),key=lambda item: int(item[1]["date_of_birth"])))
    for i in sorted_dic.values():
        print(f"{i['name']} is a great scientist born in {i['date_of_birth']}.")
    
women_scientists = { "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" }, 
                    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" }, 
                    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" }, 
                    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" } 
}
famous_births(women_scientists)