from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanFeatureResponse")


@_attrs_define
class PlanFeatureResponse:
    """
    Attributes:
        id (UUID):
        plan_id (UUID):
        feature_key (str):
        feature_name (str):
        is_enabled (bool):
        sort_order (int):
        description (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    plan_id: UUID
    feature_key: str
    feature_name: str
    is_enabled: bool
    sort_order: int
    description: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        plan_id = str(self.plan_id)

        feature_key = self.feature_key

        feature_name = self.feature_name

        is_enabled = self.is_enabled

        sort_order = self.sort_order

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "plan_id": plan_id,
                "feature_key": feature_key,
                "feature_name": feature_name,
                "is_enabled": is_enabled,
                "sort_order": sort_order,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        plan_id = UUID(d.pop("plan_id"))

        feature_key = d.pop("feature_key")

        feature_name = d.pop("feature_name")

        is_enabled = d.pop("is_enabled")

        sort_order = d.pop("sort_order")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        plan_feature_response = cls(
            id=id,
            plan_id=plan_id,
            feature_key=feature_key,
            feature_name=feature_name,
            is_enabled=is_enabled,
            sort_order=sort_order,
            description=description,
            created_at=created_at,
        )

        plan_feature_response.additional_properties = d
        return plan_feature_response

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
