from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import TekoalyVastustaja

class KPSParempiTekoaly(TekoalyVastustaja):
    def __init__(self,io):
        super().__init__(io)
        self.tekoaly = TekoalyParannettu(10)


