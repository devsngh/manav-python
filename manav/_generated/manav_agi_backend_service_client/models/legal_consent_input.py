from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegalConsentInput")


@_attrs_define
class LegalConsentInput:
    """One legal-doc acceptance recorded at signup.

    Frontend sends one of these per document the user agreed to during
    the signup compliance gate (Terms, Privacy, optionally Cookies / DPA).
    The `document_version` is the version string the frontend rendered —
    it comes from the doc's frontmatter via /api/legal/{slug} on the
    marketing site, so we store exactly what the user saw.

        Attributes:
            document_type (str): terms | privacy | dpa | cookies | marketing
            document_version (str):
            accepted (bool | Unset):  Default: True.
    """

    document_type: str
    document_version: str
    accepted: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_type = self.document_type

        document_version = self.document_version

        accepted = self.accepted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_type": document_type,
                "document_version": document_version,
            }
        )
        if accepted is not UNSET:
            field_dict["accepted"] = accepted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_type = d.pop("document_type")

        document_version = d.pop("document_version")

        accepted = d.pop("accepted", UNSET)

        legal_consent_input = cls(
            document_type=document_type,
            document_version=document_version,
            accepted=accepted,
        )

        legal_consent_input.additional_properties = d
        return legal_consent_input

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
