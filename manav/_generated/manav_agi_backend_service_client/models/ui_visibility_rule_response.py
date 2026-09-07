from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UIVisibilityRuleResponse")


@_attrs_define
class UIVisibilityRuleResponse:
    """
    Attributes:
        id (UUID):
        element_id (UUID):
        rule_type (str):
        target_id (str):
        is_visible (bool):
        priority (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        element_key (str | Unset):  Default: ''.
        created_by (None | Unset | UUID):
    """

    id: UUID
    element_id: UUID
    rule_type: str
    target_id: str
    is_visible: bool
    priority: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    element_key: str | Unset = ""
    created_by: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        element_id = str(self.element_id)

        rule_type = self.rule_type

        target_id = self.target_id

        is_visible = self.is_visible

        priority = self.priority

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        element_key = self.element_key

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "element_id": element_id,
                "rule_type": rule_type,
                "target_id": target_id,
                "is_visible": is_visible,
                "priority": priority,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if element_key is not UNSET:
            field_dict["element_key"] = element_key
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        element_id = UUID(d.pop("element_id"))

        rule_type = d.pop("rule_type")

        target_id = d.pop("target_id")

        is_visible = d.pop("is_visible")

        priority = d.pop("priority")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        element_key = d.pop("element_key", UNSET)

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        ui_visibility_rule_response = cls(
            id=id,
            element_id=element_id,
            rule_type=rule_type,
            target_id=target_id,
            is_visible=is_visible,
            priority=priority,
            created_at=created_at,
            updated_at=updated_at,
            element_key=element_key,
            created_by=created_by,
        )

        ui_visibility_rule_response.additional_properties = d
        return ui_visibility_rule_response

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
