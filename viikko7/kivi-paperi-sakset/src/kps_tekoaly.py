from tekoaly import Tekoaly
from kivi_paperi_sakset import TekoalyVastustaja


class KPSTekoaly(TekoalyVastustaja):
    def __init__(self,io):
        super().__init__(io)
        self.tekoaly = Tekoaly()

