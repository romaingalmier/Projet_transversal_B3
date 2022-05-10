def viser(self):
    self.choixOrdre('baliseDebut')
    
    freqX = conversion(self.listePaul1[1]);
    freqY = conversion(self.listePaul1[2]);
    freq = freqX+freqY;
    for i in range(len(freq)):
        self.executerOrdre(int(freq[i]))
    self.choixOrdre('baliseFin')
    
    
def conversion(n):
    L=list(str(n))
    for i in range(len(L)):
        L[i]=int(L[i])
    return L