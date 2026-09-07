from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cabinet_diff_file import CabinetDiffFile
    from ..models.cabinet_diff_response_counts import CabinetDiffResponseCounts


T = TypeVar("T", bound="CabinetDiffResponse")


@_attrs_define
class CabinetDiffResponse:
    """
    Attributes:
        agent_name (str):
        files (list[CabinetDiffFile]):
        counts (CabinetDiffResponseCounts):
        role_stem (None | str | Unset):
    """

    agent_name: str
    files: list[CabinetDiffFile]
    counts: CabinetDiffResponseCounts
    role_stem: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_name = self.agent_name

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        counts = self.counts.to_dict()

        role_stem: None | str | Unset
        if isinstance(self.role_stem, Unset):
            role_stem = UNSET
        else:
            role_stem = self.role_stem

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_name": agent_name,
                "files": files,
                "counts": counts,
            }
        )
        if role_stem is not UNSET:
            field_dict["role_stem"] = role_stem

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cabinet_diff_file import CabinetDiffFile  # noqa: PLC0415
        from ..models.cabinet_diff_response_counts import CabinetDiffResponseCounts  # noqa: PLC0415

        d = dict(src_dict)
        agent_name = d.pop("agent_name")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = CabinetDiffFile.from_dict(files_item_data)

            files.append(files_item)

        counts = CabinetDiffResponseCounts.from_dict(d.pop("counts"))

        def _parse_role_stem(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_stem = _parse_role_stem(d.pop("role_stem", UNSET))

        cabinet_diff_response = cls(
            agent_name=agent_name,
            files=files,
            counts=counts,
            role_stem=role_stem,
        )

        cabinet_diff_response.additional_properties = d
        return cabinet_diff_response

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
