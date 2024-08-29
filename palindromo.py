palabra = "tenet"
string_reversed = ""
for character in palabra:
    string_reversed = character + string_reversed
if (palabra == string_reversed):
    print("Es palíndromo")
else:
    print("no es palíndromo")

print(string_reversed)    


