from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignment_target_type import AssignmentTargetType

T = TypeVar("T", bound="DeepAgentAssignResponse")


@_attrs_define
class DeepAgentAssignResponse:
    """
    Attributes:
        id (UUID):
        deepagent_id (UUID):
        target_type (AssignmentTargetType):
        target_id (None | UUID):
        target_label (None | str):
        is_active (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    deepagent_id: UUID
    target_type: AssignmentTargetType
    target_id: None | UUID
    target_label: None | str
    is_active: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        deepagent_id = str(self.deepagent_id)

        target_type = self.target_type.value

        target_id: None | str
        if isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id

        target_label: None | str
        target_label = self.target_label

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "deepagent_id": deepagent_id,
                "target_type": target_type,
                "target_id": target_id,
                "target_label": target_label,
                "is_active": is_active,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        deepagent_id = UUID(d.pop("deepagent_id"))

        target_type = AssignmentTargetType(d.pop("target_type"))

        def _parse_target_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_0 = UUID(data)

                return target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        target_id = _parse_target_id(d.pop("target_id"))

        def _parse_target_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_label = _parse_target_label(d.pop("target_label"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        deep_agent_assign_response = cls(
            id=id,
            deepagent_id=deepagent_id,
            target_type=target_type,
            target_id=target_id,
            target_label=target_label,
            is_active=is_active,
            created_at=created_at,
        )

        deep_agent_assign_response.additional_properties = d
        return deep_agent_assign_response

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
