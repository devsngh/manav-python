from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hil_decision import HILDecision
from ..models.hil_rule_status import HILRuleStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HILRuleCreate")


@_attrs_define
class HILRuleCreate:
    """
    Attributes:
        rule_name (str):
        tool_name (str):
        description (None | str | Unset):
        allowed_decisions (list[HILDecision] | Unset):
        review_message (None | str | Unset):
        status (HILRuleStatus | Unset): HIL Rule lifecycle status Default: HILRuleStatus.DRAFT.
        is_active (bool | Unset):  Default: True.
        reviewer_user_ids (list[str] | Unset):
    """

    rule_name: str
    tool_name: str
    description: None | str | Unset = UNSET
    allowed_decisions: list[HILDecision] | Unset = UNSET
    review_message: None | str | Unset = UNSET
    status: HILRuleStatus | Unset = HILRuleStatus.DRAFT
    is_active: bool | Unset = True
    reviewer_user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name = self.rule_name

        tool_name = self.tool_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        allowed_decisions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_decisions, Unset):
            allowed_decisions = []
            for allowed_decisions_item_data in self.allowed_decisions:
                allowed_decisions_item = allowed_decisions_item_data.value
                allowed_decisions.append(allowed_decisions_item)

        review_message: None | str | Unset
        if isinstance(self.review_message, Unset):
            review_message = UNSET
        else:
            review_message = self.review_message

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_active = self.is_active

        reviewer_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.reviewer_user_ids, Unset):
            reviewer_user_ids = self.reviewer_user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_name": rule_name,
                "tool_name": tool_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if allowed_decisions is not UNSET:
            field_dict["allowed_decisions"] = allowed_decisions
        if review_message is not UNSET:
            field_dict["review_message"] = review_message
        if status is not UNSET:
            field_dict["status"] = status
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if reviewer_user_ids is not UNSET:
            field_dict["reviewer_user_ids"] = reviewer_user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_name = d.pop("rule_name")

        tool_name = d.pop("tool_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _allowed_decisions = d.pop("allowed_decisions", UNSET)
        allowed_decisions: list[HILDecision] | Unset = UNSET
        if _allowed_decisions is not UNSET:
            allowed_decisions = []
            for allowed_decisions_item_data in _allowed_decisions:
                allowed_decisions_item = HILDecision(allowed_decisions_item_data)

                allowed_decisions.append(allowed_decisions_item)

        def _parse_review_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_message = _parse_review_message(d.pop("review_message", UNSET))

        _status = d.pop("status", UNSET)
        status: HILRuleStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HILRuleStatus(_status)

        is_active = d.pop("is_active", UNSET)

        reviewer_user_ids = cast(list[str], d.pop("reviewer_user_ids", UNSET))

        hil_rule_create = cls(
            rule_name=rule_name,
            tool_name=tool_name,
            description=description,
            allowed_decisions=allowed_decisions,
            review_message=review_message,
            status=status,
            is_active=is_active,
            reviewer_user_ids=reviewer_user_ids,
        )

        hil_rule_create.additional_properties = d
        return hil_rule_create

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
