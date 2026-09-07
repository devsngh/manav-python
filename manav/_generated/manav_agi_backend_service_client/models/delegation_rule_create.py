from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DelegationRuleCreate")


@_attrs_define
class DelegationRuleCreate:
    """
    Attributes:
        effective_from (datetime.date):
        effective_until (datetime.date):
        delegator_user_id (None | Unset | UUID):
        delegator_bot_id (None | Unset | UUID):
        delegate_user_id (None | Unset | UUID):
        delegate_bot_id (None | Unset | UUID):
        resource_type (None | str | Unset):
        max_amount (float | None | str | Unset):
        is_active (bool | Unset):  Default: True.
        reason (None | str | Unset):
    """

    effective_from: datetime.date
    effective_until: datetime.date
    delegator_user_id: None | Unset | UUID = UNSET
    delegator_bot_id: None | Unset | UUID = UNSET
    delegate_user_id: None | Unset | UUID = UNSET
    delegate_bot_id: None | Unset | UUID = UNSET
    resource_type: None | str | Unset = UNSET
    max_amount: float | None | str | Unset = UNSET
    is_active: bool | Unset = True
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_from = self.effective_from.isoformat()

        effective_until = self.effective_until.isoformat()

        delegator_user_id: None | str | Unset
        if isinstance(self.delegator_user_id, Unset):
            delegator_user_id = UNSET
        elif isinstance(self.delegator_user_id, UUID):
            delegator_user_id = str(self.delegator_user_id)
        else:
            delegator_user_id = self.delegator_user_id

        delegator_bot_id: None | str | Unset
        if isinstance(self.delegator_bot_id, Unset):
            delegator_bot_id = UNSET
        elif isinstance(self.delegator_bot_id, UUID):
            delegator_bot_id = str(self.delegator_bot_id)
        else:
            delegator_bot_id = self.delegator_bot_id

        delegate_user_id: None | str | Unset
        if isinstance(self.delegate_user_id, Unset):
            delegate_user_id = UNSET
        elif isinstance(self.delegate_user_id, UUID):
            delegate_user_id = str(self.delegate_user_id)
        else:
            delegate_user_id = self.delegate_user_id

        delegate_bot_id: None | str | Unset
        if isinstance(self.delegate_bot_id, Unset):
            delegate_bot_id = UNSET
        elif isinstance(self.delegate_bot_id, UUID):
            delegate_bot_id = str(self.delegate_bot_id)
        else:
            delegate_bot_id = self.delegate_bot_id

        resource_type: None | str | Unset
        if isinstance(self.resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = self.resource_type

        max_amount: float | None | str | Unset
        if isinstance(self.max_amount, Unset):
            max_amount = UNSET
        else:
            max_amount = self.max_amount

        is_active = self.is_active

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_from": effective_from,
                "effective_until": effective_until,
            }
        )
        if delegator_user_id is not UNSET:
            field_dict["delegator_user_id"] = delegator_user_id
        if delegator_bot_id is not UNSET:
            field_dict["delegator_bot_id"] = delegator_bot_id
        if delegate_user_id is not UNSET:
            field_dict["delegate_user_id"] = delegate_user_id
        if delegate_bot_id is not UNSET:
            field_dict["delegate_bot_id"] = delegate_bot_id
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effective_from = datetime.date.fromisoformat(d.pop("effective_from"))

        effective_until = datetime.date.fromisoformat(d.pop("effective_until"))

        def _parse_delegator_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegator_user_id_type_0 = UUID(data)

                return delegator_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delegator_user_id = _parse_delegator_user_id(d.pop("delegator_user_id", UNSET))

        def _parse_delegator_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegator_bot_id_type_0 = UUID(data)

                return delegator_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delegator_bot_id = _parse_delegator_bot_id(d.pop("delegator_bot_id", UNSET))

        def _parse_delegate_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegate_user_id_type_0 = UUID(data)

                return delegate_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delegate_user_id = _parse_delegate_user_id(d.pop("delegate_user_id", UNSET))

        def _parse_delegate_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delegate_bot_id_type_0 = UUID(data)

                return delegate_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        delegate_bot_id = _parse_delegate_bot_id(d.pop("delegate_bot_id", UNSET))

        def _parse_resource_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_type = _parse_resource_type(d.pop("resource_type", UNSET))

        def _parse_max_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        max_amount = _parse_max_amount(d.pop("max_amount", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        delegation_rule_create = cls(
            effective_from=effective_from,
            effective_until=effective_until,
            delegator_user_id=delegator_user_id,
            delegator_bot_id=delegator_bot_id,
            delegate_user_id=delegate_user_id,
            delegate_bot_id=delegate_bot_id,
            resource_type=resource_type,
            max_amount=max_amount,
            is_active=is_active,
            reason=reason,
        )

        delegation_rule_create.additional_properties = d
        return delegation_rule_create

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
