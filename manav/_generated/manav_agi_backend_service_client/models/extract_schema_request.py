from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractSchemaRequest")


@_attrs_define
class ExtractSchemaRequest:
    """
    Attributes:
        connection_id (str): UserDatasourceConnection UUID
        enum_distinct_threshold (int | Unset): Columns with <= N distinct values are flagged is_enum=True. Agent decides
            the right value per workspace. Default: 20.
        sample_rows (int | Unset): Sample rows per table (for sample_values). 0 = skip sampling. Default: 10.
    """

    connection_id: str
    enum_distinct_threshold: int | Unset = 20
    sample_rows: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        enum_distinct_threshold = self.enum_distinct_threshold

        sample_rows = self.sample_rows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
            }
        )
        if enum_distinct_threshold is not UNSET:
            field_dict["enum_distinct_threshold"] = enum_distinct_threshold
        if sample_rows is not UNSET:
            field_dict["sample_rows"] = sample_rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = d.pop("connection_id")

        enum_distinct_threshold = d.pop("enum_distinct_threshold", UNSET)

        sample_rows = d.pop("sample_rows", UNSET)

        extract_schema_request = cls(
            connection_id=connection_id,
            enum_distinct_threshold=enum_distinct_threshold,
            sample_rows=sample_rows,
        )

        extract_schema_request.additional_properties = d
        return extract_schema_request

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
