from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalPolicyCreate")


@_attrs_define
class ApprovalPolicyCreate:
    """
    Attributes:
        name (str):
        resource_type (str): e.g. publish_package / ad_brief / purchase_order
        description (None | str | Unset):
        is_active (bool | Unset):  Default: True.
        effective_from (datetime.date | None | Unset):
        effective_until (datetime.date | None | Unset):
    """

    name: str
    resource_type: str
    description: None | str | Unset = UNSET
    is_active: bool | Unset = True
    effective_from: datetime.date | None | Unset = UNSET
    effective_until: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resource_type = self.resource_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active = self.is_active

        effective_from: None | str | Unset
        if isinstance(self.effective_from, Unset):
            effective_from = UNSET
        elif isinstance(self.effective_from, datetime.date):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        effective_until: None | str | Unset
        if isinstance(self.effective_until, Unset):
            effective_until = UNSET
        elif isinstance(self.effective_until, datetime.date):
            effective_until = self.effective_until.isoformat()
        else:
            effective_until = self.effective_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resource_type": resource_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if effective_until is not UNSET:
            field_dict["effective_until"] = effective_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        resource_type = d.pop("resource_type")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_effective_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.date.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_from = _parse_effective_from(d.pop("effective_from", UNSET))

        def _parse_effective_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_until_type_0 = datetime.date.fromisoformat(data)

                return effective_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_until = _parse_effective_until(d.pop("effective_until", UNSET))

        approval_policy_create = cls(
            name=name,
            resource_type=resource_type,
            description=description,
            is_active=is_active,
            effective_from=effective_from,
            effective_until=effective_until,
        )

        approval_policy_create.additional_properties = d
        return approval_policy_create

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
