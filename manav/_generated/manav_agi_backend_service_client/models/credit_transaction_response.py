from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credit_transaction_type import CreditTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreditTransactionResponse")


@_attrs_define
class CreditTransactionResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        type_ (CreditTransactionType):
        amount (int):
        balance_after (int):
        description (None | str | Unset):
        reference_type (None | str | Unset):
        reference_id (None | Unset | UUID):
        stripe_payment_intent_id (None | str | Unset):
        user_id (None | Unset | UUID):
        created_at (datetime.datetime | None | Unset):
    """

    id: UUID
    org_id: UUID
    type_: CreditTransactionType
    amount: int
    balance_after: int
    description: None | str | Unset = UNSET
    reference_type: None | str | Unset = UNSET
    reference_id: None | Unset | UUID = UNSET
    stripe_payment_intent_id: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        type_ = self.type_.value

        amount = self.amount

        balance_after = self.balance_after

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        reference_type: None | str | Unset
        if isinstance(self.reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = self.reference_type

        reference_id: None | str | Unset
        if isinstance(self.reference_id, Unset):
            reference_id = UNSET
        elif isinstance(self.reference_id, UUID):
            reference_id = str(self.reference_id)
        else:
            reference_id = self.reference_id

        stripe_payment_intent_id: None | str | Unset
        if isinstance(self.stripe_payment_intent_id, Unset):
            stripe_payment_intent_id = UNSET
        else:
            stripe_payment_intent_id = self.stripe_payment_intent_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "type": type_,
                "amount": amount,
                "balance_after": balance_after,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if reference_type is not UNSET:
            field_dict["reference_type"] = reference_type
        if reference_id is not UNSET:
            field_dict["reference_id"] = reference_id
        if stripe_payment_intent_id is not UNSET:
            field_dict["stripe_payment_intent_id"] = stripe_payment_intent_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        type_ = CreditTransactionType(d.pop("type"))

        amount = d.pop("amount")

        balance_after = d.pop("balance_after")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_reference_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_type = _parse_reference_type(d.pop("reference_type", UNSET))

        def _parse_reference_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_id_type_0 = UUID(data)

                return reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reference_id = _parse_reference_id(d.pop("reference_id", UNSET))

        def _parse_stripe_payment_intent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_payment_intent_id = _parse_stripe_payment_intent_id(d.pop("stripe_payment_intent_id", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        credit_transaction_response = cls(
            id=id,
            org_id=org_id,
            type_=type_,
            amount=amount,
            balance_after=balance_after,
            description=description,
            reference_type=reference_type,
            reference_id=reference_id,
            stripe_payment_intent_id=stripe_payment_intent_id,
            user_id=user_id,
            created_at=created_at,
        )

        credit_transaction_response.additional_properties = d
        return credit_transaction_response

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
