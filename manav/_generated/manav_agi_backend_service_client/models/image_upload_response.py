from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImageUploadResponse")


@_attrs_define
class ImageUploadResponse:
    """
    Attributes:
        id (UUID):
        image_url (str):
        alt_text (str):
        category (str):
    """

    id: UUID
    image_url: str
    alt_text: str
    category: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        image_url = self.image_url

        alt_text = self.alt_text

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "image_url": image_url,
                "alt_text": alt_text,
                "category": category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        image_url = d.pop("image_url")

        alt_text = d.pop("alt_text")

        category = d.pop("category")

        image_upload_response = cls(
            id=id,
            image_url=image_url,
            alt_text=alt_text,
            category=category,
        )

        image_upload_response.additional_properties = d
        return image_upload_response

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
