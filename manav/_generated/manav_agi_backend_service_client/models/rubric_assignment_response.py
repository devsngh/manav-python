from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rubric_assignment_response_scope import RubricAssignmentResponseScope

T = TypeVar("T", bound="RubricAssignmentResponse")


@_attrs_define
class RubricAssignmentResponse:
    """
    Attributes:
        id (UUID):
        rubric_id (UUID):
        agent_id (UUID):
        scope (RubricAssignmentResponseScope):
        is_active (bool):
        priority (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    rubric_id: UUID
    agent_id: UUID
    scope: RubricAssignmentResponseScope
    is_active: bool
    priority: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        rubric_id = str(self.rubric_id)

        agent_id = str(self.agent_id)

        scope = self.scope.value

        is_active = self.is_active

        priority = self.priority

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rubric_id": rubric_id,
                "agent_id": agent_id,
                "scope": scope,
                "is_active": is_active,
                "priority": priority,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        rubric_id = UUID(d.pop("rubric_id"))

        agent_id = UUID(d.pop("agent_id"))

        scope = RubricAssignmentResponseScope(d.pop("scope"))

        is_active = d.pop("is_active")

        priority = d.pop("priority")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        rubric_assignment_response = cls(
            id=id,
            rubric_id=rubric_id,
            agent_id=agent_id,
            scope=scope,
            is_active=is_active,
            priority=priority,
            created_at=created_at,
            updated_at=updated_at,
        )

        rubric_assignment_response.additional_properties = d
        return rubric_assignment_response

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
