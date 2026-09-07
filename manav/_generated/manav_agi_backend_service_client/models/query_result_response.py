from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_result_response_rows_item import QueryResultResponseRowsItem


T = TypeVar("T", bound="QueryResultResponse")


@_attrs_define
class QueryResultResponse:
    """
    Attributes:
        columns (list[str]):
        rows (list[QueryResultResponseRowsItem]):
        row_count (int):
        execution_time_ms (float):
    """

    columns: list[str]
    rows: list[QueryResultResponseRowsItem]
    row_count: int
    execution_time_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        columns = self.columns

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        row_count = self.row_count

        execution_time_ms = self.execution_time_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columns": columns,
                "rows": rows,
                "row_count": row_count,
                "execution_time_ms": execution_time_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_result_response_rows_item import QueryResultResponseRowsItem  # noqa: PLC0415

        d = dict(src_dict)
        columns = cast(list[str], d.pop("columns"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = QueryResultResponseRowsItem.from_dict(rows_item_data)

            rows.append(rows_item)

        row_count = d.pop("row_count")

        execution_time_ms = d.pop("execution_time_ms")

        query_result_response = cls(
            columns=columns,
            rows=rows,
            row_count=row_count,
            execution_time_ms=execution_time_ms,
        )

        query_result_response.additional_properties = d
        return query_result_response

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
