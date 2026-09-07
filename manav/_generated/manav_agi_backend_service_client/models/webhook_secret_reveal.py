from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookSecretReveal")


@_attrs_define
class WebhookSecretReveal:
    """Returned ONCE on creation/rotation; never queryable after.

    Attributes:
        id (UUID):
        webhook_url (str):
        secret_plaintext (str):
        secret_algorithm (str):
        signature_header_name (str):
        expires_warning (str | Unset):  Default: 'Store this secret securely. It is shown ONCE and cannot be retrieved
            again. To get a new secret, rotate the webhook.'.
    """

    id: UUID
    webhook_url: str
    secret_plaintext: str
    secret_algorithm: str
    signature_header_name: str
    expires_warning: str | Unset = (
        "Store this secret securely. It is shown ONCE and cannot be retrieved again. To get a new secret, rotate the webhook."
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        webhook_url = self.webhook_url

        secret_plaintext = self.secret_plaintext

        secret_algorithm = self.secret_algorithm

        signature_header_name = self.signature_header_name

        expires_warning = self.expires_warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "webhook_url": webhook_url,
                "secret_plaintext": secret_plaintext,
                "secret_algorithm": secret_algorithm,
                "signature_header_name": signature_header_name,
            }
        )
        if expires_warning is not UNSET:
            field_dict["expires_warning"] = expires_warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        webhook_url = d.pop("webhook_url")

        secret_plaintext = d.pop("secret_plaintext")

        secret_algorithm = d.pop("secret_algorithm")

        signature_header_name = d.pop("signature_header_name")

        expires_warning = d.pop("expires_warning", UNSET)

        webhook_secret_reveal = cls(
            id=id,
            webhook_url=webhook_url,
            secret_plaintext=secret_plaintext,
            secret_algorithm=secret_algorithm,
            signature_header_name=signature_header_name,
            expires_warning=expires_warning,
        )

        webhook_secret_reveal.additional_properties = d
        return webhook_secret_reveal

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
