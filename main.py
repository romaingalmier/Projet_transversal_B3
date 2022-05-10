import serial
import Autonome as Au


if __name__ == '__main__':
    '''

        getCible{

            while . . .
        }


    '''

    Robot = Au.Robot()
    print(type(Robot))
    Viser = Au.Viser()
    Deplacement = Au.Deplacement()

    while True :
        #TODO Recuperer listes et les metttres en parametres 
        Deplacement.getListeTom()
        Viser.getListePaul1()
    #-------------------------------------

        if Viser.detectionCible():

            Deplacement.bloquerDeplacement()

            Viser.sequenceDeTir()


            

            Deplacement.activerDeplacement()


