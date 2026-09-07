from enum import StrEnum


class ParameterType(StrEnum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    FLOAT = "float"
    INT = "int"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
