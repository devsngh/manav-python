from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductPersonaResponse")


@_attrs_define
class ProductPersonaResponse:
    """
    Attributes:
        id (UUID):
        product_id (UUID):
        persona_id (UUID):
        is_buyer (bool):
        is_user (bool):
        is_decision_maker (bool):
        is_influencer (bool):
        priority (int):
        notes (None | str):
        created_at (datetime.datetime):
    """

    id: UUID
    product_id: UUID
    persona_id: UUID
    is_buyer: bool
    is_user: bool
    is_decision_maker: bool
    is_influencer: bool
    priority: int
    notes: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        product_id = str(self.product_id)

        persona_id = str(self.persona_id)

        is_buyer = self.is_buyer

        is_user = self.is_user

        is_decision_maker = self.is_decision_maker

        is_influencer = self.is_influencer

        priority = self.priority

        notes: None | str
        notes = self.notes

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product_id": product_id,
                "persona_id": persona_id,
                "is_buyer": is_buyer,
                "is_user": is_user,
                "is_decision_maker": is_decision_maker,
                "is_influencer": is_influencer,
                "priority": priority,
                "notes": notes,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        product_id = UUID(d.pop("product_id"))

        persona_id = UUID(d.pop("persona_id"))

        is_buyer = d.pop("is_buyer")

        is_user = d.pop("is_user")

        is_decision_maker = d.pop("is_decision_maker")

        is_influencer = d.pop("is_influencer")

        priority = d.pop("priority")

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        product_persona_response = cls(
            id=id,
            product_id=product_id,
            persona_id=persona_id,
            is_buyer=is_buyer,
            is_user=is_user,
            is_decision_maker=is_decision_maker,
            is_influencer=is_influencer,
            priority=priority,
            notes=notes,
            created_at=created_at,
        )

        product_persona_response.additional_properties = d
        return product_persona_response

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
