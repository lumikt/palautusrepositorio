import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaaja_haku(self):
        haku = self.stats.search("Kurri")
        
        self.assertAlmostEqual(haku.name, "Kurri")

    def test_joukkue_haku(self):
        haku = self.stats.team("PIT")

        self.assertAlmostEqual(haku[0].name, "Lemieux")
    
    def test_top_pelaajat(self):
        haku = self.stats.top(1)

        self.assertAlmostEqual(haku[0].name, "Gretzky")

    def test_pelaaja_ei_loydy(self):
        haku = self.stats.search("Messi")

        self.assertAlmostEqual(haku, None)