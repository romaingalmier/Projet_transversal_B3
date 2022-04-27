"""
Tom/harou : Liste[T,T,F,...,T] True/False --> oblstacle a un certain angle 
Paul : 

"""
from unittest import case
import serial

L = [True,False,False,True,True]

class Deplacement:
    def __init__(self):
        self.ordre = "S"
        
        self.ser = serial.Serial("/dev/ttyUSB0", baudrate = 19200)#init Serial (ideal dans une autre classe)

    def traitementListe(self,listeTom):
        return listeTom[0],listeTom[1],listeTom[2],listeTom[3],listeTom[4]

    def choixDirection(self,listeTom):
        """
        en fonction de la liste arbre de décision

        @return direction : zone choisit 
        """
        #TODO 4 tourner a gauche/droite
        gauche, diagGauche, toutDroit, diagDroite, droite = self.traitementListe(listeTom)

        if toutDroit:
            direction = "toutDroit"
            self.ordre
        
        elif gauche:
            direction = "gauche"

        elif droite:
            direction = "droite"

        elif diagGauche:
            direction = "diagGauche"

        elif diagDroite:
            direction = "diagDroite"

        else :
            direction = "reculer"

        self.choixOrdre(direction) 
        
    
    def choixOrdre(self,direction):
        """
        adaptation direction en ordre
        """
         


        #appel envoyerOrdre
        pass


    def envoyerOrdre(self,order):
        """
        la partie serial pour communiquer
        """
        self.ser.write(order.encode())




class Viser:
    def __init__(self):
        pass
