from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ast_class import AstClass
    from ..models.ast_function import AstFunction


T = TypeVar("T", bound="AstResponse")


@_attrs_define
class AstResponse:
    """
    Attributes:
        language (str):
        functions (list[AstFunction]):
        classes (list[AstClass]):
        top_level_lines (int):
        total_lines (int):
    """

    language: str
    functions: list[AstFunction]
    classes: list[AstClass]
    top_level_lines: int
    total_lines: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        functions = []
        for functions_item_data in self.functions:
            functions_item = functions_item_data.to_dict()
            functions.append(functions_item)

        classes = []
        for classes_item_data in self.classes:
            classes_item = classes_item_data.to_dict()
            classes.append(classes_item)

        top_level_lines = self.top_level_lines

        total_lines = self.total_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "functions": functions,
                "classes": classes,
                "top_level_lines": top_level_lines,
                "total_lines": total_lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ast_class import AstClass  # noqa: PLC0415
        from ..models.ast_function import AstFunction  # noqa: PLC0415

        d = dict(src_dict)
        language = d.pop("language")

        functions = []
        _functions = d.pop("functions")
        for functions_item_data in _functions:
            functions_item = AstFunction.from_dict(functions_item_data)

            functions.append(functions_item)

        classes = []
        _classes = d.pop("classes")
        for classes_item_data in _classes:
            classes_item = AstClass.from_dict(classes_item_data)

            classes.append(classes_item)

        top_level_lines = d.pop("top_level_lines")

        total_lines = d.pop("total_lines")

        ast_response = cls(
            language=language,
            functions=functions,
            classes=classes,
            top_level_lines=top_level_lines,
            total_lines=total_lines,
        )

        ast_response.additional_properties = d
        return ast_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
