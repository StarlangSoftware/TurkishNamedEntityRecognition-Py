import unittest

from DataStructure.CounterHashMap import CounterHashMap

from NamedEntityRecognition.NERCorpus import NERCorpus
from NamedEntityRecognition.NamedEntityType import NamedEntityType


class NERCorpusTest(unittest.TestCase):

    def test_NERCorpus(self):
        counter = CounterHashMap()
        nerCorpus = NERCorpus("../nerdata.txt")
        self.assertEqual(27556, nerCorpus.sentenceCount())
        self.assertEqual(492233, nerCorpus.numberOfWords())
        for i in range(nerCorpus.sentenceCount()):
            namedEntitySentence = nerCorpus.getSentence(i)
            for j in range(namedEntitySentence.wordCount()):
                namedEntityWord = namedEntitySentence.getWord(j)
                counter.put(namedEntityWord.getNamedEntityType())
        self.assertEqual(438976, counter[NamedEntityType.NONE])
        self.assertEqual(23878, counter[NamedEntityType.PERSON])
        self.assertEqual(16931, counter[NamedEntityType.ORGANIZATION])
        self.assertEqual(12448, counter[NamedEntityType.LOCATION])


if __name__ == '__main__':
    unittest.main()
