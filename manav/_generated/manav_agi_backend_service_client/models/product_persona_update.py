from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductPersonaUpdate")


@_attrs_define
class ProductPersonaUpdate:
    """
    Attributes:
        is_buyer (bool | None | Unset):
        is_user (bool | None | Unset):
        is_decision_maker (bool | None | Unset):
        is_influencer (bool | None | Unset):
        priority (int | None | Unset):
        notes (None | str | Unset):
    """

    is_buyer: bool | None | Unset = UNSET
    is_user: bool | None | Unset = UNSET
    is_decision_maker: bool | None | Unset = UNSET
    is_influencer: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_buyer: bool | None | Unset
        if isinstance(self.is_buyer, Unset):
            is_buyer = UNSET
        else:
            is_buyer = self.is_buyer

        is_user: bool | None | Unset
        if isinstance(self.is_user, Unset):
            is_user = UNSET
        else:
            is_user = self.is_user

        is_decision_maker: bool | None | Unset
        if isinstance(self.is_decision_maker, Unset):
            is_decision_maker = UNSET
        else:
            is_decision_maker = self.is_decision_maker

        is_influencer: bool | None | Unset
        if isinstance(self.is_influencer, Unset):
            is_influencer = UNSET
        else:
            is_influencer = self.is_influencer

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        def _parse_is_buyer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_buyer = _parse_is_buyer(d.pop("is_buyer", UNSET))

        def _parse_is_user(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_user = _parse_is_user(d.pop("is_user", UNSET))

        def _parse_is_decision_maker(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_decision_maker = _parse_is_decision_maker(d.pop("is_decision_maker", UNSET))

        def _parse_is_influencer(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_influencer = _parse_is_influencer(d.pop("is_influencer", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        product_persona_update = cls(
            is_buyer=is_buyer,
            is_user=is_user,
            is_decision_maker=is_decision_maker,
            is_influencer=is_influencer,
            priority=priority,
            notes=notes,
        )

        product_persona_update.additional_properties = d
        return product_persona_update

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
