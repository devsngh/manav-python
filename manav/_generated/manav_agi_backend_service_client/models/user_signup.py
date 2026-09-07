from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.legal_consent_input import LegalConsentInput


T = TypeVar("T", bound="UserSignup")


@_attrs_define
class UserSignup:
    """
    Attributes:
        email (str):
        password (str):
        full_name (str):
        org_id (None | Unset | UUID):
        legal_consents (list[LegalConsentInput] | Unset):
        marketing_opt_in (bool | Unset):  Default: False.
    """

    email: str
    password: str
    full_name: str
    org_id: None | Unset | UUID = UNSET
    legal_consents: list[LegalConsentInput] | Unset = UNSET
    marketing_opt_in: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        full_name = self.full_name

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        legal_consents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.legal_consents, Unset):
            legal_consents = []
            for legal_consents_item_data in self.legal_consents:
                legal_consents_item = legal_consents_item_data.to_dict()
                legal_consents.append(legal_consents_item)

        marketing_opt_in = self.marketing_opt_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "password": password,
                "full_name": full_name,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if legal_consents is not UNSET:
            field_dict["legal_consents"] = legal_consents
        if marketing_opt_in is not UNSET:
            field_dict["marketing_opt_in"] = marketing_opt_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.legal_consent_input import LegalConsentInput  # noqa: PLC0415

        d = dict(src_dict)
        email = d.pop("email")

        password = d.pop("password")

        full_name = d.pop("full_name")

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        _legal_consents = d.pop("legal_consents", UNSET)
        legal_consents: list[LegalConsentInput] | Unset = UNSET
        if _legal_consents is not UNSET:
            legal_consents = []
            for legal_consents_item_data in _legal_consents:
                legal_consents_item = LegalConsentInput.from_dict(legal_consents_item_data)

                legal_consents.append(legal_consents_item)

        marketing_opt_in = d.pop("marketing_opt_in", UNSET)

        user_signup = cls(
            email=email,
            password=password,
            full_name=full_name,
            org_id=org_id,
            legal_consents=legal_consents,
            marketing_opt_in=marketing_opt_in,
        )

        user_signup.additional_properties = d
        return user_signup

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
