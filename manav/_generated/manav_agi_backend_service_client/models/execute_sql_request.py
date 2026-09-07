from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteSQLRequest")


@_attrs_define
class ExecuteSQLRequest:
    """
    Attributes:
        profile_id (str):
        database_name (str):
        query (str):
        limit (int | Unset):  Default: 100.
    """

    profile_id: str
    database_name: str
    query: str
    limit: int | Unset = 100
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        database_name = self.database_name

        query = self.query

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profile_id": profile_id,
                "database_name": database_name,
                "query": query,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        profile_id = d.pop("profile_id")

        database_name = d.pop("database_name")

        query = d.pop("query")

        limit = d.pop("limit", UNSET)

        execute_sql_request = cls(
            profile_id=profile_id,
            database_name=database_name,
            query=query,
            limit=limit,
        )

        execute_sql_request.additional_properties = d
        return execute_sql_request

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
