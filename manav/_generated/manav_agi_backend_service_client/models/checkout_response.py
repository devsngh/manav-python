from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckoutResponse")


@_attrs_define
class CheckoutResponse:
    """
    Attributes:
        checkout_url (None | str | Unset):
        provisioned_free (list[UUID] | Unset):
    """

    checkout_url: None | str | Unset = UNSET
    provisioned_free: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkout_url: None | str | Unset
        if isinstance(self.checkout_url, Unset):
            checkout_url = UNSET
        else:
            checkout_url = self.checkout_url

        provisioned_free: list[str] | Unset = UNSET
        if not isinstance(self.provisioned_free, Unset):
            provisioned_free = []
            for provisioned_free_item_data in self.provisioned_free:
                provisioned_free_item = str(provisioned_free_item_data)
                provisioned_free.append(provisioned_free_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checkout_url is not UNSET:
            field_dict["checkout_url"] = checkout_url
        if provisioned_free is not UNSET:
            field_dict["provisioned_free"] = provisioned_free

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_checkout_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkout_url = _parse_checkout_url(d.pop("checkout_url", UNSET))

        _provisioned_free = d.pop("provisioned_free", UNSET)
        provisioned_free: list[UUID] | Unset = UNSET
        if _provisioned_free is not UNSET:
            provisioned_free = []
            for provisioned_free_item_data in _provisioned_free:
                provisioned_free_item = UUID(provisioned_free_item_data)

                provisioned_free.append(provisioned_free_item)

        checkout_response = cls(
            checkout_url=checkout_url,
            provisioned_free=provisioned_free,
        )

        checkout_response.additional_properties = d
        return checkout_response

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
