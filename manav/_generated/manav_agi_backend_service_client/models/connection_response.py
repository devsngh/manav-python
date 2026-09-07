from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datasource_response import DatasourceResponse


T = TypeVar("T", bound="ConnectionResponse")


@_attrs_define
class ConnectionResponse:
    """
    Attributes:
        id (UUID):
        user_id (UUID):
        datasource_id (UUID):
        connection_status (str):
        connected_at (datetime.datetime):
        last_used_at (datetime.datetime | None):
        datasource (DatasourceResponse | None | Unset):
    """

    id: UUID
    user_id: UUID
    datasource_id: UUID
    connection_status: str
    connected_at: datetime.datetime
    last_used_at: datetime.datetime | None
    datasource: DatasourceResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datasource_response import DatasourceResponse  # noqa: PLC0415

        id = str(self.id)

        user_id = str(self.user_id)

        datasource_id = str(self.datasource_id)

        connection_status = self.connection_status

        connected_at = self.connected_at.isoformat()

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        datasource: dict[str, Any] | None | Unset
        if isinstance(self.datasource, Unset):
            datasource = UNSET
        elif isinstance(self.datasource, DatasourceResponse):
            datasource = self.datasource.to_dict()
        else:
            datasource = self.datasource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "datasource_id": datasource_id,
                "connection_status": connection_status,
                "connected_at": connected_at,
                "last_used_at": last_used_at,
            }
        )
        if datasource is not UNSET:
            field_dict["datasource"] = datasource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datasource_response import DatasourceResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        datasource_id = UUID(d.pop("datasource_id"))

        connection_status = d.pop("connection_status")

        connected_at = datetime.datetime.fromisoformat(d.pop("connected_at"))

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_datasource(data: object) -> DatasourceResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                datasource_type_0 = DatasourceResponse.from_dict(data)

                return datasource_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasourceResponse | None | Unset, data)

        datasource = _parse_datasource(d.pop("datasource", UNSET))

        connection_response = cls(
            id=id,
            user_id=user_id,
            datasource_id=datasource_id,
            connection_status=connection_status,
            connected_at=connected_at,
            last_used_at=last_used_at,
            datasource=datasource,
        )

        connection_response.additional_properties = d
        return connection_response

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
