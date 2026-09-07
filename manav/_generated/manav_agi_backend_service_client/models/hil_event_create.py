from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timeout_policy import TimeoutPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hil_event_create_interrupt_data import HILEventCreateInterruptData
    from ..models.hil_event_create_tool_args import HILEventCreateToolArgs


T = TypeVar("T", bound="HILEventCreate")


@_attrs_define
class HILEventCreate:
    """
    Attributes:
        thread_id (str):
        user_id (str): User UUID who owns the chat session
        tool_name (str):
        org_id (None | str | Unset):
        tool_args (HILEventCreateToolArgs | Unset):
        interrupt_data (HILEventCreateInterruptData | Unset):
        review_message (None | str | Unset):
        allowed_decisions (list[str] | Unset):
        target_reviewer_ids (list[str] | Unset):
        bot_id (None | str | Unset):
        bot_name (None | str | Unset):
        timeout_policy (None | TimeoutPolicy | Unset):
        timeout_at (datetime.datetime | None | Unset):
    """

    thread_id: str
    user_id: str
    tool_name: str
    org_id: None | str | Unset = UNSET
    tool_args: HILEventCreateToolArgs | Unset = UNSET
    interrupt_data: HILEventCreateInterruptData | Unset = UNSET
    review_message: None | str | Unset = UNSET
    allowed_decisions: list[str] | Unset = UNSET
    target_reviewer_ids: list[str] | Unset = UNSET
    bot_id: None | str | Unset = UNSET
    bot_name: None | str | Unset = UNSET
    timeout_policy: None | TimeoutPolicy | Unset = UNSET
    timeout_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        user_id = self.user_id

        tool_name = self.tool_name

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        else:
            org_id = self.org_id

        tool_args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_args, Unset):
            tool_args = self.tool_args.to_dict()

        interrupt_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interrupt_data, Unset):
            interrupt_data = self.interrupt_data.to_dict()

        review_message: None | str | Unset
        if isinstance(self.review_message, Unset):
            review_message = UNSET
        else:
            review_message = self.review_message

        allowed_decisions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_decisions, Unset):
            allowed_decisions = self.allowed_decisions

        target_reviewer_ids: list[str] | Unset = UNSET
        if not isinstance(self.target_reviewer_ids, Unset):
            target_reviewer_ids = self.target_reviewer_ids

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        timeout_policy: None | str | Unset
        if isinstance(self.timeout_policy, Unset):
            timeout_policy = UNSET
        elif isinstance(self.timeout_policy, TimeoutPolicy):
            timeout_policy = self.timeout_policy.value
        else:
            timeout_policy = self.timeout_policy

        timeout_at: None | str | Unset
        if isinstance(self.timeout_at, Unset):
            timeout_at = UNSET
        elif isinstance(self.timeout_at, datetime.datetime):
            timeout_at = self.timeout_at.isoformat()
        else:
            timeout_at = self.timeout_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_id": thread_id,
                "user_id": user_id,
                "tool_name": tool_name,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if tool_args is not UNSET:
            field_dict["tool_args"] = tool_args
        if interrupt_data is not UNSET:
            field_dict["interrupt_data"] = interrupt_data
        if review_message is not UNSET:
            field_dict["review_message"] = review_message
        if allowed_decisions is not UNSET:
            field_dict["allowed_decisions"] = allowed_decisions
        if target_reviewer_ids is not UNSET:
            field_dict["target_reviewer_ids"] = target_reviewer_ids
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if timeout_policy is not UNSET:
            field_dict["timeout_policy"] = timeout_policy
        if timeout_at is not UNSET:
            field_dict["timeout_at"] = timeout_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hil_event_create_interrupt_data import HILEventCreateInterruptData  # noqa: PLC0415
        from ..models.hil_event_create_tool_args import HILEventCreateToolArgs  # noqa: PLC0415

        d = dict(src_dict)
        thread_id = d.pop("thread_id")

        user_id = d.pop("user_id")

        tool_name = d.pop("tool_name")

        def _parse_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        _tool_args = d.pop("tool_args", UNSET)
        tool_args: HILEventCreateToolArgs | Unset
        if isinstance(_tool_args, Unset):
            tool_args = UNSET
        else:
            tool_args = HILEventCreateToolArgs.from_dict(_tool_args)

        _interrupt_data = d.pop("interrupt_data", UNSET)
        interrupt_data: HILEventCreateInterruptData | Unset
        if isinstance(_interrupt_data, Unset):
            interrupt_data = UNSET
        else:
            interrupt_data = HILEventCreateInterruptData.from_dict(_interrupt_data)

        def _parse_review_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_message = _parse_review_message(d.pop("review_message", UNSET))

        allowed_decisions = cast(list[str], d.pop("allowed_decisions", UNSET))

        target_reviewer_ids = cast(list[str], d.pop("target_reviewer_ids", UNSET))

        def _parse_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        def _parse_timeout_policy(data: object) -> None | TimeoutPolicy | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timeout_policy_type_0 = TimeoutPolicy(data)

                return timeout_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimeoutPolicy | Unset, data)

        timeout_policy = _parse_timeout_policy(d.pop("timeout_policy", UNSET))

        def _parse_timeout_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timeout_at_type_0 = datetime.datetime.fromisoformat(data)

                return timeout_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timeout_at = _parse_timeout_at(d.pop("timeout_at", UNSET))

        hil_event_create = cls(
            thread_id=thread_id,
            user_id=user_id,
            tool_name=tool_name,
            org_id=org_id,
            tool_args=tool_args,
            interrupt_data=interrupt_data,
            review_message=review_message,
            allowed_decisions=allowed_decisions,
            target_reviewer_ids=target_reviewer_ids,
            bot_id=bot_id,
            bot_name=bot_name,
            timeout_policy=timeout_policy,
            timeout_at=timeout_at,
        )

        hil_event_create.additional_properties = d
        return hil_event_create

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
