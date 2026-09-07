from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConvertAmountRequest")


@_attrs_define
class ConvertAmountRequest:
    """
    Attributes:
        amount (float | str):
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        as_of (datetime.date | None | Unset):
    """

    amount: float | str
    from_currency_id: UUID
    to_currency_id: UUID
    rate_type_id: UUID
    as_of: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: float | str
        amount = self.amount

        from_currency_id = str(self.from_currency_id)

        to_currency_id = str(self.to_currency_id)

        rate_type_id = str(self.rate_type_id)

        as_of: None | str | Unset
        if isinstance(self.as_of, Unset):
            as_of = UNSET
        elif isinstance(self.as_of, datetime.date):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "from_currency_id": from_currency_id,
                "to_currency_id": to_currency_id,
                "rate_type_id": rate_type_id,
            }
        )
        if as_of is not UNSET:
            field_dict["as_of"] = as_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        from_currency_id = UUID(d.pop("from_currency_id"))

        to_currency_id = UUID(d.pop("to_currency_id"))

        rate_type_id = UUID(d.pop("rate_type_id"))

        def _parse_as_of(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.date.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        as_of = _parse_as_of(d.pop("as_of", UNSET))

        convert_amount_request = cls(
            amount=amount,
            from_currency_id=from_currency_id,
            to_currency_id=to_currency_id,
            rate_type_id=rate_type_id,
            as_of=as_of,
        )

        convert_amount_request.additional_properties = d
        return convert_amount_request

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
