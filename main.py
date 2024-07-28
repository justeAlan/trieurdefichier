from pathlib import Path
import shutil

# Récupérer le dossier où est placer le script dans une variable
currentp = Path.cwd()

# Annoncer le dossier avant d'activer le script
print("Initialisation du script : Trieur de Fichier, veuillez patienter...")
INPUT_MENU = f"Vous allez trier le dosier '/{currentp.stem}', souhaitez-vous continuer ?\n O pour Oui\n N pour Non \n Votre choix > "
MENU_CHOICES = ["O" , "N"]

# Boucle du MENU
while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(INPUT_MENU).upper()
        if user_choice not in MENU_CHOICES:
            print("Veuillez selectionner une option valide.")
    if user_choice == "N":
        print(f"Les fichiers de /{currentp.stem} ne seront pas triés. ")
        print("Sortie du programme...")
        break
    elif user_choice == "O":
        print(f"Lancement de tri de {currentp.stem}...")
    
# Lister tous les fichiers et récupérer les extensions dans une variable sans le point
        all_ext = set()
        for files in currentp.iterdir():
            if files.is_file():
                no_dot = (files.suffix[1:])
                all_ext.add(no_dot)

# Une fois la liste récupérer créer un dossier pour chaque extension
# Récupérer les extensions et leur attribuer un Path puis créer le dossier
        for ext in all_ext:
            new_dir = currentp / ext
            if new_dir.exists():
                print(f"Le dossier /{ext} existe déjà.")
            else:
                new_dir.mkdir(exist_ok=True)
                print(f"Création du dossier /{ext} effectué avec succès !")
# Prendre chaque fichier et les bouger de dossiers
        for files in currentp.iterdir() :
            if files.is_file():
                if files.name == 'main.py':
                    print("On ne tri pas le scrpit Python ;)")
                else:
                    # Transférer le fichier
                    shutil.move(str(files), str(files.suffix[1:]))
                    print(f"Le fichier {files} a bien été bougé dans /{files.suffix[1:]} ")
        print("Le tri est terminé.")
        break
print("Merci d'avoir utilisé le triAlan :D")
    
        
                

