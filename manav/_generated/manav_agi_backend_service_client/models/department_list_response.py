from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.department_response import DepartmentResponse


T = TypeVar("T", bound="DepartmentListResponse")


@_attrs_define
class DepartmentListResponse:
    """List of departments

    Attributes:
        departments (list[DepartmentResponse]):
        total (int):
    """

    departments: list[DepartmentResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        departments = []
        for departments_item_data in self.departments:
            departments_item = departments_item_data.to_dict()
            departments.append(departments_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "departments": departments,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.department_response import DepartmentResponse  # noqa: PLC0415

        d = dict(src_dict)
        departments = []
        _departments = d.pop("departments")
        for departments_item_data in _departments:
            departments_item = DepartmentResponse.from_dict(departments_item_data)

            departments.append(departments_item)

        total = d.pop("total")

        department_list_response = cls(
            departments=departments,
            total=total,
        )

        department_list_response.additional_properties = d
        return department_list_response

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
