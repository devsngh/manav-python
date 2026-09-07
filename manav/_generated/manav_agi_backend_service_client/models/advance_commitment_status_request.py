from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvanceCommitmentStatusRequest")


@_attrs_define
class AdvanceCommitmentStatusRequest:
    """
    Attributes:
        new_status (str): verbal / soft_circle / signed_term_sheet / wired / fully_funded
        wired_amount (float | None | str | Unset):
    """

    new_status: str
    wired_amount: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_status = self.new_status

        wired_amount: float | None | str | Unset
        if isinstance(self.wired_amount, Unset):
            wired_amount = UNSET
        else:
            wired_amount = self.wired_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_status": new_status,
            }
        )
        if wired_amount is not UNSET:
            field_dict["wired_amount"] = wired_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_status = d.pop("new_status")

        def _parse_wired_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        wired_amount = _parse_wired_amount(d.pop("wired_amount", UNSET))

        advance_commitment_status_request = cls(
            new_status=new_status,
            wired_amount=wired_amount,
        )

        advance_commitment_status_request.additional_properties = d
        return advance_commitment_status_request

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
