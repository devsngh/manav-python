from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadCreate")


@_attrs_define
class ThreadCreate:
    """Schema for creating a new chat thread

    Attributes:
        bot_id (UUID):
        org_id (None | Unset | UUID):
        initial_query (None | str | Unset):
        prefer_bot_id (None | str | Unset):
        deepagent_id (None | Unset | UUID):
    """

    bot_id: UUID
    org_id: None | Unset | UUID = UNSET
    initial_query: None | str | Unset = UNSET
    prefer_bot_id: None | str | Unset = UNSET
    deepagent_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id = str(self.bot_id)

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        initial_query: None | str | Unset
        if isinstance(self.initial_query, Unset):
            initial_query = UNSET
        else:
            initial_query = self.initial_query

        prefer_bot_id: None | str | Unset
        if isinstance(self.prefer_bot_id, Unset):
            prefer_bot_id = UNSET
        else:
            prefer_bot_id = self.prefer_bot_id

        deepagent_id: None | str | Unset
        if isinstance(self.deepagent_id, Unset):
            deepagent_id = UNSET
        elif isinstance(self.deepagent_id, UUID):
            deepagent_id = str(self.deepagent_id)
        else:
            deepagent_id = self.deepagent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if initial_query is not UNSET:
            field_dict["initial_query"] = initial_query
        if prefer_bot_id is not UNSET:
            field_dict["prefer_bot_id"] = prefer_bot_id
        if deepagent_id is not UNSET:
            field_dict["deepagent_id"] = deepagent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_id = UUID(d.pop("bot_id"))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_initial_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initial_query = _parse_initial_query(d.pop("initial_query", UNSET))

        def _parse_prefer_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefer_bot_id = _parse_prefer_bot_id(d.pop("prefer_bot_id", UNSET))

        def _parse_deepagent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deepagent_id_type_0 = UUID(data)

                return deepagent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deepagent_id = _parse_deepagent_id(d.pop("deepagent_id", UNSET))

        thread_create = cls(
            bot_id=bot_id,
            org_id=org_id,
            initial_query=initial_query,
            prefer_bot_id=prefer_bot_id,
            deepagent_id=deepagent_id,
        )

        thread_create.additional_properties = d
        return thread_create

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
