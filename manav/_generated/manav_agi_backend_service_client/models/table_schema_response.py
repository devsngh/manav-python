from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.column_info import ColumnInfo
    from ..models.table_schema_response_foreign_keys_item import TableSchemaResponseForeignKeysItem
    from ..models.table_schema_response_indexes_item import TableSchemaResponseIndexesItem


T = TypeVar("T", bound="TableSchemaResponse")


@_attrs_define
class TableSchemaResponse:
    """
    Attributes:
        table_name (str):
        columns (list[ColumnInfo]):
        schema_name (None | str | Unset):
        indexes (list[TableSchemaResponseIndexesItem] | Unset):
        foreign_keys (list[TableSchemaResponseForeignKeysItem] | Unset):
        row_count (int | None | Unset):
        size_mb (float | None | Unset):
    """

    table_name: str
    columns: list[ColumnInfo]
    schema_name: None | str | Unset = UNSET
    indexes: list[TableSchemaResponseIndexesItem] | Unset = UNSET
    foreign_keys: list[TableSchemaResponseForeignKeysItem] | Unset = UNSET
    row_count: int | None | Unset = UNSET
    size_mb: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        schema_name: None | str | Unset
        if isinstance(self.schema_name, Unset):
            schema_name = UNSET
        else:
            schema_name = self.schema_name

        indexes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.indexes, Unset):
            indexes = []
            for indexes_item_data in self.indexes:
                indexes_item = indexes_item_data.to_dict()
                indexes.append(indexes_item)

        foreign_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.foreign_keys, Unset):
            foreign_keys = []
            for foreign_keys_item_data in self.foreign_keys:
                foreign_keys_item = foreign_keys_item_data.to_dict()
                foreign_keys.append(foreign_keys_item)

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        size_mb: float | None | Unset
        if isinstance(self.size_mb, Unset):
            size_mb = UNSET
        else:
            size_mb = self.size_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table_name": table_name,
                "columns": columns,
            }
        )
        if schema_name is not UNSET:
            field_dict["schema_name"] = schema_name
        if indexes is not UNSET:
            field_dict["indexes"] = indexes
        if foreign_keys is not UNSET:
            field_dict["foreign_keys"] = foreign_keys
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if size_mb is not UNSET:
            field_dict["size_mb"] = size_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.column_info import ColumnInfo  # noqa: PLC0415
        from ..models.table_schema_response_foreign_keys_item import TableSchemaResponseForeignKeysItem  # noqa: PLC0415
        from ..models.table_schema_response_indexes_item import TableSchemaResponseIndexesItem  # noqa: PLC0415

        d = dict(src_dict)
        table_name = d.pop("table_name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ColumnInfo.from_dict(columns_item_data)

            columns.append(columns_item)

        def _parse_schema_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_name = _parse_schema_name(d.pop("schema_name", UNSET))

        _indexes = d.pop("indexes", UNSET)
        indexes: list[TableSchemaResponseIndexesItem] | Unset = UNSET
        if _indexes is not UNSET:
            indexes = []
            for indexes_item_data in _indexes:
                indexes_item = TableSchemaResponseIndexesItem.from_dict(indexes_item_data)

                indexes.append(indexes_item)

        _foreign_keys = d.pop("foreign_keys", UNSET)
        foreign_keys: list[TableSchemaResponseForeignKeysItem] | Unset = UNSET
        if _foreign_keys is not UNSET:
            foreign_keys = []
            for foreign_keys_item_data in _foreign_keys:
                foreign_keys_item = TableSchemaResponseForeignKeysItem.from_dict(foreign_keys_item_data)

                foreign_keys.append(foreign_keys_item)

        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        def _parse_size_mb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_mb = _parse_size_mb(d.pop("size_mb", UNSET))

        table_schema_response = cls(
            table_name=table_name,
            columns=columns,
            schema_name=schema_name,
            indexes=indexes,
            foreign_keys=foreign_keys,
            row_count=row_count,
            size_mb=size_mb,
        )

        table_schema_response.additional_properties = d
        return table_schema_response

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
