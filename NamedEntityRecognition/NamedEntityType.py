from __future__ import annotations
from enum import Enum, auto

"""
Enumerator class for Named Entity types.
"""


class NamedEntityType(Enum):
    NONE = auto()
    PERSON = auto()
    ORGANIZATION = auto()
    LOCATION = auto()
    TIME = auto()
    MONEY = auto()

    @staticmethod
    def getNamedEntityType(entityType: str) -> NamedEntityType:
        """
        Static function to convert a string entity type to NamedEntityType type.

        PARAMETERS
        ----------
        entityType : str
            Entity type in string form

        RETURNS
        -------
        NamedEntityType
            Entity type in NamedEntityType form
        """
        for _type in NamedEntityType:
            if entityType == _type.name:
                return _type
        return NamedEntityType.NONE

    @staticmethod
    def getNamedEntityString(namedEntityType: NamedEntityType) -> str:
        """
        Static function to convert a NamedEntityType to string form.

        PARAMETERS
        ----------
        namedEntityType : NamedEntityType
            Entity type in NamedEntityType form

        RETURNS
        -------
        str
            Entity type in string form
        """
        if namedEntityType is None:
            return "NONE"
        return namedEntityType.name
