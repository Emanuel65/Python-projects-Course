# Tema 2
# Scrieti un program ce va numara cate caractere are un sir de caractere dat
# de utilizator. Aceasta numarare sa se realizeze cu ajutorul unui for
# fara a utiliza len(). La final afisati rezultatul.

# **********
# stocam input-ul userului intr-o variabila
user_input = input("Va rog introduceti un sir de caractere.\n")

# declaram si initializam variabila de numarare la 0
number_of_characters = 0

# cream un for loop care sa treaca prin sirul de caractere si sa incrementeze
# variabila de numarare cu 1
for i in user_input:
    number_of_characters += 1

# afisam numarul de caractere
if number_of_characters == 1:
    print(f"String-ul dvs. are {number_of_characters} caracter.\n")
else:
    print(f"String-ul dvs. are {number_of_characters} caractere.\n")


# Tema 3
# Creati un program cu o lista de CD/DVD-uri utilizand liste nested. Trebuie
# ca programul sa imite lista de cumparaturi prezentata in curs(fisierul
# Lista_avansat.py ca si facilitati (adaugare, stergere, afisare, iesire din program).

# declaram si initializam un dictionar de CD-uri ca un dictionar gol
CD_list = {}


# declaram o functie care sa adauge filmul si continutul in lista
def add_movie(movie_title, movie_contents):
    if movie_title not in CD_list:
        CD_list[movie_title] = movie_contents


# declaram o functie care sa readea continutul listei
def read_movie():
    for key, value in CD_list.items():
        print(f"Title: {key}\nContent: {value}\n")
        print(f"Title: {key}\nContent: {value}\n")


# declaram o functie care sa stearga unul din filme
def delete_movie(movie_title):
    if movie_title in CD_list:
        del CD_list[movie_title]


# declaram o functie care sa inchida consola
def exit_console():
    exit()


# declaram o functie care sa afiseze optiunile posibile
def display_options():
    available_options = {"1": "Add movie to database",
                         "2": "Display the database",
                         "3": "Delete movie from the database",
                         "4": "Exit"}
    for key, value in available_options.items():
        print(f"{key}: {value}")


# declaram o functie care sa valideze si sa aduca input-ul userului
def get_valid_user_input():
    user_raw_input = input("Please enter the number of your selection:\n")
    while True:
        if user_raw_input.isnumeric():
            valid_input = user_raw_input
            return int(valid_input)
        else:
            continue


# cream logica principala a programului
print("Welcome to the CD Movie Database!\n")
while True:
    display_options()
    if get_valid_user_input() == 1:
        movie_title = input("Please enter the movie title:\n")
        movie_content = input("Please enter the movie content:\n")
        add_movie(movie_title, movie_content)
    elif get_valid_user_input() == 2:
        read_movie()
    elif get_valid_user_input() == 3:
        movie_title = input("Please enter the movie title you wish to delete")
        delete_movie(movie_title)
    elif get_valid_user_input() == 4:
        exit_console()
    else:
        print("Please choose a valid option")
        display_options()
    choice = input("Do you wish to make another selection?\nPress Y for yes, or N for no.\n").upper()
    if choice == "Y":
        continue
    else:
        exit()
        break
