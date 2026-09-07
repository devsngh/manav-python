from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_bot_group_response import UserBotGroupResponse


T = TypeVar("T", bound="UserBotGroupListResponse")


@_attrs_define
class UserBotGroupListResponse:
    """Paginated list of user-bot groups.

    Attributes:
        groups (list[UserBotGroupResponse]):
        total (int):
        page (int):
        page_size (int):
        has_more (bool):
    """

    groups: list[UserBotGroupResponse]
    total: int
    page: int
    page_size: int
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groups": groups,
                "total": total,
                "page": page,
                "page_size": page_size,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_bot_group_response import UserBotGroupResponse  # noqa: PLC0415

        d = dict(src_dict)
        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = UserBotGroupResponse.from_dict(groups_item_data)

            groups.append(groups_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        has_more = d.pop("has_more")

        user_bot_group_list_response = cls(
            groups=groups,
            total=total,
            page=page,
            page_size=page_size,
            has_more=has_more,
        )

        user_bot_group_list_response.additional_properties = d
        return user_bot_group_list_response

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
