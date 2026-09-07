from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.world_sync_table_per_table import WorldSyncTablePerTable


T = TypeVar("T", bound="WorldSyncResponse")


@_attrs_define
class WorldSyncResponse:
    """
    Attributes:
        workspace_id (str):
        countries (WorldSyncTablePerTable):
        industries (WorldSyncTablePerTable):
        cities (WorldSyncTablePerTable):
        total_inserted (int):
        total_updated (int):
        message (str):
        total_errors (int | Unset):  Default: 0.
    """

    workspace_id: str
    countries: WorldSyncTablePerTable
    industries: WorldSyncTablePerTable
    cities: WorldSyncTablePerTable
    total_inserted: int
    total_updated: int
    message: str
    total_errors: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        countries = self.countries.to_dict()

        industries = self.industries.to_dict()

        cities = self.cities.to_dict()

        total_inserted = self.total_inserted

        total_updated = self.total_updated

        message = self.message

        total_errors = self.total_errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
                "countries": countries,
                "industries": industries,
                "cities": cities,
                "total_inserted": total_inserted,
                "total_updated": total_updated,
                "message": message,
            }
        )
        if total_errors is not UNSET:
            field_dict["total_errors"] = total_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.world_sync_table_per_table import WorldSyncTablePerTable  # noqa: PLC0415

        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        countries = WorldSyncTablePerTable.from_dict(d.pop("countries"))

        industries = WorldSyncTablePerTable.from_dict(d.pop("industries"))

        cities = WorldSyncTablePerTable.from_dict(d.pop("cities"))

        total_inserted = d.pop("total_inserted")

        total_updated = d.pop("total_updated")

        message = d.pop("message")

        total_errors = d.pop("total_errors", UNSET)

        world_sync_response = cls(
            workspace_id=workspace_id,
            countries=countries,
            industries=industries,
            cities=cities,
            total_inserted=total_inserted,
            total_updated=total_updated,
            message=message,
            total_errors=total_errors,
        )

        world_sync_response.additional_properties = d
        return world_sync_response

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
