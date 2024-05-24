import cv2  # Importation de la bibliothèque OpenCV pour les tâches de vision par ordinateur
import pandas as pd  # Importation de pandas pour la manipulation de données
from ultralytics import YOLO  # Importation du modèle de détection d'objets YOLO depuis Ultralytics
import cvzone  # Importation de cvzone pour des utilitaires supplémentaires OpenCV

# Charger le modèle YOLO pré-entraîné
model = YOLO('best.pt')

# Fonction pour gérer les événements de la souris pour l'affichage RVB
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)

# Créer une fenêtre pour afficher le flux RVB et définir le rappel d'événement de la souris
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Ouvrir le fichier vidéo pour le traitement
cap = cv2.VideoCapture('accident_car.mp4')

# Lire les étiquettes de classe à partir d'un fichier texte
my_file = open("classe1.txt", "r")
data = my_file.read()
class_list = data.split("\n")

# Variable pour compter les trames
count = 0

# Boucle principale pour le traitement des trames vidéo
while True:    
    # Lire la trame de la vidéo
    ret, frame = cap.read()
    
    # Si la fin de la vidéo est atteinte, revenir au début
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Incrémenter le compteur de trames et traiter chaque troisième trame
    count += 1
    if count % 3 != 0:
        continue
    
    # Redimensionner la trame pour l'affichage
    frame = cv2.resize(frame, (1020, 500))
    
    # Effectuer la détection d'objet sur la trame en utilisant le modèle YOLO
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    # Itérer sur les objets détectés et dessiner les boîtes englobantes
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]

        # Dessiner la boîte englobante et l'étiquette sur la trame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
        cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)
    
    # Afficher la trame avec les boîtes englobantes
    cv2.imshow("RGB", frame)
    
    # Interrompre la boucle si la touche 'Esc' est pressée
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Libérer la capture vidéo et fermer les fenêtres OpenCV
cap.release()  
cv2.destroyAllWindows()
