from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadOrganizationLogoOrgsUploadLogoPost")


@_attrs_define
class BodyUploadOrganizationLogoOrgsUploadLogoPost:
    """
    Attributes:
        file (File):
        folder (str | Unset):  Default: 'organizations/logos'.
    """

    file: File
    folder: str | Unset = "organizations/logos"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        folder = self.folder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.folder, Unset):
            files.append(("folder", (None, str(self.folder).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        folder = d.pop("folder", UNSET)

        body_upload_organization_logo_orgs_upload_logo_post = cls(
            file=file,
            folder=folder,
        )

        body_upload_organization_logo_orgs_upload_logo_post.additional_properties = d
        return body_upload_organization_logo_orgs_upload_logo_post

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
