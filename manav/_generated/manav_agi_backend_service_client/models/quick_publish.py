from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.marketplace_item_type import MarketplaceItemType

T = TypeVar("T", bound="QuickPublish")


@_attrs_define
class QuickPublish:
    """
    Attributes:
        item_type (MarketplaceItemType):
        item_id (UUID):
    """

    item_type: MarketplaceItemType
    item_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_type = self.item_type.value

        item_id = str(self.item_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "item_type": item_type,
                "item_id": item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_type = MarketplaceItemType(d.pop("item_type"))

        item_id = UUID(d.pop("item_id"))

        quick_publish = cls(
            item_type=item_type,
            item_id=item_id,
        )

        quick_publish.additional_properties = d
        return quick_publish

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
