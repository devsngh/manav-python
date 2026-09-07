from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hil_rule_status import HILRuleStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HILRuleResponse")


@_attrs_define
class HILRuleResponse:
    """
    Attributes:
        id (UUID):
        rule_name (str):
        description (None | str):
        tool_name (str):
        allowed_decisions (list[str]):
        review_message (None | str):
        status (HILRuleStatus): HIL Rule lifecycle status
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        reviewer_user_ids (list[str] | Unset):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
    """

    id: UUID
    rule_name: str
    description: None | str
    tool_name: str
    allowed_decisions: list[str]
    review_message: None | str
    status: HILRuleStatus
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    reviewer_user_ids: list[str] | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        rule_name = self.rule_name

        description: None | str
        description = self.description

        tool_name = self.tool_name

        allowed_decisions = self.allowed_decisions

        review_message: None | str
        review_message = self.review_message

        status = self.status.value

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        reviewer_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.reviewer_user_ids, Unset):
            reviewer_user_ids = self.reviewer_user_ids

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rule_name": rule_name,
                "description": description,
                "tool_name": tool_name,
                "allowed_decisions": allowed_decisions,
                "review_message": review_message,
                "status": status,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if reviewer_user_ids is not UNSET:
            field_dict["reviewer_user_ids"] = reviewer_user_ids
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        rule_name = d.pop("rule_name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        tool_name = d.pop("tool_name")

        allowed_decisions = cast(list[str], d.pop("allowed_decisions"))

        def _parse_review_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        review_message = _parse_review_message(d.pop("review_message"))

        status = HILRuleStatus(d.pop("status"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        reviewer_user_ids = cast(list[str], d.pop("reviewer_user_ids", UNSET))

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

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        hil_rule_response = cls(
            id=id,
            rule_name=rule_name,
            description=description,
            tool_name=tool_name,
            allowed_decisions=allowed_decisions,
            review_message=review_message,
            status=status,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            reviewer_user_ids=reviewer_user_ids,
            created_by=created_by,
            updated_by=updated_by,
        )

        hil_rule_response.additional_properties = d
        return hil_rule_response

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
