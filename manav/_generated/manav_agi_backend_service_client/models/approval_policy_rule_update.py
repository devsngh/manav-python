from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.approval_policy_rule_update_condition_jsonb_type_0 import ApprovalPolicyRuleUpdateConditionJsonbType0


T = TypeVar("T", bound="ApprovalPolicyRuleUpdate")


@_attrs_define
class ApprovalPolicyRuleUpdate:
    """
    Attributes:
        step_order (int | None | Unset):
        approver_type (None | str | Unset):
        approver_role (None | str | Unset):
        approver_bot_id (None | Unset | UUID):
        approver_user_id (None | Unset | UUID):
        condition_jsonb (ApprovalPolicyRuleUpdateConditionJsonbType0 | None | Unset):
        is_required (bool | None | Unset):
        sla_hours (int | None | Unset):
    """

    step_order: int | None | Unset = UNSET
    approver_type: None | str | Unset = UNSET
    approver_role: None | str | Unset = UNSET
    approver_bot_id: None | Unset | UUID = UNSET
    approver_user_id: None | Unset | UUID = UNSET
    condition_jsonb: ApprovalPolicyRuleUpdateConditionJsonbType0 | None | Unset = UNSET
    is_required: bool | None | Unset = UNSET
    sla_hours: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approval_policy_rule_update_condition_jsonb_type_0 import (
            ApprovalPolicyRuleUpdateConditionJsonbType0,  # noqa: PLC0415
        )

        step_order: int | None | Unset
        if isinstance(self.step_order, Unset):
            step_order = UNSET
        else:
            step_order = self.step_order

        approver_type: None | str | Unset
        if isinstance(self.approver_type, Unset):
            approver_type = UNSET
        else:
            approver_type = self.approver_type

        approver_role: None | str | Unset
        if isinstance(self.approver_role, Unset):
            approver_role = UNSET
        else:
            approver_role = self.approver_role

        approver_bot_id: None | str | Unset
        if isinstance(self.approver_bot_id, Unset):
            approver_bot_id = UNSET
        elif isinstance(self.approver_bot_id, UUID):
            approver_bot_id = str(self.approver_bot_id)
        else:
            approver_bot_id = self.approver_bot_id

        approver_user_id: None | str | Unset
        if isinstance(self.approver_user_id, Unset):
            approver_user_id = UNSET
        elif isinstance(self.approver_user_id, UUID):
            approver_user_id = str(self.approver_user_id)
        else:
            approver_user_id = self.approver_user_id

        condition_jsonb: dict[str, Any] | None | Unset
        if isinstance(self.condition_jsonb, Unset):
            condition_jsonb = UNSET
        elif isinstance(self.condition_jsonb, ApprovalPolicyRuleUpdateConditionJsonbType0):
            condition_jsonb = self.condition_jsonb.to_dict()
        else:
            condition_jsonb = self.condition_jsonb

        is_required: bool | None | Unset
        if isinstance(self.is_required, Unset):
            is_required = UNSET
        else:
            is_required = self.is_required

        sla_hours: int | None | Unset
        if isinstance(self.sla_hours, Unset):
            sla_hours = UNSET
        else:
            sla_hours = self.sla_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step_order is not UNSET:
            field_dict["step_order"] = step_order
        if approver_type is not UNSET:
            field_dict["approver_type"] = approver_type
        if approver_role is not UNSET:
            field_dict["approver_role"] = approver_role
        if approver_bot_id is not UNSET:
            field_dict["approver_bot_id"] = approver_bot_id
        if approver_user_id is not UNSET:
            field_dict["approver_user_id"] = approver_user_id
        if condition_jsonb is not UNSET:
            field_dict["condition_jsonb"] = condition_jsonb
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if sla_hours is not UNSET:
            field_dict["sla_hours"] = sla_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_policy_rule_update_condition_jsonb_type_0 import (
            ApprovalPolicyRuleUpdateConditionJsonbType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_step_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        step_order = _parse_step_order(d.pop("step_order", UNSET))

        def _parse_approver_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approver_type = _parse_approver_type(d.pop("approver_type", UNSET))

        def _parse_approver_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approver_role = _parse_approver_role(d.pop("approver_role", UNSET))

        def _parse_approver_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_bot_id_type_0 = UUID(data)

                return approver_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approver_bot_id = _parse_approver_bot_id(d.pop("approver_bot_id", UNSET))

        def _parse_approver_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_user_id_type_0 = UUID(data)

                return approver_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approver_user_id = _parse_approver_user_id(d.pop("approver_user_id", UNSET))

        def _parse_condition_jsonb(data: object) -> ApprovalPolicyRuleUpdateConditionJsonbType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                condition_jsonb_type_0 = ApprovalPolicyRuleUpdateConditionJsonbType0.from_dict(data)

                return condition_jsonb_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApprovalPolicyRuleUpdateConditionJsonbType0 | None | Unset, data)

        condition_jsonb = _parse_condition_jsonb(d.pop("condition_jsonb", UNSET))

        def _parse_is_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_required = _parse_is_required(d.pop("is_required", UNSET))

        def _parse_sla_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sla_hours = _parse_sla_hours(d.pop("sla_hours", UNSET))

        approval_policy_rule_update = cls(
            step_order=step_order,
            approver_type=approver_type,
            approver_role=approver_role,
            approver_bot_id=approver_bot_id,
            approver_user_id=approver_user_id,
            condition_jsonb=condition_jsonb,
            is_required=is_required,
            sla_hours=sla_hours,
        )

        approval_policy_rule_update.additional_properties = d
        return approval_policy_rule_update

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
