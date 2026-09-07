from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hil_decision import HILDecision
from ..models.hil_rule_status import HILRuleStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HILRuleUpdate")


@_attrs_define
class HILRuleUpdate:
    """
    Attributes:
        rule_name (None | str | Unset):
        description (None | str | Unset):
        tool_name (None | str | Unset):
        allowed_decisions (list[HILDecision] | None | Unset):
        review_message (None | str | Unset):
        status (HILRuleStatus | None | Unset):
        is_active (bool | None | Unset):
        reviewer_user_ids (list[str] | None | Unset):
    """

    rule_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tool_name: None | str | Unset = UNSET
    allowed_decisions: list[HILDecision] | None | Unset = UNSET
    review_message: None | str | Unset = UNSET
    status: HILRuleStatus | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    reviewer_user_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name: None | str | Unset
        if isinstance(self.rule_name, Unset):
            rule_name = UNSET
        else:
            rule_name = self.rule_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tool_name: None | str | Unset
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        allowed_decisions: list[str] | None | Unset
        if isinstance(self.allowed_decisions, Unset):
            allowed_decisions = UNSET
        elif isinstance(self.allowed_decisions, list):
            allowed_decisions = []
            for allowed_decisions_type_0_item_data in self.allowed_decisions:
                allowed_decisions_type_0_item = allowed_decisions_type_0_item_data.value
                allowed_decisions.append(allowed_decisions_type_0_item)

        else:
            allowed_decisions = self.allowed_decisions

        review_message: None | str | Unset
        if isinstance(self.review_message, Unset):
            review_message = UNSET
        else:
            review_message = self.review_message

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, HILRuleStatus):
            status = self.status.value
        else:
            status = self.status

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        reviewer_user_ids: list[str] | None | Unset
        if isinstance(self.reviewer_user_ids, Unset):
            reviewer_user_ids = UNSET
        elif isinstance(self.reviewer_user_ids, list):
            reviewer_user_ids = self.reviewer_user_ids

        else:
            reviewer_user_ids = self.reviewer_user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_name is not UNSET:
            field_dict["rule_name"] = rule_name
        if description is not UNSET:
            field_dict["description"] = description
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
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

        def _parse_rule_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rule_name = _parse_rule_name(d.pop("rule_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))

        def _parse_allowed_decisions(data: object) -> list[HILDecision] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_decisions_type_0 = []
                _allowed_decisions_type_0 = data
                for allowed_decisions_type_0_item_data in _allowed_decisions_type_0:
                    allowed_decisions_type_0_item = HILDecision(allowed_decisions_type_0_item_data)

                    allowed_decisions_type_0.append(allowed_decisions_type_0_item)

                return allowed_decisions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HILDecision] | None | Unset, data)

        allowed_decisions = _parse_allowed_decisions(d.pop("allowed_decisions", UNSET))

        def _parse_review_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_message = _parse_review_message(d.pop("review_message", UNSET))

        def _parse_status(data: object) -> HILRuleStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = HILRuleStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HILRuleStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_reviewer_user_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reviewer_user_ids_type_0 = cast(list[str], data)

                return reviewer_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        reviewer_user_ids = _parse_reviewer_user_ids(d.pop("reviewer_user_ids", UNSET))

        hil_rule_update = cls(
            rule_name=rule_name,
            description=description,
            tool_name=tool_name,
            allowed_decisions=allowed_decisions,
            review_message=review_message,
            status=status,
            is_active=is_active,
            reviewer_user_ids=reviewer_user_ids,
        )

        hil_rule_update.additional_properties = d
        return hil_rule_update

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
