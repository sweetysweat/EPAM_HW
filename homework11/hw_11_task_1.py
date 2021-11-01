"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum

class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"

class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"

Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")

class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")

assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    def __new__(mcs: type, class_name: str, parent_classes: tuple, attrs: dict) -> "SimplifiedEnum":
        attr_with_enums = f"_{class_name}__keys"
        new_attrs = {element: element for element in attrs[attr_with_enums]}
        return super(SimplifiedEnum, mcs).__new__(mcs, class_name, parent_classes, new_attrs)
