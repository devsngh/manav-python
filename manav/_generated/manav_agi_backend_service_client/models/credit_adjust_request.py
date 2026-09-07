from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreditAdjustRequest")


@_attrs_define
class CreditAdjustRequest:
    """
    Attributes:
        org_id (UUID):
        amount (int):
        description (str):
    """

    org_id: UUID
    amount: int
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = str(self.org_id)

        amount = self.amount

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "amount": amount,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_id = UUID(d.pop("org_id"))

        amount = d.pop("amount")

        description = d.pop("description")

        credit_adjust_request = cls(
            org_id=org_id,
            amount=amount,
            description=description,
        )

        credit_adjust_request.additional_properties = d
        return credit_adjust_request

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
