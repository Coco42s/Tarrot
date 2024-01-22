

import re

choix = "Pique 4"

if re.match(r"^(Pique|Trèfle|Coeur|Carreau)\s(42)$", choix):
    print("Bonjour")

