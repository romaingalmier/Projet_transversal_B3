# importation des modules nécessaires
from imutils.video import VideoStream
import argparse
import cv2
import imutils
import time
#import fonctions_paul

# définir les limites basses et hautes de la couleur voulue dans l'espace HSV
couleur_basse = (29, 86, 6) 
couleur_haute = (64, 255, 255) 
couleur_basse_viseur = (0, 100, 110) 
couleur_haute_viseur = (25, 255, 255) 
#couleur_basse_viseur = (0, 120, 70) 
#couleur_haute_viseur = (20, 255, 255) 

# On démarre la webcam
video_stream = VideoStream(src=0).start()

while True:
	#Initialisation liste
	Liste1Paul = [False,0,0]
	Liste2Paul = [[False,False],[False,False]]
	# lire l'image actuelle
	image = video_stream.read()

	#redimensionnement de l'image, flouttage et convertion en HSV
	image = imutils.resize(image, width=600)
	gauss_blur = cv2.GaussianBlur(image, (11, 11), 0)
	hsv = cv2.cvtColor(gauss_blur, cv2.COLOR_BGR2HSV)

	'''Cas de la cible'''
	# Construction d'un masque pour la couleur choisie
	# Puis plusieurs érosions et dilatation pour enlever les taches restantes dans le masque
	masque = cv2.inRange(hsv, couleur_basse, couleur_haute)
	masque = cv2.erode(masque, None, iterations=2)
	masque = cv2.dilate(masque, None, iterations=2)

	# recherche des contours du masque et initialisation des coordonnées du centre du cercle
	contours = cv2.findContours(masque.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(contours)
	centre = None

	# On rentre dans la condition si au moins un contour a été détecté
	detection = False
	freq1 = 0
	freq2 = 0
	if len(contours) > 0:
		detection = True
		# Permet de trouver le plus grand contour du masque puis de l'utiliser pour trouver le cercle d'encerclement minimal et le centre
		c = max(contours, key=cv2.contourArea)
		((x, y), rayon) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		centre = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		freq1 = centre[0] * 1.0263 + 1203.8
		freq2 = centre[1] * (-1.0255) + 842.5
		# Si le rayon est suffisament grand
		if rayon > 10:
			# Dessin du cercle et du centre sur l'image 
			cv2.circle(image, (int(x), int(y)), int(rayon), (0, 0, 0), 2)
			cv2.circle(image, centre, 5, (0, 0, 0), -1)
		#Communication au robot
	time.sleep(0.1)
	Liste1Paul[0] = detection
	Liste1Paul[1] = freq1
	Liste1Paul[2] = freq2
	print(Liste1Paul)
	Liste1Paul.clear()
		


	# Affichage de l'image sur notre écran 
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
	