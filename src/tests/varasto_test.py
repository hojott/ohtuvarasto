import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_luo_negatiivisen_saldon(self):
        varasto = Varasto(10, -1)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_luo_negatiivisen_varaston(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_luo_liian_pienen_tilavuuden(self):
        varasto = Varasto(5, 10)
        self.assertAlmostEqual(varasto.saldo, 5)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_liikaa_tilaa(self):
        self.varasto.ota_varastosta(7)

        # varastossa pitäisi olla tilaa 4 + 7 = 11 -> 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ottaminen_negatiivista_tilaa(self):
        self.varasto.ota_varastosta(-1)

        # varastossa pitäisi olla tilaa 10 + 0 = 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_laittaminen_liikaa_tilaa(self):
        self.varasto.lisaa_varastoon(11)
        
        #varastossa pitäisi olla tilaa 10 - 11 = -1 -> 0
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_laittaminen_negatiivista_tilaa(self):
        self.varasto.ota_varastosta(10)
        self.varasto.lisaa_varastoon(-1)

        #varastossa pitäisi olla tilaa 0 + 10 - 0 = 10
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test___str__(self):
        self.assertEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")
