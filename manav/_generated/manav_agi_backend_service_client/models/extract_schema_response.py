from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.raw_fk import RawFK
    from ..models.raw_table import RawTable


T = TypeVar("T", bound="ExtractSchemaResponse")


@_attrs_define
class ExtractSchemaResponse:
    """
    Attributes:
        engine (str):
        tables (list[RawTable]):
        fks (list[RawFK]):
        table_count (int):
        column_count (int):
    """

    engine: str
    tables: list[RawTable]
    fks: list[RawFK]
    table_count: int
    column_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        engine = self.engine

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()
            tables.append(tables_item)

        fks = []
        for fks_item_data in self.fks:
            fks_item = fks_item_data.to_dict()
            fks.append(fks_item)

        table_count = self.table_count

        column_count = self.column_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "engine": engine,
                "tables": tables,
                "fks": fks,
                "table_count": table_count,
                "column_count": column_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_fk import RawFK  # noqa: PLC0415
        from ..models.raw_table import RawTable  # noqa: PLC0415

        d = dict(src_dict)
        engine = d.pop("engine")

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = RawTable.from_dict(tables_item_data)

            tables.append(tables_item)

        fks = []
        _fks = d.pop("fks")
        for fks_item_data in _fks:
            fks_item = RawFK.from_dict(fks_item_data)

            fks.append(fks_item)

        table_count = d.pop("table_count")

        column_count = d.pop("column_count")

        extract_schema_response = cls(
            engine=engine,
            tables=tables,
            fks=fks,
            table_count=table_count,
            column_count=column_count,
        )

        extract_schema_response.additional_properties = d
        return extract_schema_response

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
