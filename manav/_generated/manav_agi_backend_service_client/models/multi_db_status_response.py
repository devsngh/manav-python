from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_status import DomainStatus


T = TypeVar("T", bound="MultiDbStatusResponse")


@_attrs_define
class MultiDbStatusResponse:
    """
    Attributes:
        domains (list[DomainStatus]):
        total_tables (int):
        total_size_mb (float):
        backup_available (bool):
        last_backup (None | str | Unset):
    """

    domains: list[DomainStatus]
    total_tables: int
    total_size_mb: float
    backup_available: bool
    last_backup: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()
            domains.append(domains_item)

        total_tables = self.total_tables

        total_size_mb = self.total_size_mb

        backup_available = self.backup_available

        last_backup: None | str | Unset
        if isinstance(self.last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = self.last_backup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domains": domains,
                "total_tables": total_tables,
                "total_size_mb": total_size_mb,
                "backup_available": backup_available,
            }
        )
        if last_backup is not UNSET:
            field_dict["last_backup"] = last_backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_status import DomainStatus  # noqa: PLC0415

        d = dict(src_dict)
        domains = []
        _domains = d.pop("domains")
        for domains_item_data in _domains:
            domains_item = DomainStatus.from_dict(domains_item_data)

            domains.append(domains_item)

        total_tables = d.pop("total_tables")

        total_size_mb = d.pop("total_size_mb")

        backup_available = d.pop("backup_available")

        def _parse_last_backup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_backup = _parse_last_backup(d.pop("last_backup", UNSET))

        multi_db_status_response = cls(
            domains=domains,
            total_tables=total_tables,
            total_size_mb=total_size_mb,
            backup_available=backup_available,
            last_backup=last_backup,
        )

        multi_db_status_response.additional_properties = d
        return multi_db_status_response

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
