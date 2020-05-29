from Dictionary.Word import Word

from NamedEntityRecognition.NamedEntityType import NamedEntityType


class NamedEntityWord(Word):

    __namedEntityType: NamedEntityType

    def __init__(self, name: str, namedEntityType: NamedEntityType):
        """
        A constructor of NamedEntityWord which takes name and nameEntityType as input and sets the corresponding
        attributes

        PARAMETERS
        ----------
        name : str
            Name of the word
        namedEntityType : NamedEntityType
            NamedEntityType of the word
        """
        super().__init__(name)
        self.__namedEntityType = namedEntityType

    def getNamedEntityType(self) -> NamedEntityType:
        """
        Accessor method for namedEntityType attribute.

        RETURNS
        -------
        NamedEntityType
            namedEntityType of the word.
        """
        return self.__namedEntityType
