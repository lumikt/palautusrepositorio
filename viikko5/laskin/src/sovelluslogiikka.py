class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._log = []

    def miinus(self, operandi):
        self._log.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._log.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._log = []
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._log.append(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        if self._log == []:
            pass
        else:
            viimeisin = self._log.pop(-1)
            self._arvo = viimeisin