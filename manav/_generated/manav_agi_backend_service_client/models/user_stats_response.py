from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserStatsResponse")


@_attrs_define
class UserStatsResponse:
    """User statistics

    Attributes:
        total_users (int):
        active_users (int):
        inactive_users (int):
        super_admins (int):
        regular_users (int):
        verified_users (int):
        unverified_users (int):
        users_with_bots (int):
        users_in_organizations (int):
    """

    total_users: int
    active_users: int
    inactive_users: int
    super_admins: int
    regular_users: int
    verified_users: int
    unverified_users: int
    users_with_bots: int
    users_in_organizations: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_users = self.total_users

        active_users = self.active_users

        inactive_users = self.inactive_users

        super_admins = self.super_admins

        regular_users = self.regular_users

        verified_users = self.verified_users

        unverified_users = self.unverified_users

        users_with_bots = self.users_with_bots

        users_in_organizations = self.users_in_organizations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_users": total_users,
                "active_users": active_users,
                "inactive_users": inactive_users,
                "super_admins": super_admins,
                "regular_users": regular_users,
                "verified_users": verified_users,
                "unverified_users": unverified_users,
                "users_with_bots": users_with_bots,
                "users_in_organizations": users_in_organizations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_users = d.pop("total_users")

        active_users = d.pop("active_users")

        inactive_users = d.pop("inactive_users")

        super_admins = d.pop("super_admins")

        regular_users = d.pop("regular_users")

        verified_users = d.pop("verified_users")

        unverified_users = d.pop("unverified_users")

        users_with_bots = d.pop("users_with_bots")

        users_in_organizations = d.pop("users_in_organizations")

        user_stats_response = cls(
            total_users=total_users,
            active_users=active_users,
            inactive_users=inactive_users,
            super_admins=super_admins,
            regular_users=regular_users,
            verified_users=verified_users,
            unverified_users=unverified_users,
            users_with_bots=users_with_bots,
            users_in_organizations=users_in_organizations,
        )

        user_stats_response.additional_properties = d
        return user_stats_response

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
