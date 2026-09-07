from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssetTagResponse")


@_attrs_define
class AssetTagResponse:
    """
    Attributes:
        id (UUID):
        asset_id (UUID):
        tag_key (str):
        tag_value (str):
        tagged_at (datetime.datetime):
        tagged_by_bot_id (None | UUID):
    """

    id: UUID
    asset_id: UUID
    tag_key: str
    tag_value: str
    tagged_at: datetime.datetime
    tagged_by_bot_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        asset_id = str(self.asset_id)

        tag_key = self.tag_key

        tag_value = self.tag_value

        tagged_at = self.tagged_at.isoformat()

        tagged_by_bot_id: None | str
        if isinstance(self.tagged_by_bot_id, UUID):
            tagged_by_bot_id = str(self.tagged_by_bot_id)
        else:
            tagged_by_bot_id = self.tagged_by_bot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "asset_id": asset_id,
                "tag_key": tag_key,
                "tag_value": tag_value,
                "tagged_at": tagged_at,
                "tagged_by_bot_id": tagged_by_bot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        asset_id = UUID(d.pop("asset_id"))

        tag_key = d.pop("tag_key")

        tag_value = d.pop("tag_value")

        tagged_at = datetime.datetime.fromisoformat(d.pop("tagged_at"))

        def _parse_tagged_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tagged_by_bot_id_type_0 = UUID(data)

                return tagged_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        tagged_by_bot_id = _parse_tagged_by_bot_id(d.pop("tagged_by_bot_id"))

        asset_tag_response = cls(
            id=id,
            asset_id=asset_id,
            tag_key=tag_key,
            tag_value=tag_value,
            tagged_at=tagged_at,
            tagged_by_bot_id=tagged_by_bot_id,
        )

        asset_tag_response.additional_properties = d
        return asset_tag_response

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
