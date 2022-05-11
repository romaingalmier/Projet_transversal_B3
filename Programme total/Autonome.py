"""
Tom/harou : Liste[T,T,F,...,T] True/False --> oblstacle a un certain angle 
Paul : Liste1[bool(cible detecter ou non),freq1,freq2]
       Liste2[[bool, bool],[bool,bool]] --> 
                    apres 1ere viser :[[besoin d'ajuster? , sens d'ajustement : horizontal(True)/vertical],...]

"""
import serial
from time import sleep

L = [[True],False,False,True,True]


class Robot:
    def __init__(self):
        self.order = "S"
        # self.ser = serial.Serial("/dev/ttyUSB0", baudrate = 19200)

        
    def choixOrdre(self,direction):
        """
        adaptation direction en ordre
        """
        switcher={
        #Ordre deplacement -----------------            
                "toutDroit":'A',
                "gauche":'G',
                "droite":'D',
                "diagGauche":'G',
                "diagDroite":'D',
                "reculer":'R',
                "stop":'S',
        #Ordre Lumiere du canon ----------------- 
                "allumer":'O',
                "eteindre":'N',
        #Ordre Viser ----------------- 
                "viserHaut":'H',
                "viserBas":'B',
                "viserGauche":'E',
                "viserDroite":'D',

                "baliseDebut" :'V',
                "baliseFin" :'W',
            }

        self.order = switcher.get(direction)
        self.executerOrdre()

    # def executerOrdre(self):
    #     """
    #     la partie serial pour communiquer
    #     """
    #     print(self.order)
    #     # self.ser.write(self.order.encode())

    def executerOrdre(self,ordre = -1):
        """
        la partie serial pour communiquer
        """
        if ordre == -1 :
            # self.ser.write(self.order.encode())
            print(self.order)
        else :
            print(ordre)
            # self.ser.write(ordre.encode())

class Deplacement(Robot):
    def __init__(self):
        self.listeTom = []
        self.depacementPossible = True # Bool pour activer ou desactiver le deplacement

        
    def traitementListe(self):
        #return self.listeTom[0][0],self.listeTom[1][0],self.listeTom[2][0],self.listeTom[3][0],self.listeTom[4][0]
        return self.listeTom[0],self.listeTom[1],self.listeTom[2],self.listeTom[3],self.listeTom[4]

    def choixDirection(self):
        """
        en fonction de la liste arbre de décision

        @return direction : zone choisit 
        """
        #TODO 4 tourner a gauche/droite
        gauche, diagGauche, toutDroit, diagDroite, droite = self.traitementListe()
        if self.depacementPossible : 
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

    def bloquerDeplacement(self):
        self.choixOrdre('stop')
        self.depacementPossible = False
    
    def activerDeplacement(self):
        self.depacementPossible = True
        self.choixDirection()
        #choixDirecton() ?

    def getlisteTom(self,liste):
        self.listeTom = liste



class Viser(Robot):
    """
    Paul : Liste1[bool(cible detecter ou non),freq1,freq2]
       Liste2[[bool, bool],[bool,bool]] --> 
                    apres 1ere viser :[[besoin d'ajuster? , sens d'ajustement : horizontal(True)/vertical],...]

    """
    def __init__(self):
        self.listePaul1 = []
        self.listePaul2 = []
        
    def getlistePaul1(self,liste):
        self.listePaul1 = liste

    def getlistePaul2(self,liste):
        self.listePaul1 = liste

    def detectionCible(self):
        return self.listePaul1[0]


    def viser(self):
        self.choixOrdre('baliseDebut')
        
        freqX = conversionIntlisteStr(self.listePaul1[1])
        freqY = conversionIntlisteStr(self.listePaul1[2])
        freq = freqX+freqY
        for i in range(len(freq)):
            self.executerOrdre(int(freq[i]))

        self.choixOrdre('baliseFin')
        
    def tirer(self):
        self.choixOrdre('allumer')
        sleep(0.3) #attente des sevomoteurs + check visuel
        # cibleAtteinte = self.verificationCiblage()
        self.choixOrdre('eteindre')
        # if cibleAtteinte:
        #     self.choixOrdre('eteindre')
        # else:
        #     self.ajusterViser()

    def sequenceDeTir(self):   
        self.viser()
        self.tirer()

    def verificationCiblage(self):
        #get ListPaul2 ?
        return self.listePaul2[0][0] and self.listePaul2[1][1]
        
    def ajusterViser(self):
        # CibleToucher?
        pass
    
        
        
def conversionIntlisteStr(n):
    L=list(str(n))
    for i in range(len(L)):
        L[i]=int(L[i])
    return L
    