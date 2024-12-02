KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0 for i in range(0,koko)] #* koko
    
    def __init__(self, kapasiteetti:int =None, kasvatuskoko:int =None):
        if kapasiteetti == None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti=kapasiteetti

        if kasvatuskoko == None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko
        

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, etsittava_luku):
        for i in range(0, self.alkioiden_lkm):
            if etsittava_luku == self.ljono[i]:
                return True
        return False



    def lisaa(self, lisattava_luku):
        if not self.kuuluu(lisattava_luku):
            self.ljono[self.alkioiden_lkm] = lisattava_luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono

                self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)
            return True
            
        return False

    def poista(self, poistettava_luku):
        for i in range(0, self.alkioiden_lkm):
            if poistettava_luku == self.ljono[i]:
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]
                    self.ljono[j + 1] = 0

                self.alkioiden_lkm -= 1 
                return True

        return False

    def kopioi_lista(self, kopioitava_lista, uusi_lista):
        for i in range(0, len(kopioitava_lista)):
            uusi_lista[i] = kopioitava_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste_taulu.lisaa(a_taulu[i])
            yhdiste_taulu.lisaa(b_taulu[i])

        return yhdiste_taulu

    @staticmethod
    def leikkaus(a, b):
        leikkaus_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        
        for alkio in a_taulu:
            if b.kuuluu(alkio):
                leikkaus_taulu.lisaa(alkio)

        return leikkaus_taulu

    @staticmethod
    def erotus(a, b):
        erotus_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            if not b.kuuluu(alkio):
                erotus_taulu.lisaa(alkio)
        
        return erotus_taulu

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos += str(self.ljono[i]) +", "
            tuotos += str(self.ljono[self.alkioiden_lkm - 1])+ "}"
            return tuotos
