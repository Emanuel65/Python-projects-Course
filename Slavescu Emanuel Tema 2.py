# Tema 1
# Creati un progam care sa verifice daca textul introdus
# de un utilizator de la tastatura este un sir de tip numere sau litere.

# **********
# declaram o functie care sa faca treaba pana la capat
def actual_int_check(raw_input):
    try:
        int(raw_input)
    except ValueError:
        return False


# colectam input-ul utilizatorului
raw_user_input = input("Introduceti un numar.\n")

# cerem utilizatorului sa introduca un numar pana ce reuseste
while actual_int_check(raw_user_input) is False:
    print("Input invalid!\n",
          "Sirul de caracter nu este un numar".swapcase())
    raw_user_input = input("Va rog introduceti un numar.\n")
    continue

# daca am ajuns in acest punct inseamna ca numarul este valid si il afisam
print(f"Ati ales numarul {raw_user_input.center(80)}. Felicitari!\n",
      "Sirul de caractere este format din numere")
input()


# ------------------------------------------------------------------------

# Tema 2
# Creati un program care sa calculeze a si b (variabile capturate de la
# utilizator
# prin raw_input) urmatoarea functie matematica

# **********
# declaram o functie care sa faca treaba pana la capat
def actual_float_check(raw_input):
    try:
        float(raw_input)
    except ValueError:
        return False


# declaram o functie care sa ia cei doi parametri si sa faca operatia
def math_operation(a, b):
    result = 6 * (2 + (a - 1) % b) * 2 ** a
    return result


# colectam raw input-ul de la utilizator
raw_user_input_a = input("Introduceti valoarea numarului a\n")
raw_user_input_b = input("Introduceti valoarea numarului b\n")

# cerem utilizatorului sa introduca float-uri pana ce reuseste
while (actual_float_check(raw_user_input_a) is False or
       actual_float_check(raw_user_input_b) is False):
    print("Input invalid!")
    raw_user_input_a = input("Introduceti valoarea numarului a\n")
    raw_user_input_b = input("Introduceti valoarea numarului b\n")
    continue

# daca am ajuns in acest punct, inseamna ca utilizatorul a introdus float-uri
valid_input_a = float(raw_user_input_a)
valid_input_b = float(raw_user_input_b)

# afisam rezultatul operatiei
print(f"Rezultatul este: {math_operation(valid_input_a, valid_input_b)}")
input()


# ------------------------------------------------------------------------

# Tema 3
# Creati un program in care utilizatorul sa introduca un numar.
# Validati daca acest numar este par sau impar si
# afisati un raspuns in acest sens.

# **********
# colectam input-ul utilizatorului
raw_user_input = input("Introduceti un numar.\n")

# ne folosim de functia pe care am creat-o anterior pentru a valida input-ul
while actual_int_check(raw_user_input) is False:
    print("Input invalid!")
    raw_user_input = input("Introduceti un numar.\n")
    continue

# daca am ajuns in acest punct inseamna ca utilizatorul a introdus un numar.
valid_input = int(raw_user_input)

# verificam daca este par sau impar si afisam Rezultatul
if valid_input % 2 == 0:
    print(f"{valid_input} este par.")
else:
    print(f"{valid_input} nu este par")
input()


# ------------------------------------------------------------------------

# Tema 4
# Creati un program in care utilizatorul sa introduca un sir de caractere.
# Validati daca acest sir are in interior sirul de caractere “este” si
# afisati un raspuns in acest sens.

# **********
# cream lista de caractere tinta
target_chars = ("!", ",", ".", "?")

# colectam input-ul utilizatorului
user_input = input("Introduceti un sir de caractere.\n")

# verificam daca exista "este"
if "este" in user_input:
    # verificam daca are unul din caracterele tinta
    if user_input.endswith(target_chars):
        # afisam rezultatul si caracterul folosit
        print("sirul de caractere contine \"este\" si se termina cu",
              f"{user_input[-1]}")
    # afisam rezultatul si indicam faptu ca nu contine niciun caracter tinta
    else:
        print(f"sirul de caractere contine \"este\" dar nu si {target_chars}")
# afisam lipsa cuvantului "este"
else:
    print("Sirul de caractere nu contine \"este\"")
    input()


# ------------------------------------------------------------------------

# Tema 5
# Creati un program in care utilizatorul sa introduca un an.
# Calculati daca anul este bisect sau nu si afisati un raspuns in acest sens.

# **********
# colectam input-ul utilizatorului
raw_user_input = input("Introduceti un an.\n")

# ne folosim de functia pe care am creat-o anterior pentru a valida input-ul
while actual_int_check(raw_user_input) is False:
    print("Input invalid!\n",
          "Sirul de caracter nu este un an")
    raw_user_input = input("Va rog introduceti un an.\n")
    continue

# daca am ajuns in acest punct inseamna ca utilizatorul a introdus un an.
valid_input = int(raw_user_input)

# verificam daca anul este bisect
if valid_input % 4 == 0:
    print("Anul introdus este bisect.")
else:
    print("Anul introdus nu este bisect.")
input()


# ------------------------------------------------------------------------

# Tema 6
# Creati un program in care utilizatorul sa introduca un numar. Calculati daca
# numarul este pozitiv, zero sau negativ.

# **********
# colectam input-ul utilizatorului
raw_user_input = input("Introduceti un numar intreg.\n")

# ne folosim de functia pe care am creat-o anterior pentru a valida input-ul
while actual_int_check(raw_user_input) is False:
    print("Input invalid!\n",
          "Sirul de caracter nu este un numar intreg")
    raw_user_input = input("Va rog introduceti un numar intreg.\n")
    continue

# daca am ajuns in acest punct inseamna ca utilizatorul a introdus un an.
valid_input = int(raw_user_input)

# verificam daca numarul este mai mare, mai mic, sau egal cu 0
if valid_input < 0:
    print("Ati introdus un numar negativ, valoarea lui pozitiva este:",
          f"{abs(valid_input)}")
elif valid_input == 0:
    print("Ati introdus numarul 0")
else:
    if valid_input < 10:
        print("numar intre 0 si 10")
    else:
        print("numar mai mare ca 10")
input()


# ------------------------------------------------------------------------

# Tema 7
# Creati un program care are ca scop un meniu.

# **********
# afisam optiunile posibile
print("1 - Afisare lista de cumparaturi",
      "2 - Adaugare element",
      "3 - Stergere element",
      "4 - Stergere lista de cumparaturi",
      "5 - cautare lista de cumparaturi")

# colectam input-ul utilizatorului
raw_user_input = input("Introduceti numarul unei optiuni (1 - 5).\n")

# declaram o variabila care semnaleaza daca s-a introdus un numar
valid_number = True

# declaram o variabila care semnaleaza daca optiunea este in meniu
valid_menu_option = True

# declaram o functie care sa verifice daca input-ul este valid si sa returneze
# numarul optiunii
def check_valid_menu_option(raw_input):
    if actual_int_check(raw_input) is False:
        valid_number = False
    else
        valid_input = int(raw_input)
        if valid_input < 1 or valid_input > 5:
            valid_menu_option = False
        else:
            return valid_input

# procesam optiunea userului
check_valid_menu_option(raw_user_input)

# validam input-ul
    while valid_number == False or valid_menu_option == False:
        if valid_number == False:
            print("Input invalid!\n")
            raw_user_input = input("Va rog introduceti un numar.")
            check_valid_menu_option(raw_user_input)
        elif 
