from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datasource_metrics_by_status import DatasourceMetricsByStatus
    from ..models.datasource_metrics_most_popular_type_0 import DatasourceMetricsMostPopularType0


T = TypeVar("T", bound="DatasourceMetrics")


@_attrs_define
class DatasourceMetrics:
    """
    Attributes:
        total_datasources (int):
        by_status (DatasourceMetricsByStatus):
        total_connections (int):
        connected_users (int):
        most_popular (DatasourceMetricsMostPopularType0 | None | Unset):
    """

    total_datasources: int
    by_status: DatasourceMetricsByStatus
    total_connections: int
    connected_users: int
    most_popular: DatasourceMetricsMostPopularType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datasource_metrics_most_popular_type_0 import DatasourceMetricsMostPopularType0  # noqa: PLC0415

        total_datasources = self.total_datasources

        by_status = self.by_status.to_dict()

        total_connections = self.total_connections

        connected_users = self.connected_users

        most_popular: dict[str, Any] | None | Unset
        if isinstance(self.most_popular, Unset):
            most_popular = UNSET
        elif isinstance(self.most_popular, DatasourceMetricsMostPopularType0):
            most_popular = self.most_popular.to_dict()
        else:
            most_popular = self.most_popular

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_datasources": total_datasources,
                "by_status": by_status,
                "total_connections": total_connections,
                "connected_users": connected_users,
            }
        )
        if most_popular is not UNSET:
            field_dict["most_popular"] = most_popular

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datasource_metrics_by_status import DatasourceMetricsByStatus  # noqa: PLC0415
        from ..models.datasource_metrics_most_popular_type_0 import DatasourceMetricsMostPopularType0  # noqa: PLC0415

        d = dict(src_dict)
        total_datasources = d.pop("total_datasources")

        by_status = DatasourceMetricsByStatus.from_dict(d.pop("by_status"))

        total_connections = d.pop("total_connections")

        connected_users = d.pop("connected_users")

        def _parse_most_popular(data: object) -> DatasourceMetricsMostPopularType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                most_popular_type_0 = DatasourceMetricsMostPopularType0.from_dict(data)

                return most_popular_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatasourceMetricsMostPopularType0 | None | Unset, data)

        most_popular = _parse_most_popular(d.pop("most_popular", UNSET))

        datasource_metrics = cls(
            total_datasources=total_datasources,
            by_status=by_status,
            total_connections=total_connections,
            connected_users=connected_users,
            most_popular=most_popular,
        )

        datasource_metrics.additional_properties = d
        return datasource_metrics

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
