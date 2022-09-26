from Dictionary.Word import Word

from NamedEntityRecognition.NamedEntityType import NamedEntityType


class NamedEntityWord(Word):

    __named_entity_type: NamedEntityType

    def __init__(self,
                 name: str,
                 namedEntityType: NamedEntityType):
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
        self.__named_entity_type = namedEntityType

    def getNamedEntityType(self) -> NamedEntityType:
        """
        Accessor method for namedEntityType attribute.

        RETURNS
        -------
        NamedEntityType
            namedEntityType of the word.
        """
        return self.__named_entity_type

    def __repr__(self):
        return f"{self.name} {self.__named_entity_type}"
