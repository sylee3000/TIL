dict = {"Pokemon":"Pikachu", "Digimon":"Agumon", "Yugioh":"Black Magician"}

in_data = input()
if in_data in dict.keys():
    print(dict[in_data])
else:
    print("I don't know")