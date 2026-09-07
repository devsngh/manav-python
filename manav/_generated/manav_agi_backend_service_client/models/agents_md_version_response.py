from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentsMdVersionResponse")


@_attrs_define
class AgentsMdVersionResponse:
    """
    Attributes:
        id (UUID):
        deepagent_id (UUID):
        version_number (str):
        content (None | str):
        change_summary (None | str):
        created_at (datetime.datetime):
        created_by (None | UUID):
    """

    id: UUID
    deepagent_id: UUID
    version_number: str
    content: None | str
    change_summary: None | str
    created_at: datetime.datetime
    created_by: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deepagent_id = str(self.deepagent_id)

        version_number = self.version_number

        content: None | str
        content = self.content

        change_summary: None | str
        change_summary = self.change_summary

        created_at = self.created_at.isoformat()

        created_by: None | str
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deepagent_id": deepagent_id,
                "version_number": version_number,
                "content": content,
                "change_summary": change_summary,
                "created_at": created_at,
                "created_by": created_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deepagent_id = UUID(d.pop("deepagent_id"))

        version_number = d.pop("version_number")

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        def _parse_change_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        change_summary = _parse_change_summary(d.pop("change_summary"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_created_by(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by = _parse_created_by(d.pop("created_by"))

        agents_md_version_response = cls(
            id=id,
            deepagent_id=deepagent_id,
            version_number=version_number,
            content=content,
            change_summary=change_summary,
            created_at=created_at,
            created_by=created_by,
        )

        agents_md_version_response.additional_properties = d
        return agents_md_version_response

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
