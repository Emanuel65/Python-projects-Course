# Dupa ce am instalat pyfiglet cu "pip install pyfiglet" in command prompt
import pyfiglet

# Tema 1

print("\t\t\tDimineata de Vasile Alecsandri\a\n\n",
      '''Zori de ziua se revarsa peste vesela natura,\n'''
      '''Prevestind un soare dulce cu lumina si caldura,\n'''
      "In", "curand", "si", "el", "apare", "pe", "orizontul", "aurit", "\n"
      "Sorbind" + "roua" + "diminetii" + "de" + "pe" + "campul" + "inverzit.\n"
      """El se-nalta de trei suliti pe cereasca mandra scara,\n"""
      """Si cu raze vii saruta june flori de primavara,\n"""
      "Deditei si" + "viorele," + "brebenei si toporasi,\n"
      '''Ce razbat prin frunze uscate si s-arata dragalasi.\n''')
input()

# Tema 3

ascii_Art = pyfiglet.figlet_format("Bitacad")

print(ascii_Art)
input()
