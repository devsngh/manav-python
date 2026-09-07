from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DependencyResponse")


@_attrs_define
class DependencyResponse:
    """
    Attributes:
        id (UUID):
        task_id (UUID):
        depends_on_task_id (UUID):
        task_title (None | str | Unset):
        task_status (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    task_id: UUID
    depends_on_task_id: UUID
    task_title: None | str | Unset = UNSET
    task_status: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        task_id = str(self.task_id)

        depends_on_task_id = str(self.depends_on_task_id)

        task_title: None | str | Unset
        if isinstance(self.task_title, Unset):
            task_title = UNSET
        else:
            task_title = self.task_title

        task_status: None | str | Unset
        if isinstance(self.task_status, Unset):
            task_status = UNSET
        else:
            task_status = self.task_status

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "task_id": task_id,
                "depends_on_task_id": depends_on_task_id,
            }
        )
        if task_title is not UNSET:
            field_dict["task_title"] = task_title
        if task_status is not UNSET:
            field_dict["task_status"] = task_status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        task_id = UUID(d.pop("task_id"))

        depends_on_task_id = UUID(d.pop("depends_on_task_id"))

        def _parse_task_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_title = _parse_task_title(d.pop("task_title", UNSET))

        def _parse_task_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_status = _parse_task_status(d.pop("task_status", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        dependency_response = cls(
            id=id,
            task_id=task_id,
            depends_on_task_id=depends_on_task_id,
            task_title=task_title,
            task_status=task_status,
            created_at=created_at,
        )

        dependency_response.additional_properties = d
        return dependency_response

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
