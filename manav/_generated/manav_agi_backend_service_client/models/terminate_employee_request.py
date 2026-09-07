from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TerminateEmployeeRequest")


@_attrs_define
class TerminateEmployeeRequest:
    """
    Attributes:
        termination_date (datetime.date | None | Unset):
    """

    termination_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        termination_date: None | str | Unset
        if isinstance(self.termination_date, Unset):
            termination_date = UNSET
        elif isinstance(self.termination_date, datetime.date):
            termination_date = self.termination_date.isoformat()
        else:
            termination_date = self.termination_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if termination_date is not UNSET:
            field_dict["termination_date"] = termination_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_termination_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_date_type_0 = datetime.date.fromisoformat(data)

                return termination_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        termination_date = _parse_termination_date(d.pop("termination_date", UNSET))

        terminate_employee_request = cls(
            termination_date=termination_date,
        )

        terminate_employee_request.additional_properties = d
        return terminate_employee_request

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
