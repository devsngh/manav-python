from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentActivationItem")


@_attrs_define
class AgentActivationItem:
    """One row in the left-rail agent picker.

    Attributes:
        name (str):
        agent_id (str):
        initial (str):
        is_active (bool):
        bot_id (None | str | Unset):
        tier (None | str | Unset):
        profile_picture_url (None | str | Unset):
        activated_at (datetime.datetime | None | Unset):
        is_booting (bool | Unset):  Default: False.
        is_booted (bool | Unset):  Default: False.
        is_dormant (bool | Unset):  Default: True.
        triggered_by (None | str | Unset):
        cabinet_files (int | Unset):  Default: 0.
    """

    name: str
    agent_id: str
    initial: str
    is_active: bool
    bot_id: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    activated_at: datetime.datetime | None | Unset = UNSET
    is_booting: bool | Unset = False
    is_booted: bool | Unset = False
    is_dormant: bool | Unset = True
    triggered_by: None | str | Unset = UNSET
    cabinet_files: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        agent_id = self.agent_id

        initial = self.initial

        is_active = self.is_active

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        activated_at: None | str | Unset
        if isinstance(self.activated_at, Unset):
            activated_at = UNSET
        elif isinstance(self.activated_at, datetime.datetime):
            activated_at = self.activated_at.isoformat()
        else:
            activated_at = self.activated_at

        is_booting = self.is_booting

        is_booted = self.is_booted

        is_dormant = self.is_dormant

        triggered_by: None | str | Unset
        if isinstance(self.triggered_by, Unset):
            triggered_by = UNSET
        else:
            triggered_by = self.triggered_by

        cabinet_files = self.cabinet_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "agent_id": agent_id,
                "initial": initial,
                "is_active": is_active,
            }
        )
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if tier is not UNSET:
            field_dict["tier"] = tier
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if activated_at is not UNSET:
            field_dict["activated_at"] = activated_at
        if is_booting is not UNSET:
            field_dict["is_booting"] = is_booting
        if is_booted is not UNSET:
            field_dict["is_booted"] = is_booted
        if is_dormant is not UNSET:
            field_dict["is_dormant"] = is_dormant
        if triggered_by is not UNSET:
            field_dict["triggered_by"] = triggered_by
        if cabinet_files is not UNSET:
            field_dict["cabinet_files"] = cabinet_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        agent_id = d.pop("agent_id")

        initial = d.pop("initial")

        is_active = d.pop("is_active")

        def _parse_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url", UNSET))

        def _parse_activated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activated_at_type_0 = datetime.datetime.fromisoformat(data)

                return activated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        activated_at = _parse_activated_at(d.pop("activated_at", UNSET))

        is_booting = d.pop("is_booting", UNSET)

        is_booted = d.pop("is_booted", UNSET)

        is_dormant = d.pop("is_dormant", UNSET)

        def _parse_triggered_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        triggered_by = _parse_triggered_by(d.pop("triggered_by", UNSET))

        cabinet_files = d.pop("cabinet_files", UNSET)

        agent_activation_item = cls(
            name=name,
            agent_id=agent_id,
            initial=initial,
            is_active=is_active,
            bot_id=bot_id,
            tier=tier,
            profile_picture_url=profile_picture_url,
            activated_at=activated_at,
            is_booting=is_booting,
            is_booted=is_booted,
            is_dormant=is_dormant,
            triggered_by=triggered_by,
            cabinet_files=cabinet_files,
        )

        agent_activation_item.additional_properties = d
        return agent_activation_item

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
