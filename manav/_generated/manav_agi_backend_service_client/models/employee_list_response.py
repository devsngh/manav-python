from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.employee_response import EmployeeResponse


T = TypeVar("T", bound="EmployeeListResponse")


@_attrs_define
class EmployeeListResponse:
    """
    Attributes:
        employees (list[EmployeeResponse]):
        total (int):
        page (int):
        page_size (int):
    """

    employees: list[EmployeeResponse]
    total: int
    page: int
    page_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        employees = []
        for employees_item_data in self.employees:
            employees_item = employees_item_data.to_dict()
            employees.append(employees_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "employees": employees,
                "total": total,
                "page": page,
                "page_size": page_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.employee_response import EmployeeResponse  # noqa: PLC0415

        d = dict(src_dict)
        employees = []
        _employees = d.pop("employees")
        for employees_item_data in _employees:
            employees_item = EmployeeResponse.from_dict(employees_item_data)

            employees.append(employees_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        employee_list_response = cls(
            employees=employees,
            total=total,
            page=page,
            page_size=page_size,
        )

        employee_list_response.additional_properties = d
        return employee_list_response

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
