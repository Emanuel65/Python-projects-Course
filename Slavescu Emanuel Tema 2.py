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
