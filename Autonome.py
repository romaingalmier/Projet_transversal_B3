"""
Tom/harou : Liste[T,T,F,...,T] True/False --> oblstacle a un certain angle 
Paul : Liste1[bool(cible detecter ou non),freq1,freq2]
       Liste2[[bool, bool],[bool,bool]] --> 
                    apres 1ere viser :[[besoin d'ajuster? , sens d'ajustement : horizontal(True)/vertical],...]

"""
import serial
from time import sleep

L = [True,False,False,True,True]


class Robot:
    def __init__(self):
        self.ordre = "S"
        self.ser = serial.Serial("/dev/ttyUSB0", baudrate = 19200)

        self.depacementPossible = True # Bool pour activer ou desactiver le deplacement

    def choixOrdre(self,direction):
        """
        adaptation direction en ordre
        """
        switcher={
        #Ordre deplacement -----------------            
                "toutDroit":'A',
                "gauche":'G',
                "droite":'D',
                # "diagGauche":'',
                # "diagDroite":'',
                "reculer":'R',
                "stop":'S',
        #Ordre Lumiere du canon ----------------- 
                "allumer":'O',
                "eteindre":'N',
        #Ordre deplacement ----------------- 
                "viserHaut":'H',
                "viserBas":'B',
                "viserGauche":'E',
                "viserDroite":'D',

            }

        self.order = switcher.get(direction)
        self.executerOrdre()

    def executerOrdre(self):
        """
        la partie serial pour communiquer
        """
        self.ser.write(self.order.encode())

class Deplacement(Robot):
    def __init__(self):
        pass
        
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


class Viser(Robot):
    """
    Paul : Liste1[bool(cible detecter ou non),freq1,freq2]
       Liste2[[bool, bool],[bool,bool]] --> 
                    apres 1ere viser :[[besoin d'ajuster? , sens d'ajustement : horizontal(True)/vertical],...]

    """
    def __init__(self):
        pass

    def bloquerDeplacement(self):
        self.choixOrdre('stop')
        self.depacementPossible = False


    def viser(self):
        '''
        recuperer les coords ?

        Pour l'envoie de l'ordre:  balisedeb = V /freq1/freq2 / balisfin = W
        '''
        pass 
    
    def verificationCiblage(self,listePaul2):
        #get ListPaul2 ?
        return listePaul2[0][0] and listePaul2[1][1]
        
    
    
    def ajusterViser(self,listePaul2):
        # CibleToucher?
        pass

    def tirer(self):
        self.viser()
        self.choixOrdre('allumer')
        sleep(3) #attente des sevomoteurs + check visuel
        cibleAtteinte = self.verificationCiblage()

        if cibleAtteinte:
            self.depacementPossible = True
            self.choixOrdre('eteindre')
        else:
            self.ajusterViser()


        
        


    