from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductPersonaLink")


@_attrs_define
class ProductPersonaLink:
    """
    Attributes:
        persona_id (UUID):
        is_buyer (bool | Unset):  Default: False.
        is_user (bool | Unset):  Default: False.
        is_decision_maker (bool | Unset):  Default: False.
        is_influencer (bool | Unset):  Default: False.
        priority (int | Unset):  Default: 50.
        notes (None | str | Unset):
    """

    persona_id: UUID
    is_buyer: bool | Unset = False
    is_user: bool | Unset = False
    is_decision_maker: bool | Unset = False
    is_influencer: bool | Unset = False
    priority: int | Unset = 50
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        persona_id = str(self.persona_id)

        is_buyer = self.is_buyer

        is_user = self.is_user

        is_decision_maker = self.is_decision_maker

        is_influencer = self.is_influencer

        priority = self.priority

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "persona_id": persona_id,
            }
        )
        if is_buyer is not UNSET:
            field_dict["is_buyer"] = is_buyer
        if is_user is not UNSET:
            field_dict["is_user"] = is_user
        if is_decision_maker is not UNSET:
            field_dict["is_decision_maker"] = is_decision_maker
        if is_influencer is not UNSET:
            field_dict["is_influencer"] = is_influencer
        if priority is not UNSET:
            field_dict["priority"] = priority
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persona_id = UUID(d.pop("persona_id"))

        is_buyer = d.pop("is_buyer", UNSET)

        is_user = d.pop("is_user", UNSET)

        is_decision_maker = d.pop("is_decision_maker", UNSET)

        is_influencer = d.pop("is_influencer", UNSET)

        priority = d.pop("priority", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        product_persona_link = cls(
            persona_id=persona_id,
            is_buyer=is_buyer,
            is_user=is_user,
            is_decision_maker=is_decision_maker,
            is_influencer=is_influencer,
            priority=priority,
            notes=notes,
        )

        product_persona_link.additional_properties = d
        return product_persona_link

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
