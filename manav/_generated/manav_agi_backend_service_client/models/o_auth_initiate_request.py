from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OAuthInitiateRequest")


@_attrs_define
class OAuthInitiateRequest:
    """
    Attributes:
        datasource_id (UUID):
        redirect_uri (str):
    """

    datasource_id: UUID
    redirect_uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource_id = str(self.datasource_id)

        redirect_uri = self.redirect_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasource_id": datasource_id,
                "redirect_uri": redirect_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datasource_id = UUID(d.pop("datasource_id"))

        redirect_uri = d.pop("redirect_uri")

        o_auth_initiate_request = cls(
            datasource_id=datasource_id,
            redirect_uri=redirect_uri,
        )

        o_auth_initiate_request.additional_properties = d
        return o_auth_initiate_request

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
