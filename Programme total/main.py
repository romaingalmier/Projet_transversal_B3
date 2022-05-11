import serial
import Autonome as Au
import cible 
import lidar

listePaul1 = [False, 404,50]
listeTom =  [False,False,False,True,False]
if __name__ == '__main__':
    
    Viser = Au.Viser()
    Deplacement = Au.Deplacement()

    while True :
        #TODO Recuperer listes et les metttres en parametres 
        Deplacement.getlisteTom(lidar.donnee())
        Viser.getlistePaul1(cible.lancer_detection(1))
        #-------------------------------------

        if Viser.detectionCible():
            print("cible detecter")
            Deplacement.bloquerDeplacement()
            Viser.sequenceDeTir()
            Deplacement.activerDeplacement()
        else : 
            Deplacement.choixDirection()
        

