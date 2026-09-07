from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credential_field_definition import CredentialFieldDefinition


T = TypeVar("T", bound="CredentialKeysResponse")


@_attrs_define
class CredentialKeysResponse:
    """
    Attributes:
        datasource_id (str):
        datasource_name (str):
        datasource_ui_name (str):
        connection_template (None | str):
        credential_keys (list[CredentialFieldDefinition]):
    """

    datasource_id: str
    datasource_name: str
    datasource_ui_name: str
    connection_template: None | str
    credential_keys: list[CredentialFieldDefinition]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasource_id = self.datasource_id

        datasource_name = self.datasource_name

        datasource_ui_name = self.datasource_ui_name

        connection_template: None | str
        connection_template = self.connection_template

        credential_keys = []
        for credential_keys_item_data in self.credential_keys:
            credential_keys_item = credential_keys_item_data.to_dict()
            credential_keys.append(credential_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasource_id": datasource_id,
                "datasource_name": datasource_name,
                "datasource_ui_name": datasource_ui_name,
                "connection_template": connection_template,
                "credential_keys": credential_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_field_definition import CredentialFieldDefinition  # noqa: PLC0415

        d = dict(src_dict)
        datasource_id = d.pop("datasource_id")

        datasource_name = d.pop("datasource_name")

        datasource_ui_name = d.pop("datasource_ui_name")

        def _parse_connection_template(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        connection_template = _parse_connection_template(d.pop("connection_template"))

        credential_keys = []
        _credential_keys = d.pop("credential_keys")
        for credential_keys_item_data in _credential_keys:
            credential_keys_item = CredentialFieldDefinition.from_dict(credential_keys_item_data)

            credential_keys.append(credential_keys_item)

        credential_keys_response = cls(
            datasource_id=datasource_id,
            datasource_name=datasource_name,
            datasource_ui_name=datasource_ui_name,
            connection_template=connection_template,
            credential_keys=credential_keys,
        )

        credential_keys_response.additional_properties = d
        return credential_keys_response

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
