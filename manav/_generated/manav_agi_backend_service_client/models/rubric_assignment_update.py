from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rubric_assignment_update_scope_type_0 import RubricAssignmentUpdateScopeType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="RubricAssignmentUpdate")


@_attrs_define
class RubricAssignmentUpdate:
    """
    Attributes:
        scope (None | RubricAssignmentUpdateScopeType0 | Unset):
        is_active (bool | None | Unset):
        priority (int | None | Unset):
    """

    scope: None | RubricAssignmentUpdateScopeType0 | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        elif isinstance(self.scope, RubricAssignmentUpdateScopeType0):
            scope = self.scope.value
        else:
            scope = self.scope

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        def _parse_scope(data: object) -> None | RubricAssignmentUpdateScopeType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scope_type_0 = RubricAssignmentUpdateScopeType0(data)

                return scope_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RubricAssignmentUpdateScopeType0 | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        rubric_assignment_update = cls(
            scope=scope,
            is_active=is_active,
            priority=priority,
        )

        rubric_assignment_update.additional_properties = d
        return rubric_assignment_update

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
