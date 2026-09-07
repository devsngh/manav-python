from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.migrate_response_results_item import MigrateResponseResultsItem


T = TypeVar("T", bound="MigrateResponse")


@_attrs_define
class MigrateResponse:
    """
    Attributes:
        success (bool):
        results (list[MigrateResponseResultsItem]):
        message (str):
    """

    success: bool
    results: list[MigrateResponseResultsItem]
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "results": results,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migrate_response_results_item import MigrateResponseResultsItem  # noqa: PLC0415

        d = dict(src_dict)
        success = d.pop("success")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = MigrateResponseResultsItem.from_dict(results_item_data)

            results.append(results_item)

        message = d.pop("message")

        migrate_response = cls(
            success=success,
            results=results,
            message=message,
        )

        migrate_response.additional_properties = d
        return migrate_response

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
