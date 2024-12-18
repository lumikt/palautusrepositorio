from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self,io):
        self.io = io
        
    def _toisen_siirto(self,ekan_siirto):
        return self.io.lue("Toisen pelaajan siirto: ")

