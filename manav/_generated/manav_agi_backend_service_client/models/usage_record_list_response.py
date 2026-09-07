from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.usage_record_response import UsageRecordResponse


T = TypeVar("T", bound="UsageRecordListResponse")


@_attrs_define
class UsageRecordListResponse:
    """
    Attributes:
        records (list[UsageRecordResponse]):
        total (int):
        page (int):
        page_size (int):
        total_pages (int):
    """

    records: list[UsageRecordResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "records": records,
                "total": total,
                "page": page,
                "page_size": page_size,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_record_response import UsageRecordResponse  # noqa: PLC0415

        d = dict(src_dict)
        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = UsageRecordResponse.from_dict(records_item_data)

            records.append(records_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_pages = d.pop("total_pages")

        usage_record_list_response = cls(
            records=records,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

        usage_record_list_response.additional_properties = d
        return usage_record_list_response

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
