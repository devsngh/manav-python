from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainStatus")


@_attrs_define
class DomainStatus:
    """
    Attributes:
        domain (str):
        database (str):
        table_count (int):
        size_mb (float):
        migration_head (None | str | Unset):
    """

    domain: str
    database: str
    table_count: int
    size_mb: float
    migration_head: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        database = self.database

        table_count = self.table_count

        size_mb = self.size_mb

        migration_head: None | str | Unset
        if isinstance(self.migration_head, Unset):
            migration_head = UNSET
        else:
            migration_head = self.migration_head

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "database": database,
                "table_count": table_count,
                "size_mb": size_mb,
            }
        )
        if migration_head is not UNSET:
            field_dict["migration_head"] = migration_head

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        database = d.pop("database")

        table_count = d.pop("table_count")

        size_mb = d.pop("size_mb")

        def _parse_migration_head(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        migration_head = _parse_migration_head(d.pop("migration_head", UNSET))

        domain_status = cls(
            domain=domain,
            database=database,
            table_count=table_count,
            size_mb=size_mb,
            migration_head=migration_head,
        )

        domain_status.additional_properties = d
        return domain_status

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
