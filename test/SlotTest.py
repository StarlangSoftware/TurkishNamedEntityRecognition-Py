import unittest

from NamedEntityRecognition.Slot import Slot
from NamedEntityRecognition.SlotType import SlotType


class SlotTest(unittest.TestCase):

    def test_slot(self):
        slot1 = Slot("B-depart_date.month_name")
        self.assertEqual(SlotType.B, slot1.getType())
        self.assertEqual("depart_date.month_name", slot1.getTag())
        self.assertEqual("B-depart_date.month_name", slot1.__str__())
        slot2 = Slot("O")
        self.assertEqual(SlotType.O, slot2.getType())
        self.assertEqual("O", slot2.__str__())
        slot3 = Slot("I-round_trip")
        self.assertEqual(SlotType.I, slot3.getType())
        self.assertEqual("round_trip", slot3.getTag())
        self.assertEqual("I-round_trip", slot3.__str__())


if __name__ == '__main__':
    unittest.main()
