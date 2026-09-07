from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetUpdate")


@_attrs_define
class AssetUpdate:
    """
    Attributes:
        asset_role (None | str | Unset):
        mime_type (None | str | Unset):
        file_size_bytes (int | None | Unset):
        dimensions_width (int | None | Unset):
        dimensions_height (int | None | Unset):
        duration_sec (float | None | str | Unset):
        page_count (int | None | Unset):
        version (int | None | Unset):
        status (None | str | Unset):
        visibility (None | str | Unset):
    """

    asset_role: None | str | Unset = UNSET
    mime_type: None | str | Unset = UNSET
    file_size_bytes: int | None | Unset = UNSET
    dimensions_width: int | None | Unset = UNSET
    dimensions_height: int | None | Unset = UNSET
    duration_sec: float | None | str | Unset = UNSET
    page_count: int | None | Unset = UNSET
    version: int | None | Unset = UNSET
    status: None | str | Unset = UNSET
    visibility: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_role: None | str | Unset
        if isinstance(self.asset_role, Unset):
            asset_role = UNSET
        else:
            asset_role = self.asset_role

        mime_type: None | str | Unset
        if isinstance(self.mime_type, Unset):
            mime_type = UNSET
        else:
            mime_type = self.mime_type

        file_size_bytes: int | None | Unset
        if isinstance(self.file_size_bytes, Unset):
            file_size_bytes = UNSET
        else:
            file_size_bytes = self.file_size_bytes

        dimensions_width: int | None | Unset
        if isinstance(self.dimensions_width, Unset):
            dimensions_width = UNSET
        else:
            dimensions_width = self.dimensions_width

        dimensions_height: int | None | Unset
        if isinstance(self.dimensions_height, Unset):
            dimensions_height = UNSET
        else:
            dimensions_height = self.dimensions_height

        duration_sec: float | None | str | Unset
        if isinstance(self.duration_sec, Unset):
            duration_sec = UNSET
        else:
            duration_sec = self.duration_sec

        page_count: int | None | Unset
        if isinstance(self.page_count, Unset):
            page_count = UNSET
        else:
            page_count = self.page_count

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        visibility: None | str | Unset
        if isinstance(self.visibility, Unset):
            visibility = UNSET
        else:
            visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_role is not UNSET:
            field_dict["asset_role"] = asset_role
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if file_size_bytes is not UNSET:
            field_dict["file_size_bytes"] = file_size_bytes
        if dimensions_width is not UNSET:
            field_dict["dimensions_width"] = dimensions_width
        if dimensions_height is not UNSET:
            field_dict["dimensions_height"] = dimensions_height
        if duration_sec is not UNSET:
            field_dict["duration_sec"] = duration_sec
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_asset_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_role = _parse_asset_role(d.pop("asset_role", UNSET))

        def _parse_mime_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mime_type = _parse_mime_type(d.pop("mime_type", UNSET))

        def _parse_file_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_size_bytes = _parse_file_size_bytes(d.pop("file_size_bytes", UNSET))

        def _parse_dimensions_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dimensions_width = _parse_dimensions_width(d.pop("dimensions_width", UNSET))

        def _parse_dimensions_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dimensions_height = _parse_dimensions_height(d.pop("dimensions_height", UNSET))

        def _parse_duration_sec(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        duration_sec = _parse_duration_sec(d.pop("duration_sec", UNSET))

        def _parse_page_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        page_count = _parse_page_count(d.pop("page_count", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_visibility(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visibility = _parse_visibility(d.pop("visibility", UNSET))

        asset_update = cls(
            asset_role=asset_role,
            mime_type=mime_type,
            file_size_bytes=file_size_bytes,
            dimensions_width=dimensions_width,
            dimensions_height=dimensions_height,
            duration_sec=duration_sec,
            page_count=page_count,
            version=version,
            status=status,
            visibility=visibility,
        )

        asset_update.additional_properties = d
        return asset_update

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
