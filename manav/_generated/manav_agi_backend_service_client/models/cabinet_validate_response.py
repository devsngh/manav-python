from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CabinetValidateResponse")


@_attrs_define
class CabinetValidateResponse:
    """
    Attributes:
        valid (bool):
        yaml_ok (bool):
        body_present (bool):
        placeholders (list[str] | Unset):
        unknown_placeholders (list[str] | Unset):
        errors (list[str] | Unset):
    """

    valid: bool
    yaml_ok: bool
    body_present: bool
    placeholders: list[str] | Unset = UNSET
    unknown_placeholders: list[str] | Unset = UNSET
    errors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        yaml_ok = self.yaml_ok

        body_present = self.body_present

        placeholders: list[str] | Unset = UNSET
        if not isinstance(self.placeholders, Unset):
            placeholders = self.placeholders

        unknown_placeholders: list[str] | Unset = UNSET
        if not isinstance(self.unknown_placeholders, Unset):
            unknown_placeholders = self.unknown_placeholders

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "valid": valid,
                "yaml_ok": yaml_ok,
                "body_present": body_present,
            }
        )
        if placeholders is not UNSET:
            field_dict["placeholders"] = placeholders
        if unknown_placeholders is not UNSET:
            field_dict["unknown_placeholders"] = unknown_placeholders
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        yaml_ok = d.pop("yaml_ok")

        body_present = d.pop("body_present")

        placeholders = cast(list[str], d.pop("placeholders", UNSET))

        unknown_placeholders = cast(list[str], d.pop("unknown_placeholders", UNSET))

        errors = cast(list[str], d.pop("errors", UNSET))

        cabinet_validate_response = cls(
            valid=valid,
            yaml_ok=yaml_ok,
            body_present=body_present,
            placeholders=placeholders,
            unknown_placeholders=unknown_placeholders,
            errors=errors,
        )

        cabinet_validate_response.additional_properties = d
        return cabinet_validate_response

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
