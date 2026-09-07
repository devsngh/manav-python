from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_message_create_metadata_type_0 import BotMessageCreateMetadataType0


T = TypeVar("T", bound="BotMessageCreate")


@_attrs_define
class BotMessageCreate:
    """Schema for sending a bot message

    Attributes:
        conversation_id (UUID):
        content (str):
        metadata (BotMessageCreateMetadataType0 | None | Unset):
    """

    conversation_id: UUID
    content: str
    metadata: BotMessageCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_message_create_metadata_type_0 import BotMessageCreateMetadataType0  # noqa: PLC0415

        conversation_id = str(self.conversation_id)

        content = self.content

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BotMessageCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation_id": conversation_id,
                "content": content,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_message_create_metadata_type_0 import BotMessageCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        conversation_id = UUID(d.pop("conversation_id"))

        content = d.pop("content")

        def _parse_metadata(data: object) -> BotMessageCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BotMessageCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotMessageCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        bot_message_create = cls(
            conversation_id=conversation_id,
            content=content,
            metadata=metadata,
        )

        bot_message_create.additional_properties = d
        return bot_message_create

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
