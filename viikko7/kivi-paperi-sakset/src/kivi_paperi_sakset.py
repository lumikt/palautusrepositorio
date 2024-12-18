from tuomari import Tuomari

class KonsoliIO:
    def lue(self, teksti):
        return input(teksti)
    
    def kirjoita(self, teksti):
        return print(teksti)



class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self.io.lue("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._toisen_siirto(ekan_siirto)



        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.io.kirjoita(tuomari)

            ekan_siirto = self.io.lue("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        self.io.kirjoita("Kiitos!")
        self.io.kirjoita(tuomari)
        


    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        raise Exception("Tämä metodi pitää korvata aliluokassa")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

class TekoalyVastustaja(KiviPaperiSakset):
    def __init__(self, io):
        self.io = io

    def _toisen_siirto(self,ekan_siirto):
        self.tekoaly.aseta_siirto(ekan_siirto)

        vastaus = self.tekoaly.anna_siirto()
        self.io.kirjoita("Tietokone valitsi: "+ str(vastaus))
        
        return vastaus