from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordSubscriptionDocRequest")


@_attrs_define
class RecordSubscriptionDocRequest:
    """
    Attributes:
        subscription_doc_asset_id (UUID):
        signed_at (datetime.datetime | None | Unset):
    """

    subscription_doc_asset_id: UUID
    signed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_doc_asset_id = str(self.subscription_doc_asset_id)

        signed_at: None | str | Unset
        if isinstance(self.signed_at, Unset):
            signed_at = UNSET
        elif isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscription_doc_asset_id": subscription_doc_asset_id,
            }
        )
        if signed_at is not UNSET:
            field_dict["signed_at"] = signed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_doc_asset_id = UUID(d.pop("subscription_doc_asset_id"))

        def _parse_signed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_at_type_0 = datetime.datetime.fromisoformat(data)

                return signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        signed_at = _parse_signed_at(d.pop("signed_at", UNSET))

        record_subscription_doc_request = cls(
            subscription_doc_asset_id=subscription_doc_asset_id,
            signed_at=signed_at,
        )

        record_subscription_doc_request.additional_properties = d
        return record_subscription_doc_request

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
