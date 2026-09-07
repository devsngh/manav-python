from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_status import InvoiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvoiceResponse")


@_attrs_define
class InvoiceResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        status (InvoiceStatus):
        amount_cents (int):
        currency (str):
        stripe_invoice_id (None | str | Unset):
        description (None | str | Unset):
        period_start (datetime.datetime | None | Unset):
        period_end (datetime.datetime | None | Unset):
        paid_at (datetime.datetime | None | Unset):
        pdf_url (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    org_id: UUID
    status: InvoiceStatus
    amount_cents: int
    currency: str
    stripe_invoice_id: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    period_start: datetime.datetime | None | Unset = UNSET
    period_end: datetime.datetime | None | Unset = UNSET
    paid_at: datetime.datetime | None | Unset = UNSET
    pdf_url: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        status = self.status.value

        amount_cents = self.amount_cents

        currency = self.currency

        stripe_invoice_id: None | str | Unset
        if isinstance(self.stripe_invoice_id, Unset):
            stripe_invoice_id = UNSET
        else:
            stripe_invoice_id = self.stripe_invoice_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        elif isinstance(self.period_start, datetime.datetime):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: None | str | Unset
        if isinstance(self.period_end, Unset):
            period_end = UNSET
        elif isinstance(self.period_end, datetime.datetime):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        paid_at: None | str | Unset
        if isinstance(self.paid_at, Unset):
            paid_at = UNSET
        elif isinstance(self.paid_at, datetime.datetime):
            paid_at = self.paid_at.isoformat()
        else:
            paid_at = self.paid_at

        pdf_url: None | str | Unset
        if isinstance(self.pdf_url, Unset):
            pdf_url = UNSET
        else:
            pdf_url = self.pdf_url

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "status": status,
                "amount_cents": amount_cents,
                "currency": currency,
            }
        )
        if stripe_invoice_id is not UNSET:
            field_dict["stripe_invoice_id"] = stripe_invoice_id
        if description is not UNSET:
            field_dict["description"] = description
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if pdf_url is not UNSET:
            field_dict["pdf_url"] = pdf_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        status = InvoiceStatus(d.pop("status"))

        amount_cents = d.pop("amount_cents")

        currency = d.pop("currency")

        def _parse_stripe_invoice_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_invoice_id = _parse_stripe_invoice_id(d.pop("stripe_invoice_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = datetime.datetime.fromisoformat(data)

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_start = _parse_period_start(d.pop("period_start", UNSET))

        def _parse_period_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = datetime.datetime.fromisoformat(data)

                return period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_end = _parse_period_end(d.pop("period_end", UNSET))

        def _parse_paid_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_at_type_0 = datetime.datetime.fromisoformat(data)

                return paid_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid_at = _parse_paid_at(d.pop("paid_at", UNSET))

        def _parse_pdf_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdf_url = _parse_pdf_url(d.pop("pdf_url", UNSET))

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

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        invoice_response = cls(
            id=id,
            org_id=org_id,
            status=status,
            amount_cents=amount_cents,
            currency=currency,
            stripe_invoice_id=stripe_invoice_id,
            description=description,
            period_start=period_start,
            period_end=period_end,
            paid_at=paid_at,
            pdf_url=pdf_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        invoice_response.additional_properties = d
        return invoice_response

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
