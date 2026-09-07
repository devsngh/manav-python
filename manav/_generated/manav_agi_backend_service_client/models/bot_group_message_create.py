from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_group_message_create_metadata_type_0 import BotGroupMessageCreateMetadataType0


T = TypeVar("T", bound="BotGroupMessageCreate")


@_attrs_define
class BotGroupMessageCreate:
    """Schema for sending a bot group message.

    `group_id` is optional in the body — the path parameter is canonical.
    The route validates a mismatch with 400 if callers send both.

        Attributes:
            content (str):
            group_id (None | Unset | UUID):
            metadata (BotGroupMessageCreateMetadataType0 | None | Unset):
    """

    content: str
    group_id: None | Unset | UUID = UNSET
    metadata: BotGroupMessageCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_group_message_create_metadata_type_0 import (
            BotGroupMessageCreateMetadataType0,  # noqa: PLC0415
        )

        content = self.content

        group_id: None | str | Unset
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        elif isinstance(self.group_id, UUID):
            group_id = str(self.group_id)
        else:
            group_id = self.group_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BotGroupMessageCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_group_message_create_metadata_type_0 import (
            BotGroupMessageCreateMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        content = d.pop("content")

        def _parse_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                group_id_type_0 = UUID(data)

                return group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        def _parse_metadata(data: object) -> BotGroupMessageCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BotGroupMessageCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotGroupMessageCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        bot_group_message_create = cls(
            content=content,
            group_id=group_id,
            metadata=metadata,
        )

        bot_group_message_create.additional_properties = d
        return bot_group_message_create

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
