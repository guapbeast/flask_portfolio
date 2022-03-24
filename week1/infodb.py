
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Movie": "Encanto",  
               "Release": "November 24, 2021",  
               "BoxOffice": "$250.3 Million",  
               "Email": "jmortensen@powayusd.com",  
               "MainCharacters":["Mirabel","Luisa","Isabela","Camilo", "Bruno"]  
              })  
InfoDb.append({  
               "Movie": "Turning Red",  
               "Release": "February 21, 2022",  
               "BoxOffice": "$8.4 Million",   
               "Directors": ["Byron Howard", "Jared Bush"],  
               "MainCharacters":["Meilin Lee","Priya Mangal","Ming Lee","Devon", "Miriam"]
              })  

# All of the stuff in the InfoDb dictionaries contain data that is later pulled.
def print_data(n):
    print(InfoDb[n]["Movie"], InfoDb[n]["Release"])  
    print("\t", "Characters: ", end="") 
    print(", ".join(InfoDb[n]["MainCharacters"]))
    print()

def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

  
def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  
    print("Recursive loop")
    recursive_loop(0)  
