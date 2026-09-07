from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DelegationRuleResponse")


@_attrs_define
class DelegationRuleResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        delegator_user_id (None | UUID):
        delegator_bot_id (None | UUID):
        delegate_user_id (None | UUID):
        delegate_bot_id (None | UUID):
        resource_type (None | str):
        max_amount (None | str):
        effective_from (datetime.date):
        effective_until (datetime.date):
        is_active (bool):
        reason (None | str):
        created_at (datetime.datetime):
    """

    id: UUID
    org_id: UUID
    delegator_user_id: None | UUID
    delegator_bot_id: None | UUID
    delegate_user_id: None | UUID
    delegate_bot_id: None | UUID
    resource_type: None | str
    max_amount: None | str
    effective_from: datetime.date
    effective_until: datetime.date
    is_active: bool
    reason: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        delegator_user_id: None | str
        if isinstance(self.delegator_user_id, UUID):
            delegator_user_id = str(self.delegator_user_id)
        else:
            delegator_user_id = self.delegator_user_id

        delegator_bot_id: None | str
        if isinstance(self.delegator_bot_id, UUID):
            delegator_bot_id = str(self.delegator_bot_id)
        else:
            delegator_bot_id = self.delegator_bot_id

        delegate_user_id: None | str
        if isinstance(self.delegate_user_id, UUID):
            delegate_user_id = str(self.delegate_user_id)
        else:
            delegate_user_id = self.delegate_user_id

        delegate_bot_id: None | str
        if isinstance(self.delegate_bot_id, UUID):
            delegate_bot_id = str(self.delegate_bot_id)
        else:
            delegate_bot_id = self.delegate_bot_id

        resource_type: None | str
        resource_type = self.resource_type

        max_amount: None | str
        max_amount = self.max_amount

        effective_from = self.effective_from.isoformat()

        effective_until = self.effective_until.isoformat()

        is_active = self.is_active

        reason: None | str
        reason = self.reason

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "delegator_user_id": delegator_user_id,
                "delegator_bot_id": delegator_bot_id,
                "delegate_user_id": delegate_user_id,
                "delegate_bot_id": delegate_bot_id,
                "resource_type": resource_type,
                "max_amount": max_amount,
                "effective_from": effective_from,
                "effective_until": effective_until,
                "is_active": is_active,
                "reason": reason,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        def _parse_delegator_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegator_user_id_type_0 = UUID(data)

                return delegator_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        delegator_user_id = _parse_delegator_user_id(d.pop("delegator_user_id"))

        def _parse_delegator_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegator_bot_id_type_0 = UUID(data)

                return delegator_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        delegator_bot_id = _parse_delegator_bot_id(d.pop("delegator_bot_id"))

        def _parse_delegate_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegate_user_id_type_0 = UUID(data)

                return delegate_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        delegate_user_id = _parse_delegate_user_id(d.pop("delegate_user_id"))

        def _parse_delegate_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegate_bot_id_type_0 = UUID(data)

                return delegate_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        delegate_bot_id = _parse_delegate_bot_id(d.pop("delegate_bot_id"))

        def _parse_resource_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resource_type = _parse_resource_type(d.pop("resource_type"))

        def _parse_max_amount(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        max_amount = _parse_max_amount(d.pop("max_amount"))

        effective_from = datetime.date.fromisoformat(d.pop("effective_from"))

        effective_until = datetime.date.fromisoformat(d.pop("effective_until"))

        is_active = d.pop("is_active")

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(d.pop("reason"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        delegation_rule_response = cls(
            id=id,
            org_id=org_id,
            delegator_user_id=delegator_user_id,
            delegator_bot_id=delegator_bot_id,
            delegate_user_id=delegate_user_id,
            delegate_bot_id=delegate_bot_id,
            resource_type=resource_type,
            max_amount=max_amount,
            effective_from=effective_from,
            effective_until=effective_until,
            is_active=is_active,
            reason=reason,
            created_at=created_at,
        )

        delegation_rule_response.additional_properties = d
        return delegation_rule_response

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
