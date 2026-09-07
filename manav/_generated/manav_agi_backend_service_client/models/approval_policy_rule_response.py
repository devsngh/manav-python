from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.approval_policy_rule_response_condition_jsonb_type_0 import (
        ApprovalPolicyRuleResponseConditionJsonbType0,
    )


T = TypeVar("T", bound="ApprovalPolicyRuleResponse")


@_attrs_define
class ApprovalPolicyRuleResponse:
    """
    Attributes:
        id (UUID):
        policy_id (UUID):
        step_order (int):
        condition_jsonb (ApprovalPolicyRuleResponseConditionJsonbType0 | None):
        approver_role (None | str):
        approver_bot_id (None | UUID):
        approver_user_id (None | UUID):
        approver_type (str):
        is_required (bool):
        sla_hours (int | None):
        created_at (datetime.datetime):
    """

    id: UUID
    policy_id: UUID
    step_order: int
    condition_jsonb: ApprovalPolicyRuleResponseConditionJsonbType0 | None
    approver_role: None | str
    approver_bot_id: None | UUID
    approver_user_id: None | UUID
    approver_type: str
    is_required: bool
    sla_hours: int | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_policy_rule_response_condition_jsonb_type_0 import (
            ApprovalPolicyRuleResponseConditionJsonbType0,  # noqa: PLC0415
        )

        id = str(self.id)

        policy_id = str(self.policy_id)

        step_order = self.step_order

        condition_jsonb: dict[str, Any] | None
        if isinstance(self.condition_jsonb, ApprovalPolicyRuleResponseConditionJsonbType0):
            condition_jsonb = self.condition_jsonb.to_dict()
        else:
            condition_jsonb = self.condition_jsonb

        approver_role: None | str
        approver_role = self.approver_role

        approver_bot_id: None | str
        if isinstance(self.approver_bot_id, UUID):
            approver_bot_id = str(self.approver_bot_id)
        else:
            approver_bot_id = self.approver_bot_id

        approver_user_id: None | str
        if isinstance(self.approver_user_id, UUID):
            approver_user_id = str(self.approver_user_id)
        else:
            approver_user_id = self.approver_user_id

        approver_type = self.approver_type

        is_required = self.is_required

        sla_hours: int | None
        sla_hours = self.sla_hours

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "policy_id": policy_id,
                "step_order": step_order,
                "condition_jsonb": condition_jsonb,
                "approver_role": approver_role,
                "approver_bot_id": approver_bot_id,
                "approver_user_id": approver_user_id,
                "approver_type": approver_type,
                "is_required": is_required,
                "sla_hours": sla_hours,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_policy_rule_response_condition_jsonb_type_0 import (
            ApprovalPolicyRuleResponseConditionJsonbType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        policy_id = UUID(d.pop("policy_id"))

        step_order = d.pop("step_order")

        def _parse_condition_jsonb(data: object) -> ApprovalPolicyRuleResponseConditionJsonbType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_jsonb_type_0 = ApprovalPolicyRuleResponseConditionJsonbType0.from_dict(data)

                return condition_jsonb_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalPolicyRuleResponseConditionJsonbType0 | None, data)

        condition_jsonb = _parse_condition_jsonb(d.pop("condition_jsonb"))

        def _parse_approver_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approver_role = _parse_approver_role(d.pop("approver_role"))

        def _parse_approver_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_bot_id_type_0 = UUID(data)

                return approver_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approver_bot_id = _parse_approver_bot_id(d.pop("approver_bot_id"))

        def _parse_approver_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_user_id_type_0 = UUID(data)

                return approver_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approver_user_id = _parse_approver_user_id(d.pop("approver_user_id"))

        approver_type = d.pop("approver_type")

        is_required = d.pop("is_required")

        def _parse_sla_hours(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        sla_hours = _parse_sla_hours(d.pop("sla_hours"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        approval_policy_rule_response = cls(
            id=id,
            policy_id=policy_id,
            step_order=step_order,
            condition_jsonb=condition_jsonb,
            approver_role=approver_role,
            approver_bot_id=approver_bot_id,
            approver_user_id=approver_user_id,
            approver_type=approver_type,
            is_required=is_required,
            sla_hours=sla_hours,
            created_at=created_at,
        )

        approval_policy_rule_response.additional_properties = d
        return approval_policy_rule_response

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
