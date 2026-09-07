from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetireDomainRequest")


@_attrs_define
class RetireDomainRequest:
    """
    Attributes:
        department_id (str):
        reassign_tasks_to (None | str | Unset):
        archive_social (bool | Unset):  Default: True.
    """

    department_id: str
    reassign_tasks_to: None | str | Unset = UNSET
    archive_social: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        department_id = self.department_id

        reassign_tasks_to: None | str | Unset
        if isinstance(self.reassign_tasks_to, Unset):
            reassign_tasks_to = UNSET
        else:
            reassign_tasks_to = self.reassign_tasks_to

        archive_social = self.archive_social

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "department_id": department_id,
            }
        )
        if reassign_tasks_to is not UNSET:
            field_dict["reassign_tasks_to"] = reassign_tasks_to
        if archive_social is not UNSET:
            field_dict["archive_social"] = archive_social

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        department_id = d.pop("department_id")

        def _parse_reassign_tasks_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reassign_tasks_to = _parse_reassign_tasks_to(d.pop("reassign_tasks_to", UNSET))

        archive_social = d.pop("archive_social", UNSET)

        retire_domain_request = cls(
            department_id=department_id,
            reassign_tasks_to=reassign_tasks_to,
            archive_social=archive_social,
        )

        retire_domain_request.additional_properties = d
        return retire_domain_request

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
