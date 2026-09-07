from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.life_cabinet_preview_files import LifeCabinetPreviewFiles


T = TypeVar("T", bound="LifeCabinetPreview")


@_attrs_define
class LifeCabinetPreview:
    """Stub for Phase 4-5. Returns whatever life cabinet content is
    already in the registry; empty dict if cabinet files haven't been
    authored yet.

        Attributes:
            agent_name (str):
            files (LifeCabinetPreviewFiles | Unset): Map of cabinet file slug → its YAML body (None if missing)
    """

    agent_name: str
    files: LifeCabinetPreviewFiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_name = self.agent_name

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_name": agent_name,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.life_cabinet_preview_files import LifeCabinetPreviewFiles  # noqa: PLC0415

        d = dict(src_dict)
        agent_name = d.pop("agent_name")

        _files = d.pop("files", UNSET)
        files: LifeCabinetPreviewFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = LifeCabinetPreviewFiles.from_dict(_files)

        life_cabinet_preview = cls(
            agent_name=agent_name,
            files=files,
        )

        life_cabinet_preview.additional_properties = d
        return life_cabinet_preview

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
