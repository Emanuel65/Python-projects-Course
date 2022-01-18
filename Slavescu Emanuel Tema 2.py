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
