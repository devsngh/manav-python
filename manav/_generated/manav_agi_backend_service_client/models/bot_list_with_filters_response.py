from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bot_list_with_filters_response_filters_applied import BotListWithFiltersResponseFiltersApplied
    from ..models.bot_with_user_info import BotWithUserInfo


T = TypeVar("T", bound="BotListWithFiltersResponse")


@_attrs_define
class BotListWithFiltersResponse:
    """List of bots with filters and pagination

    Attributes:
        bots (list[BotWithUserInfo]):
        total (int):
        page (int):
        page_size (int):
        filters_applied (BotListWithFiltersResponseFiltersApplied):
    """

    bots: list[BotWithUserInfo]
    total: int
    page: int
    page_size: int
    filters_applied: BotListWithFiltersResponseFiltersApplied
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bots = []
        for bots_item_data in self.bots:
            bots_item = bots_item_data.to_dict()
            bots.append(bots_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        filters_applied = self.filters_applied.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bots": bots,
                "total": total,
                "page": page,
                "page_size": page_size,
                "filters_applied": filters_applied,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_list_with_filters_response_filters_applied import (
            BotListWithFiltersResponseFiltersApplied,  # noqa: PLC0415
        )
        from ..models.bot_with_user_info import BotWithUserInfo  # noqa: PLC0415

        d = dict(src_dict)
        bots = []
        _bots = d.pop("bots")
        for bots_item_data in _bots:
            bots_item = BotWithUserInfo.from_dict(bots_item_data)

            bots.append(bots_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        filters_applied = BotListWithFiltersResponseFiltersApplied.from_dict(d.pop("filters_applied"))

        bot_list_with_filters_response = cls(
            bots=bots,
            total=total,
            page=page,
            page_size=page_size,
            filters_applied=filters_applied,
        )

        bot_list_with_filters_response.additional_properties = d
        return bot_list_with_filters_response

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
