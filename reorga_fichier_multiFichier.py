import os
from glob import glob
import shutil
from zipfile import ZipFile

chemin = os.path.dirname(__file__)
# cheminDest = os.path.join(chemin, "".join(chemin.split("\\")[-1:]))

os.chdir(chemin)

for element in os.listdir(chemin):
    if element.endswith('.zip'):
        fichierZip = element
        print(fichierZip)
        cheminDest = os.path.join(chemin, fichierZip[:-4])

        try:
            for elemenZip in fichierZip:
                os.makedirs(element)
        except FileExistsError:
            pass


        def dezip():
            with ZipFile(fichierZip, 'r') as zip:
                zip.extractall(cheminDest)

        dezip()

        dossiers = []
        # print(f" Chemin de destination: {cheminDest}")

        root = os.listdir(cheminDest)
        # print(f" Root {root}")

        os.chdir(cheminDest)
        for element in root:
            if os.path.isdir(element):
                # print(f"{element} est un dossier")
                dossiers.append(element)
            else:
                # print(f"{element} est un ficher")
                continue

        os.chdir(chemin)



        liste_extensions = ['.txt', '.odt', '.doc','docx', 'pdf', 'html']

        def reorganise():
            
            for element in liste_extensions:
                # print(element)
                fichiers = glob('**/*'+ str(element), recursive=True)
                # print(fichiers)
            
                for fichier in fichiers:
                    
                    try:
                        fichierRename = fichier.split("\\")
                        # print(f"fichierRename {fichierRename}")
                        fichierRen = fichierRename[0] + "\\" + fichierRename[1].split("_")[0] + "_" + fichierRename[2]
                        # print(f"fichierRen {fichierRen}")
                        os.rename(fichier, fichierRen)           
                        if fichierRen.endswith(".html"):
                            os.remove(fichierRen)
                        else:
                            shutil.move(fichierRen,cheminDest)
                            dossier_remove = os.path.splitext(os.path.join(cheminDest, fichier))



                    except (shutil.Error, IndexError, FileExistsError):
                        pass

            # supprime les dossiers vides
            for dossier in dossiers:
                # print(f"Dossier à supprimer {dossier}")
                if len(os.listdir(os.path.join(cheminDest, dossier))) == 0:
                    # print("Le répertoire est vide")
                    # print(os.path.join(chemin, dossier))
                    os.rmdir(os.path.join(cheminDest, dossier))
            
                else:    
                    # print("Le répertoire n'est pas vide")
                    continue
        reorganise()





        
print("Ficher réorganiser avec succès, ou pas...")