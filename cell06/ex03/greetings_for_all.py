class main:
    def greetings(name = "noble stranger"):
        if isinstance(name, str):
            print(f"Hello, {name}.")
        else:
            print("Error! It was not a name.")
greetings = main.greetings

greetings('Alexandra') 
greetings('Wil') 
greetings() 
greetings(42)