from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_count import CategoryCount
    from ..models.error_path import ErrorPath
    from ..models.error_trend import ErrorTrend
    from ..models.level_count import LevelCount
    from ..models.top_error_message import TopErrorMessage


T = TypeVar("T", bound="SystemLogStatsResponse")


@_attrs_define
class SystemLogStatsResponse:
    """
    Attributes:
        total_logs (int):
        by_level (list[LevelCount]):
        by_category (list[CategoryCount]):
        top_error_paths (list[ErrorPath]):
        error_trends (list[ErrorTrend]):
        top_error_messages (list[TopErrorMessage]):
    """

    total_logs: int
    by_level: list[LevelCount]
    by_category: list[CategoryCount]
    top_error_paths: list[ErrorPath]
    error_trends: list[ErrorTrend]
    top_error_messages: list[TopErrorMessage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_logs = self.total_logs

        by_level = []
        for by_level_item_data in self.by_level:
            by_level_item = by_level_item_data.to_dict()
            by_level.append(by_level_item)

        by_category = []
        for by_category_item_data in self.by_category:
            by_category_item = by_category_item_data.to_dict()
            by_category.append(by_category_item)

        top_error_paths = []
        for top_error_paths_item_data in self.top_error_paths:
            top_error_paths_item = top_error_paths_item_data.to_dict()
            top_error_paths.append(top_error_paths_item)

        error_trends = []
        for error_trends_item_data in self.error_trends:
            error_trends_item = error_trends_item_data.to_dict()
            error_trends.append(error_trends_item)

        top_error_messages = []
        for top_error_messages_item_data in self.top_error_messages:
            top_error_messages_item = top_error_messages_item_data.to_dict()
            top_error_messages.append(top_error_messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_logs": total_logs,
                "by_level": by_level,
                "by_category": by_category,
                "top_error_paths": top_error_paths,
                "error_trends": error_trends,
                "top_error_messages": top_error_messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_count import CategoryCount  # noqa: PLC0415
        from ..models.error_path import ErrorPath  # noqa: PLC0415
        from ..models.error_trend import ErrorTrend  # noqa: PLC0415
        from ..models.level_count import LevelCount  # noqa: PLC0415
        from ..models.top_error_message import TopErrorMessage  # noqa: PLC0415

        d = dict(src_dict)
        total_logs = d.pop("total_logs")

        by_level = []
        _by_level = d.pop("by_level")
        for by_level_item_data in _by_level:
            by_level_item = LevelCount.from_dict(by_level_item_data)

            by_level.append(by_level_item)

        by_category = []
        _by_category = d.pop("by_category")
        for by_category_item_data in _by_category:
            by_category_item = CategoryCount.from_dict(by_category_item_data)

            by_category.append(by_category_item)

        top_error_paths = []
        _top_error_paths = d.pop("top_error_paths")
        for top_error_paths_item_data in _top_error_paths:
            top_error_paths_item = ErrorPath.from_dict(top_error_paths_item_data)

            top_error_paths.append(top_error_paths_item)

        error_trends = []
        _error_trends = d.pop("error_trends")
        for error_trends_item_data in _error_trends:
            error_trends_item = ErrorTrend.from_dict(error_trends_item_data)

            error_trends.append(error_trends_item)

        top_error_messages = []
        _top_error_messages = d.pop("top_error_messages")
        for top_error_messages_item_data in _top_error_messages:
            top_error_messages_item = TopErrorMessage.from_dict(top_error_messages_item_data)

            top_error_messages.append(top_error_messages_item)

        system_log_stats_response = cls(
            total_logs=total_logs,
            by_level=by_level,
            by_category=by_category,
            top_error_paths=top_error_paths,
            error_trends=error_trends,
            top_error_messages=top_error_messages,
        )

        system_log_stats_response.additional_properties = d
        return system_log_stats_response

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
