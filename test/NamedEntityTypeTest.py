import unittest

from NamedEntityRecognition.NamedEntityType import NamedEntityType


class NamedEntityTypeTest(unittest.TestCase):

    def test_NamedEntityType(self):
        self.assertEqual(NamedEntityType.getNamedEntityType("person"), NamedEntityType.PERSON)
        self.assertEqual(NamedEntityType.getNamedEntityType("Time"), NamedEntityType.TIME)
        self.assertEqual(NamedEntityType.getNamedEntityType("location"), NamedEntityType.LOCATION)
