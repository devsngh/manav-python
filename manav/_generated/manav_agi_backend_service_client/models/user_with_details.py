from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_with_details_assigned_roles_item import UserWithDetailsAssignedRolesItem
    from ..models.user_with_details_organizations_item import UserWithDetailsOrganizationsItem


T = TypeVar("T", bound="UserWithDetails")


@_attrs_define
class UserWithDetails:
    """User with complete details including bot, roles, and organizations.
    `role` is the derived primary role name ("Super Admin" if the user holds
    that role, else "User"). Full role list is in `assigned_roles`.

        Attributes:
            id (UUID):
            email (str):
            full_name (str):
            role (str):
            is_active (bool):
            is_verified (bool):
            created_at (datetime.datetime):
            last_login (datetime.datetime | None | Unset):
            profile_picture_url (None | str | Unset):
            phone (None | str | Unset):
            address (None | str | Unset):
            city (None | str | Unset):
            country (None | str | Unset):
            bio (None | str | Unset):
            bot_id (None | Unset | UUID):
            bot_name (None | str | Unset):
            bot_identifier (None | str | Unset):
            organizations (list[UserWithDetailsOrganizationsItem] | Unset):
            assigned_roles (list[UserWithDetailsAssignedRolesItem] | Unset):
            permission_count (int | Unset):  Default: 0.
    """

    id: UUID
    email: str
    full_name: str
    role: str
    is_active: bool
    is_verified: bool
    created_at: datetime.datetime
    last_login: datetime.datetime | None | Unset = UNSET
    profile_picture_url: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    bot_id: None | Unset | UUID = UNSET
    bot_name: None | str | Unset = UNSET
    bot_identifier: None | str | Unset = UNSET
    organizations: list[UserWithDetailsOrganizationsItem] | Unset = UNSET
    assigned_roles: list[UserWithDetailsAssignedRolesItem] | Unset = UNSET
    permission_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email = self.email

        full_name = self.full_name

        role = self.role

        is_active = self.is_active

        is_verified = self.is_verified

        created_at = self.created_at.isoformat()

        last_login: None | str | Unset
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        bot_identifier: None | str | Unset
        if isinstance(self.bot_identifier, Unset):
            bot_identifier = UNSET
        else:
            bot_identifier = self.bot_identifier

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        assigned_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assigned_roles, Unset):
            assigned_roles = []
            for assigned_roles_item_data in self.assigned_roles:
                assigned_roles_item = assigned_roles_item_data.to_dict()
                assigned_roles.append(assigned_roles_item)

        permission_count = self.permission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "full_name": full_name,
                "role": role,
                "is_active": is_active,
                "is_verified": is_verified,
                "created_at": created_at,
            }
        )
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if bio is not UNSET:
            field_dict["bio"] = bio
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if bot_identifier is not UNSET:
            field_dict["bot_identifier"] = bot_identifier
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if assigned_roles is not UNSET:
            field_dict["assigned_roles"] = assigned_roles
        if permission_count is not UNSET:
            field_dict["permission_count"] = permission_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_with_details_assigned_roles_item import UserWithDetailsAssignedRolesItem  # noqa: PLC0415
        from ..models.user_with_details_organizations_item import UserWithDetailsOrganizationsItem  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        email = d.pop("email")

        full_name = d.pop("full_name")

        role = d.pop("role")

        is_active = d.pop("is_active")

        is_verified = d.pop("is_verified")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_last_login(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login = _parse_last_login(d.pop("last_login", UNSET))

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        def _parse_bot_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_identifier = _parse_bot_identifier(d.pop("bot_identifier", UNSET))

        _organizations = d.pop("organizations", UNSET)
        organizations: list[UserWithDetailsOrganizationsItem] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = UserWithDetailsOrganizationsItem.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        _assigned_roles = d.pop("assigned_roles", UNSET)
        assigned_roles: list[UserWithDetailsAssignedRolesItem] | Unset = UNSET
        if _assigned_roles is not UNSET:
            assigned_roles = []
            for assigned_roles_item_data in _assigned_roles:
                assigned_roles_item = UserWithDetailsAssignedRolesItem.from_dict(assigned_roles_item_data)

                assigned_roles.append(assigned_roles_item)

        permission_count = d.pop("permission_count", UNSET)

        user_with_details = cls(
            id=id,
            email=email,
            full_name=full_name,
            role=role,
            is_active=is_active,
            is_verified=is_verified,
            created_at=created_at,
            last_login=last_login,
            profile_picture_url=profile_picture_url,
            phone=phone,
            address=address,
            city=city,
            country=country,
            bio=bio,
            bot_id=bot_id,
            bot_name=bot_name,
            bot_identifier=bot_identifier,
            organizations=organizations,
            assigned_roles=assigned_roles,
            permission_count=permission_count,
        )

        user_with_details.additional_properties = d
        return user_with_details

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
