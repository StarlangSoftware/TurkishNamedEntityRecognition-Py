from NamedEntityRecognition.SlotType import SlotType


class Slot:

    type: SlotType
    tag: str

    def constructor1(self, type: SlotType, tag: str):
        """
        Constructor for the Slot object. Slot object stores the information about more specific entities. The slot
        type represents the beginning, inside or outside the slot, whereas tag represents the entity tag of the
        slot.
        :param type: Type of the slot. B, I or O for beginning, inside, outside the slot respectively.
        :param tag: Tag of the slot.
        """
        self.type = type
        self.tag = tag

    def constructor2(self, slot: str):
        """
        Second constructor of the slot for a given slot string. A Slot string consists of slot type and slot tag
        separated with '-'. For example B-Person represents the beginning of a person. For outside tagging simple 'O' is
        used.
        :param slot: Input slot string.
        """
        if slot == "O":
            self.type = SlotType.O
            self.tag = ""
        else:
            _type = slot[0:slot.find("-")]
            _tag = slot[slot.find("-") + 1:]
            if _type == "B":
                self.type = SlotType.B
            elif _type == "I":
                self.type = SlotType.I
            self.tag = _tag

    def __init__(self,
                 tag: str,
                 type: SlotType = None):
        if type is not None:
            self.constructor1(type, tag)
        else:
            self.constructor2(tag)

    def getType(self) -> SlotType:
        """
        Accessor for the type of the slot.
        :return: Type of the slot.
        """
        return self.type

    def getTag(self) -> str:
        """
        Accessor for the tag of the slot.
        :return: Tag of the slot.
        """
        return self.tag

    def __str__(self) -> str:
        """
        __str__ method of the slot.
        :return: Type and tag separated with '-'. If the type is outside, it returns 'O'.
        """
        if self.type == SlotType.O:
            return "O"
        elif self.type == SlotType.B or self.type == SlotType.I:
            return self.type.name + "-" + self.tag
        return ""
