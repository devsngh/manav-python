from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CabinetSyncResponse")


@_attrs_define
class CabinetSyncResponse:
    """
    Attributes:
        bot_name (str):
        docs_ingested (int):
        message (str):
        docs_skipped (int | Unset):  Default: 0.
        errors (int | Unset):  Default: 0.
    """

    bot_name: str
    docs_ingested: int
    message: str
    docs_skipped: int | Unset = 0
    errors: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_name = self.bot_name

        docs_ingested = self.docs_ingested

        message = self.message

        docs_skipped = self.docs_skipped

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_name": bot_name,
                "docs_ingested": docs_ingested,
                "message": message,
            }
        )
        if docs_skipped is not UNSET:
            field_dict["docs_skipped"] = docs_skipped
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_name = d.pop("bot_name")

        docs_ingested = d.pop("docs_ingested")

        message = d.pop("message")

        docs_skipped = d.pop("docs_skipped", UNSET)

        errors = d.pop("errors", UNSET)

        cabinet_sync_response = cls(
            bot_name=bot_name,
            docs_ingested=docs_ingested,
            message=message,
            docs_skipped=docs_skipped,
            errors=errors,
        )

        cabinet_sync_response.additional_properties = d
        return cabinet_sync_response

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
