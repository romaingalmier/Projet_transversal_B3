import serial
import Autonome as Au

listePaul1 = [False, 404,50]
listeTom =  [False,False,False,True,False]
if __name__ == '__main__':
    
    Viser = Au.Viser()
    Deplacement = Au.Deplacement()

    while True :
        #TODO Recuperer listes et les metttres en parametres 
        Deplacement.getlisteTom(listeTom)
        Viser.getlistePaul1(listePaul1)
        #-------------------------------------

        if Viser.detectionCible():
            print("cible detecter")
            Deplacement.bloquerDeplacement()
            Viser.sequenceDeTir()
            Deplacement.activerDeplacement()
        
        Deplacement.choixDirection()
        

