from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rubric_assignment_create_scope import RubricAssignmentCreateScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="RubricAssignmentCreate")


@_attrs_define
class RubricAssignmentCreate:
    """
    Attributes:
        rubric_id (UUID):
        agent_id (UUID):
        scope (RubricAssignmentCreateScope | Unset):  Default: RubricAssignmentCreateScope.ALL.
        is_active (bool | Unset):  Default: True.
        priority (int | Unset):  Default: 100.
    """

    rubric_id: UUID
    agent_id: UUID
    scope: RubricAssignmentCreateScope | Unset = RubricAssignmentCreateScope.ALL
    is_active: bool | Unset = True
    priority: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rubric_id = str(self.rubric_id)

        agent_id = str(self.agent_id)

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        is_active = self.is_active

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rubric_id": rubric_id,
                "agent_id": agent_id,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rubric_id = UUID(d.pop("rubric_id"))

        agent_id = UUID(d.pop("agent_id"))

        _scope = d.pop("scope", UNSET)
        scope: RubricAssignmentCreateScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RubricAssignmentCreateScope(_scope)

        is_active = d.pop("is_active", UNSET)

        priority = d.pop("priority", UNSET)

        rubric_assignment_create = cls(
            rubric_id=rubric_id,
            agent_id=agent_id,
            scope=scope,
            is_active=is_active,
            priority=priority,
        )

        rubric_assignment_create.additional_properties = d
        return rubric_assignment_create

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
