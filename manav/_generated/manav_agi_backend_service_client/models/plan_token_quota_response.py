from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanTokenQuotaResponse")


@_attrs_define
class PlanTokenQuotaResponse:
    """
    Attributes:
        id (UUID):
        plan_id (UUID):
        daily_token_limit (int):
        window_hours (int):
        window_strategy (str):
        overflow_policy (str):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    plan_id: UUID
    daily_token_limit: int
    window_hours: int
    window_strategy: str
    overflow_policy: str
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        plan_id = str(self.plan_id)

        daily_token_limit = self.daily_token_limit

        window_hours = self.window_hours

        window_strategy = self.window_strategy

        overflow_policy = self.overflow_policy

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "plan_id": plan_id,
                "daily_token_limit": daily_token_limit,
                "window_hours": window_hours,
                "window_strategy": window_strategy,
                "overflow_policy": overflow_policy,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        plan_id = UUID(d.pop("plan_id"))

        daily_token_limit = d.pop("daily_token_limit")

        window_hours = d.pop("window_hours")

        window_strategy = d.pop("window_strategy")

        overflow_policy = d.pop("overflow_policy")

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

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        plan_token_quota_response = cls(
            id=id,
            plan_id=plan_id,
            daily_token_limit=daily_token_limit,
            window_hours=window_hours,
            window_strategy=window_strategy,
            overflow_policy=overflow_policy,
            created_at=created_at,
            updated_at=updated_at,
        )

        plan_token_quota_response.additional_properties = d
        return plan_token_quota_response

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
