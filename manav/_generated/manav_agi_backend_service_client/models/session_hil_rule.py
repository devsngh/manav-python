from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionHILRule")


@_attrs_define
class SessionHILRule:
    """A Human-in-the-Loop rule enforced in this session

    Attributes:
        id (str):
        rule_name (str):
        tool_name (str):
        allowed_decisions (list[str]):
        review_message (None | str | Unset):
    """

    id: str
    rule_name: str
    tool_name: str
    allowed_decisions: list[str]
    review_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rule_name = self.rule_name

        tool_name = self.tool_name

        allowed_decisions = self.allowed_decisions

        review_message: None | str | Unset
        if isinstance(self.review_message, Unset):
            review_message = UNSET
        else:
            review_message = self.review_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "rule_name": rule_name,
                "tool_name": tool_name,
                "allowed_decisions": allowed_decisions,
            }
        )
        if review_message is not UNSET:
            field_dict["review_message"] = review_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        rule_name = d.pop("rule_name")

        tool_name = d.pop("tool_name")

        allowed_decisions = cast(list[str], d.pop("allowed_decisions"))

        def _parse_review_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_message = _parse_review_message(d.pop("review_message", UNSET))

        session_hil_rule = cls(
            id=id,
            rule_name=rule_name,
            tool_name=tool_name,
            allowed_decisions=allowed_decisions,
            review_message=review_message,
        )

        session_hil_rule.additional_properties = d
        return session_hil_rule

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
