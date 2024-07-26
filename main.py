from pathlib import Path

# Récupérer le dossier où est placer le script
currentp = Path.cwd()
p_str = currentp.as_posix()
currentp = (f'{p_str}')
currentp = Path(currentp)

# Lister tous les fichiers et récupérer les extensions dans une variable sans le point
all_ext = currentp.iterdir()
for ext in all_ext:
    for ext in all_ext:
        all_ext = ext.suffix
        all_ext = all_ext[1:]
        print(all_ext)
        type(all_ext)

# Une fois la liste récupérer créer un dossier pour chaque extension
# Récupérer les extensions et leur attribuer un Path puis créer le dossier
for ext in all_ext:
    new_dir = currentp / (f'{all_ext}')
    print(new_dir)