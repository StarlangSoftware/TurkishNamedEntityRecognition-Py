import unittest

from NamedEntityRecognition.AutoNER import AutoNER


class GazetteerTest(unittest.TestCase):

    def test_Contains(self):
        gazetteer = AutoNER().locationGazetteer
        self.assertTrue(gazetteer.contains("bağdat"))
        self.assertTrue(gazetteer.contains("BAĞDAT"))
        self.assertTrue(gazetteer.contains("belçika"))
        self.assertTrue(gazetteer.contains("BELÇİKA"))
        self.assertTrue(gazetteer.contains("körfez"))
        self.assertTrue(gazetteer.contains("KÖRFEZ"))
        self.assertTrue(gazetteer.contains("küba"))
        self.assertTrue(gazetteer.contains("KÜBA"))
        self.assertTrue(gazetteer.contains("varşova"))
        self.assertTrue(gazetteer.contains("VARŞOVA"))
        self.assertTrue(gazetteer.contains("krallık"))
        self.assertTrue(gazetteer.contains("KRALLIK"))
        self.assertTrue(gazetteer.contains("berlin"))
        self.assertTrue(gazetteer.contains("BERLİN"))


if __name__ == '__main__':
    unittest.main()
