from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignContractRequest")


@_attrs_define
class SignContractRequest:
    """
    Attributes:
        signed_at (datetime.datetime | None | Unset):
        signed_document_asset_id (None | Unset | UUID):
    """

    signed_at: datetime.datetime | None | Unset = UNSET
    signed_document_asset_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signed_at: None | str | Unset
        if isinstance(self.signed_at, Unset):
            signed_at = UNSET
        elif isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        signed_document_asset_id: None | str | Unset
        if isinstance(self.signed_document_asset_id, Unset):
            signed_document_asset_id = UNSET
        elif isinstance(self.signed_document_asset_id, UUID):
            signed_document_asset_id = str(self.signed_document_asset_id)
        else:
            signed_document_asset_id = self.signed_document_asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signed_at is not UNSET:
            field_dict["signed_at"] = signed_at
        if signed_document_asset_id is not UNSET:
            field_dict["signed_document_asset_id"] = signed_document_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_signed_document_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_document_asset_id_type_0 = UUID(data)

                return signed_document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        signed_document_asset_id = _parse_signed_document_asset_id(d.pop("signed_document_asset_id", UNSET))

        sign_contract_request = cls(
            signed_at=signed_at,
            signed_document_asset_id=signed_document_asset_id,
        )

        sign_contract_request.additional_properties = d
        return sign_contract_request

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
