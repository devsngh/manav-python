from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyAdminUploadImageApiWebsiteAdminImagesPost")


@_attrs_define
class BodyAdminUploadImageApiWebsiteAdminImagesPost:
    """
    Attributes:
        file (File):
        category (str | Unset):  Default: 'general'.
        alt_text (str | Unset):  Default: ''.
    """

    file: File
    category: str | Unset = "general"
    alt_text: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        category = self.category

        alt_text = self.alt_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if alt_text is not UNSET:
            field_dict["alt_text"] = alt_text

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.category, Unset):
            files.append(("category", (None, str(self.category).encode(), "text/plain")))

        if not isinstance(self.alt_text, Unset):
            files.append(("alt_text", (None, str(self.alt_text).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        category = d.pop("category", UNSET)

        alt_text = d.pop("alt_text", UNSET)

        body_admin_upload_image_api_website_admin_images_post = cls(
            file=file,
            category=category,
            alt_text=alt_text,
        )

        body_admin_upload_image_api_website_admin_images_post.additional_properties = d
        return body_admin_upload_image_api_website_admin_images_post

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
