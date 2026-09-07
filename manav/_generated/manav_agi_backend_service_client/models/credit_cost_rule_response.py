from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditCostRuleResponse")


@_attrs_define
class CreditCostRuleResponse:
    """
    Attributes:
        id (UUID):
        metric_key (str):
        metric_name (str):
        credits_per_unit (int):
        unit_label (str):
        unit_quantity (int):
        is_active (bool):
        model_id (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    metric_key: str
    metric_name: str
    credits_per_unit: int
    unit_label: str
    unit_quantity: int
    is_active: bool
    model_id: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        metric_key = self.metric_key

        metric_name = self.metric_name

        credits_per_unit = self.credits_per_unit

        unit_label = self.unit_label

        unit_quantity = self.unit_quantity

        is_active = self.is_active

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

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
                "metric_key": metric_key,
                "metric_name": metric_name,
                "credits_per_unit": credits_per_unit,
                "unit_label": unit_label,
                "unit_quantity": unit_quantity,
                "is_active": is_active,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        metric_key = d.pop("metric_key")

        metric_name = d.pop("metric_name")

        credits_per_unit = d.pop("credits_per_unit")

        unit_label = d.pop("unit_label")

        unit_quantity = d.pop("unit_quantity")

        is_active = d.pop("is_active")

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

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

        credit_cost_rule_response = cls(
            id=id,
            metric_key=metric_key,
            metric_name=metric_name,
            credits_per_unit=credits_per_unit,
            unit_label=unit_label,
            unit_quantity=unit_quantity,
            is_active=is_active,
            model_id=model_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        credit_cost_rule_response.additional_properties = d
        return credit_cost_rule_response

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
