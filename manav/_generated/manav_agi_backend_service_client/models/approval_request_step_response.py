from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApprovalRequestStepResponse")


@_attrs_define
class ApprovalRequestStepResponse:
    """
    Attributes:
        id (UUID):
        request_id (UUID):
        step_order (int):
        expected_approver_role (None | str):
        expected_approver_bot_id (None | UUID):
        expected_approver_user_id (None | UUID):
        actual_approver_user_id (None | UUID):
        actual_approver_bot_id (None | UUID):
        decision (None | str):
        decision_note (None | str):
        decided_at (datetime.datetime | None):
        sla_due_at (datetime.datetime | None):
        escalated (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    request_id: UUID
    step_order: int
    expected_approver_role: None | str
    expected_approver_bot_id: None | UUID
    expected_approver_user_id: None | UUID
    actual_approver_user_id: None | UUID
    actual_approver_bot_id: None | UUID
    decision: None | str
    decision_note: None | str
    decided_at: datetime.datetime | None
    sla_due_at: datetime.datetime | None
    escalated: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        request_id = str(self.request_id)

        step_order = self.step_order

        expected_approver_role: None | str
        expected_approver_role = self.expected_approver_role

        expected_approver_bot_id: None | str
        if isinstance(self.expected_approver_bot_id, UUID):
            expected_approver_bot_id = str(self.expected_approver_bot_id)
        else:
            expected_approver_bot_id = self.expected_approver_bot_id

        expected_approver_user_id: None | str
        if isinstance(self.expected_approver_user_id, UUID):
            expected_approver_user_id = str(self.expected_approver_user_id)
        else:
            expected_approver_user_id = self.expected_approver_user_id

        actual_approver_user_id: None | str
        if isinstance(self.actual_approver_user_id, UUID):
            actual_approver_user_id = str(self.actual_approver_user_id)
        else:
            actual_approver_user_id = self.actual_approver_user_id

        actual_approver_bot_id: None | str
        if isinstance(self.actual_approver_bot_id, UUID):
            actual_approver_bot_id = str(self.actual_approver_bot_id)
        else:
            actual_approver_bot_id = self.actual_approver_bot_id

        decision: None | str
        decision = self.decision

        decision_note: None | str
        decision_note = self.decision_note

        decided_at: None | str
        if isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        sla_due_at: None | str
        if isinstance(self.sla_due_at, datetime.datetime):
            sla_due_at = self.sla_due_at.isoformat()
        else:
            sla_due_at = self.sla_due_at

        escalated = self.escalated

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "request_id": request_id,
                "step_order": step_order,
                "expected_approver_role": expected_approver_role,
                "expected_approver_bot_id": expected_approver_bot_id,
                "expected_approver_user_id": expected_approver_user_id,
                "actual_approver_user_id": actual_approver_user_id,
                "actual_approver_bot_id": actual_approver_bot_id,
                "decision": decision,
                "decision_note": decision_note,
                "decided_at": decided_at,
                "sla_due_at": sla_due_at,
                "escalated": escalated,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        request_id = UUID(d.pop("request_id"))

        step_order = d.pop("step_order")

        def _parse_expected_approver_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_approver_role = _parse_expected_approver_role(d.pop("expected_approver_role"))

        def _parse_expected_approver_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_approver_bot_id_type_0 = UUID(data)

                return expected_approver_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        expected_approver_bot_id = _parse_expected_approver_bot_id(d.pop("expected_approver_bot_id"))

        def _parse_expected_approver_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expected_approver_user_id_type_0 = UUID(data)

                return expected_approver_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        expected_approver_user_id = _parse_expected_approver_user_id(d.pop("expected_approver_user_id"))

        def _parse_actual_approver_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_approver_user_id_type_0 = UUID(data)

                return actual_approver_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        actual_approver_user_id = _parse_actual_approver_user_id(d.pop("actual_approver_user_id"))

        def _parse_actual_approver_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_approver_bot_id_type_0 = UUID(data)

                return actual_approver_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        actual_approver_bot_id = _parse_actual_approver_bot_id(d.pop("actual_approver_bot_id"))

        def _parse_decision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decision = _parse_decision(d.pop("decision"))

        def _parse_decision_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decision_note = _parse_decision_note(d.pop("decision_note"))

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

        def _parse_sla_due_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sla_due_at_type_0 = datetime.datetime.fromisoformat(data)

                return sla_due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sla_due_at = _parse_sla_due_at(d.pop("sla_due_at"))

        escalated = d.pop("escalated")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        approval_request_step_response = cls(
            id=id,
            request_id=request_id,
            step_order=step_order,
            expected_approver_role=expected_approver_role,
            expected_approver_bot_id=expected_approver_bot_id,
            expected_approver_user_id=expected_approver_user_id,
            actual_approver_user_id=actual_approver_user_id,
            actual_approver_bot_id=actual_approver_bot_id,
            decision=decision,
            decision_note=decision_note,
            decided_at=decided_at,
            sla_due_at=sla_due_at,
            escalated=escalated,
            created_at=created_at,
        )

        approval_request_step_response.additional_properties = d
        return approval_request_step_response

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
