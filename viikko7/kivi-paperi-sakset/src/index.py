from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kivi_paperi_sakset import KonsoliIO



class PeliTehdas:
    @staticmethod
    def luo_peli(tyyppi,io):
        if tyyppi == "a":
            return KPSPelaajaVsPelaaja(io)
        if tyyppi == "b":
            return KPSTekoaly(io)
        if tyyppi == "c":
            return KPSParempiTekoaly(io)

        return None    


class PelaaKPS:

    def __init__(self,io):
        self.io = io

    def suorita(self):
        while True:
            self.io.kirjoita("Valitse pelataanko"
                  "\n (a) Ihmistä vastaan"
                  "\n (b) Tekoälyä vastaan"
                  "\n (c) Parannettua tekoälyä vastaan"
                  "\nMuilla valinnoilla lopetetaan"
                  )

            peli = PeliTehdas.luo_peli(self.io.lue("Valitse peli: "),self.io)
            if peli == None:
                break
            peli.pelaa()



def main():
    kps = PelaaKPS(KonsoliIO())
    kps.suorita()

if __name__ == "__main__":
    main()
