from Corpus.Sentence import Sentence

from NamedEntityRecognition.NamedEntityType import NamedEntityType
from NamedEntityRecognition.NamedEntityWord import NamedEntityWord


class NamedEntitySentence(Sentence):

    def __init__(self, sentence: str = None):
        """
        Another constructor of NamedEntitySentence. It takes input a named entity annotated sentence in string
        form, divides the sentence with respect to space and sets the tagged words with respect to their tags.

        PARAMETERS
        ----------
        sentence : str
            Named Entity annotated sentence in string form
        """
        if sentence is None:
            super().__init__()
        else:
            named_entity_type = NamedEntityType.NONE
            self.words = []
            word_array = sentence.split()
            for word in word_array:
                if len(word) != 0:
                    if word != "<b_enamex":
                        if word.startswith("TYPE=\""):
                            type_index_end = word.index('\"', 6)
                            if type_index_end != -1:
                                entityType = word[6: type_index_end]
                                named_entity_type = NamedEntityType.getNamedEntityType(entityType)
                            if word.endswith("e_enamex>"):
                                candidate = word[word.index('>') + 1: word.index('<')]
                                if len(candidate) != 0:
                                    self.words.append(NamedEntityWord(candidate, named_entity_type))
                                named_entity_type = NamedEntityType.NONE
                            else:
                                candidate = word[word.index('>') + 1:]
                                if len(candidate) != 0:
                                    self.words.append(NamedEntityWord(candidate, named_entity_type))
                        else:
                            if word.endswith("e_enamex>"):
                                candidate = word[0: word.index('<')]
                                if len(candidate) != 0:
                                    self.words.append(NamedEntityWord(candidate, named_entity_type))
                                named_entity_type = NamedEntityType.NONE
                            else:
                                if len(word) != 0:
                                    self.words.append(NamedEntityWord(word, named_entity_type))
