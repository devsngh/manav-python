from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RotateCredentialsRequest")


@_attrs_define
class RotateCredentialsRequest:
    """
    Attributes:
        new_oauth_credentials_ref (str):
    """

    new_oauth_credentials_ref: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_oauth_credentials_ref = self.new_oauth_credentials_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new_oauth_credentials_ref": new_oauth_credentials_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_oauth_credentials_ref = d.pop("new_oauth_credentials_ref")

        rotate_credentials_request = cls(
            new_oauth_credentials_ref=new_oauth_credentials_ref,
        )

        rotate_credentials_request.additional_properties = d
        return rotate_credentials_request

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
