from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CabinetDiffFile")


@_attrs_define
class CabinetDiffFile:
    """One file's state in the diff view.

    Paths are always in the LIVE-store form (e.g. `/agent_knowledge/mission.md`)
    so the diff UI can render every row consistently. `template_bucket` +
    `template_path` point back to the `cabinet_templates` row a live path
    was derived from (NULL when a live file has no matching template — an
    "extra").

        Attributes:
            path (str):
            namespace (str):
            in_template (bool):
            in_live (bool):
            diverges (bool):
            status (str):
            template_bucket (None | str | Unset):
            template_path (None | str | Unset):
    """

    path: str
    namespace: str
    in_template: bool
    in_live: bool
    diverges: bool
    status: str
    template_bucket: None | str | Unset = UNSET
    template_path: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        namespace = self.namespace

        in_template = self.in_template

        in_live = self.in_live

        diverges = self.diverges

        status = self.status

        template_bucket: None | str | Unset
        if isinstance(self.template_bucket, Unset):
            template_bucket = UNSET
        else:
            template_bucket = self.template_bucket

        template_path: None | str | Unset
        if isinstance(self.template_path, Unset):
            template_path = UNSET
        else:
            template_path = self.template_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "namespace": namespace,
                "in_template": in_template,
                "in_live": in_live,
                "diverges": diverges,
                "status": status,
            }
        )
        if template_bucket is not UNSET:
            field_dict["template_bucket"] = template_bucket
        if template_path is not UNSET:
            field_dict["template_path"] = template_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        namespace = d.pop("namespace")

        in_template = d.pop("in_template")

        in_live = d.pop("in_live")

        diverges = d.pop("diverges")

        status = d.pop("status")

        def _parse_template_bucket(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_bucket = _parse_template_bucket(d.pop("template_bucket", UNSET))

        def _parse_template_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_path = _parse_template_path(d.pop("template_path", UNSET))

        cabinet_diff_file = cls(
            path=path,
            namespace=namespace,
            in_template=in_template,
            in_live=in_live,
            diverges=diverges,
            status=status,
            template_bucket=template_bucket,
            template_path=template_path,
        )

        cabinet_diff_file.additional_properties = d
        return cabinet_diff_file

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
