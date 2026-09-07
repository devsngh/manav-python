from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hil_event_status import HILEventStatus
from ..models.timeout_policy import TimeoutPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hil_event_response_decision_args_type_0 import HILEventResponseDecisionArgsType0
    from ..models.hil_event_response_interrupt_data import HILEventResponseInterruptData
    from ..models.hil_event_response_tool_args import HILEventResponseToolArgs


T = TypeVar("T", bound="HILEventResponse")


@_attrs_define
class HILEventResponse:
    """
    Attributes:
        id (UUID):
        thread_id (UUID):
        user_id (UUID):
        org_id (None | UUID):
        tool_name (str):
        tool_args (HILEventResponseToolArgs):
        interrupt_data (HILEventResponseInterruptData):
        review_message (None | str):
        allowed_decisions (list[str]):
        status (HILEventStatus): HIL Event lifecycle status.
        decision (None | str):
        decision_args (HILEventResponseDecisionArgsType0 | None):
        decision_note (None | str):
        decided_by (None | UUID):
        decided_at (datetime.datetime | None):
        created_at (datetime.datetime):
        target_reviewer_ids (list[str] | Unset):
        bot_id (None | Unset | UUID):
        bot_name (None | str | Unset):
        parent_hil_id (None | Unset | UUID):
        escalated_at (datetime.datetime | None | Unset):
        escalated_by (None | Unset | UUID):
        timeout_policy (None | TimeoutPolicy | Unset):
        timeout_at (datetime.datetime | None | Unset):
        timeout_resolved_at (datetime.datetime | None | Unset):
    """

    id: UUID
    thread_id: UUID
    user_id: UUID
    org_id: None | UUID
    tool_name: str
    tool_args: HILEventResponseToolArgs
    interrupt_data: HILEventResponseInterruptData
    review_message: None | str
    allowed_decisions: list[str]
    status: HILEventStatus
    decision: None | str
    decision_args: HILEventResponseDecisionArgsType0 | None
    decision_note: None | str
    decided_by: None | UUID
    decided_at: datetime.datetime | None
    created_at: datetime.datetime
    target_reviewer_ids: list[str] | Unset = UNSET
    bot_id: None | Unset | UUID = UNSET
    bot_name: None | str | Unset = UNSET
    parent_hil_id: None | Unset | UUID = UNSET
    escalated_at: datetime.datetime | None | Unset = UNSET
    escalated_by: None | Unset | UUID = UNSET
    timeout_policy: None | TimeoutPolicy | Unset = UNSET
    timeout_at: datetime.datetime | None | Unset = UNSET
    timeout_resolved_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hil_event_response_decision_args_type_0 import HILEventResponseDecisionArgsType0  # noqa: PLC0415

        id = str(self.id)

        thread_id = str(self.thread_id)

        user_id = str(self.user_id)

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        tool_name = self.tool_name

        tool_args = self.tool_args.to_dict()

        interrupt_data = self.interrupt_data.to_dict()

        review_message: None | str
        review_message = self.review_message

        allowed_decisions = self.allowed_decisions

        status = self.status.value

        decision: None | str
        decision = self.decision

        decision_args: dict[str, Any] | None
        if isinstance(self.decision_args, HILEventResponseDecisionArgsType0):
            decision_args = self.decision_args.to_dict()
        else:
            decision_args = self.decision_args

        decision_note: None | str
        decision_note = self.decision_note

        decided_by: None | str
        if isinstance(self.decided_by, UUID):
            decided_by = str(self.decided_by)
        else:
            decided_by = self.decided_by

        decided_at: None | str
        if isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        created_at = self.created_at.isoformat()

        target_reviewer_ids: list[str] | Unset = UNSET
        if not isinstance(self.target_reviewer_ids, Unset):
            target_reviewer_ids = self.target_reviewer_ids

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        parent_hil_id: None | str | Unset
        if isinstance(self.parent_hil_id, Unset):
            parent_hil_id = UNSET
        elif isinstance(self.parent_hil_id, UUID):
            parent_hil_id = str(self.parent_hil_id)
        else:
            parent_hil_id = self.parent_hil_id

        escalated_at: None | str | Unset
        if isinstance(self.escalated_at, Unset):
            escalated_at = UNSET
        elif isinstance(self.escalated_at, datetime.datetime):
            escalated_at = self.escalated_at.isoformat()
        else:
            escalated_at = self.escalated_at

        escalated_by: None | str | Unset
        if isinstance(self.escalated_by, Unset):
            escalated_by = UNSET
        elif isinstance(self.escalated_by, UUID):
            escalated_by = str(self.escalated_by)
        else:
            escalated_by = self.escalated_by

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

        timeout_resolved_at: None | str | Unset
        if isinstance(self.timeout_resolved_at, Unset):
            timeout_resolved_at = UNSET
        elif isinstance(self.timeout_resolved_at, datetime.datetime):
            timeout_resolved_at = self.timeout_resolved_at.isoformat()
        else:
            timeout_resolved_at = self.timeout_resolved_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "thread_id": thread_id,
                "user_id": user_id,
                "org_id": org_id,
                "tool_name": tool_name,
                "tool_args": tool_args,
                "interrupt_data": interrupt_data,
                "review_message": review_message,
                "allowed_decisions": allowed_decisions,
                "status": status,
                "decision": decision,
                "decision_args": decision_args,
                "decision_note": decision_note,
                "decided_by": decided_by,
                "decided_at": decided_at,
                "created_at": created_at,
            }
        )
        if target_reviewer_ids is not UNSET:
            field_dict["target_reviewer_ids"] = target_reviewer_ids
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if parent_hil_id is not UNSET:
            field_dict["parent_hil_id"] = parent_hil_id
        if escalated_at is not UNSET:
            field_dict["escalated_at"] = escalated_at
        if escalated_by is not UNSET:
            field_dict["escalated_by"] = escalated_by
        if timeout_policy is not UNSET:
            field_dict["timeout_policy"] = timeout_policy
        if timeout_at is not UNSET:
            field_dict["timeout_at"] = timeout_at
        if timeout_resolved_at is not UNSET:
            field_dict["timeout_resolved_at"] = timeout_resolved_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hil_event_response_decision_args_type_0 import HILEventResponseDecisionArgsType0  # noqa: PLC0415
        from ..models.hil_event_response_interrupt_data import HILEventResponseInterruptData  # noqa: PLC0415
        from ..models.hil_event_response_tool_args import HILEventResponseToolArgs  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        thread_id = UUID(d.pop("thread_id"))

        user_id = UUID(d.pop("user_id"))

        def _parse_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        org_id = _parse_org_id(d.pop("org_id"))

        tool_name = d.pop("tool_name")

        tool_args = HILEventResponseToolArgs.from_dict(d.pop("tool_args"))

        interrupt_data = HILEventResponseInterruptData.from_dict(d.pop("interrupt_data"))

        def _parse_review_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        review_message = _parse_review_message(d.pop("review_message"))

        allowed_decisions = cast(list[str], d.pop("allowed_decisions"))

        status = HILEventStatus(d.pop("status"))

        def _parse_decision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decision = _parse_decision(d.pop("decision"))

        def _parse_decision_args(data: object) -> HILEventResponseDecisionArgsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                decision_args_type_0 = HILEventResponseDecisionArgsType0.from_dict(data)

                return decision_args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HILEventResponseDecisionArgsType0 | None, data)

        decision_args = _parse_decision_args(d.pop("decision_args"))

        def _parse_decision_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decision_note = _parse_decision_note(d.pop("decision_note"))

        def _parse_decided_by(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_by_type_0 = UUID(data)

                return decided_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        decided_by = _parse_decided_by(d.pop("decided_by"))

        def _parse_decided_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = datetime.datetime.fromisoformat(data)

                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        decided_at = _parse_decided_at(d.pop("decided_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        target_reviewer_ids = cast(list[str], d.pop("target_reviewer_ids", UNSET))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        def _parse_parent_hil_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_hil_id_type_0 = UUID(data)

                return parent_hil_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_hil_id = _parse_parent_hil_id(d.pop("parent_hil_id", UNSET))

        def _parse_escalated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                escalated_at_type_0 = datetime.datetime.fromisoformat(data)

                return escalated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        escalated_at = _parse_escalated_at(d.pop("escalated_at", UNSET))

        def _parse_escalated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                escalated_by_type_0 = UUID(data)

                return escalated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        escalated_by = _parse_escalated_by(d.pop("escalated_by", UNSET))

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

        def _parse_timeout_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timeout_resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return timeout_resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timeout_resolved_at = _parse_timeout_resolved_at(d.pop("timeout_resolved_at", UNSET))

        hil_event_response = cls(
            id=id,
            thread_id=thread_id,
            user_id=user_id,
            org_id=org_id,
            tool_name=tool_name,
            tool_args=tool_args,
            interrupt_data=interrupt_data,
            review_message=review_message,
            allowed_decisions=allowed_decisions,
            status=status,
            decision=decision,
            decision_args=decision_args,
            decision_note=decision_note,
            decided_by=decided_by,
            decided_at=decided_at,
            created_at=created_at,
            target_reviewer_ids=target_reviewer_ids,
            bot_id=bot_id,
            bot_name=bot_name,
            parent_hil_id=parent_hil_id,
            escalated_at=escalated_at,
            escalated_by=escalated_by,
            timeout_policy=timeout_policy,
            timeout_at=timeout_at,
            timeout_resolved_at=timeout_resolved_at,
        )

        hil_event_response.additional_properties = d
        return hil_event_response

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
