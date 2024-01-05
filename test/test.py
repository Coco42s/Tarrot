# Chaîne de caractères
str_variable = "[tt 1,tt 2,tt 3]"

# Ajout de guillemets autour des éléments et correction de la syntaxe
str_variable_fixed = str_variable.replace(",", "','").replace("[", "['").replace("]", "']")

# Utilisation de eval() pour transformer la chaîne en liste
list_variable = eval(str_variable_fixed)

# Affichage de la liste résultante
print(list_variable)