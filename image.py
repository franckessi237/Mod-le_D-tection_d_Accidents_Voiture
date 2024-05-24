import cv2  # Importation de la bibliothèque OpenCV pour le traitement d'images et de vidéos
import time  # Importation du module pour gérer le temps en Python

# Initialisation des variables
cpt = 0  # Compteur d'images extraites
maxFrames = 131  # Nombre maximum d'images à extraire de la vidéo

count = 0  # Initialisation du compteur utilisé pour déterminer à quelles images extraire

# Ouverture de la vidéo à partir du fichier "accident_car.mp4"
cap = cv2.VideoCapture('accident_car.mp4')

# Boucle pour lire la vidéo et extraire des images jusqu'à ce que le nombre maximum d'images soit atteint
while cpt < maxFrames:
    # Lecture d'un frame de la vidéo
    ret, frame = cap.read()

    # Vérification si la lecture a réussi
    if not ret:
        break  # Si la lecture échoue (fin de la vidéo), la boucle se termine

    # Incrémentation du compteur d'images lues
    count += 1

    # Si l'indice de l'image n'est pas un multiple de 3, passe à l'itération suivante de la boucle
    if count % 3 != 0:
        continue

    # Redimensionnement du frame à la taille spécifiée
    frame = cv2.resize(frame, (1080, 500))

    # Affichage du frame dans une fenêtre nommée "VideoAccident"
    cv2.imshow("VideoAccident", frame)

    # Enregistrement du frame sous forme d'image JPEG dans le répertoire spécifié avec un nom de fichier formaté
    cv2.imwrite(r"C:\Users\essit\Desktop\Projet_IA_ESSI_TSONDO_Franck_Patrick\images\car_%d.jpg" % cpt, frame)

    # Pause pour permettre l'affichage du frame
    time.sleep(0.01)

    # Incrémentation du compteur d'images extraites
    cpt += 1

    # Si une touche est enfoncée et que c'est la touche Echap (27 en code ASCII), la boucle se termine
    if cv2.waitKey(5) & 0xFF == 27:
        break

# Libération des ressources après la fin de la boucle
cap.release()  # Libération de la capture vidéo
cv2.destroyAllWindows()  # Fermeture de toutes les fenêtres OpenCV
