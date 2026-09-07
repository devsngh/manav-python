from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        id (UUID):
        email (str):
        full_name (str):
        role (str):
        org_id (None | UUID):
        is_verified (bool):
        is_active (bool):
        mfa_enabled (bool):
        profile_picture_url (None | str):
        agi_name (None | str):
        bot_id (None | str):
        position (None | str):
        age (int | None):
        phone_number (None | str):
        about (None | str):
        created_at (datetime.datetime):
        last_login_at (datetime.datetime | None):
        date_of_birth (datetime.date | None | Unset):
        subscription_tier (None | str | Unset):
        plan_name (None | str | Unset):
        onboarding_completed_at (datetime.datetime | None | Unset):
    """

    id: UUID
    email: str
    full_name: str
    role: str
    org_id: None | UUID
    is_verified: bool
    is_active: bool
    mfa_enabled: bool
    profile_picture_url: None | str
    agi_name: None | str
    bot_id: None | str
    position: None | str
    age: int | None
    phone_number: None | str
    about: None | str
    created_at: datetime.datetime
    last_login_at: datetime.datetime | None
    date_of_birth: datetime.date | None | Unset = UNSET
    subscription_tier: None | str | Unset = UNSET
    plan_name: None | str | Unset = UNSET
    onboarding_completed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        email = self.email

        full_name = self.full_name

        role = self.role

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        is_verified = self.is_verified

        is_active = self.is_active

        mfa_enabled = self.mfa_enabled

        profile_picture_url: None | str
        profile_picture_url = self.profile_picture_url

        agi_name: None | str
        agi_name = self.agi_name

        bot_id: None | str
        bot_id = self.bot_id

        position: None | str
        position = self.position

        age: int | None
        age = self.age

        phone_number: None | str
        phone_number = self.phone_number

        about: None | str
        about = self.about

        created_at = self.created_at.isoformat()

        last_login_at: None | str
        if isinstance(self.last_login_at, datetime.datetime):
            last_login_at = self.last_login_at.isoformat()
        else:
            last_login_at = self.last_login_at

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        subscription_tier: None | str | Unset
        if isinstance(self.subscription_tier, Unset):
            subscription_tier = UNSET
        else:
            subscription_tier = self.subscription_tier

        plan_name: None | str | Unset
        if isinstance(self.plan_name, Unset):
            plan_name = UNSET
        else:
            plan_name = self.plan_name

        onboarding_completed_at: None | str | Unset
        if isinstance(self.onboarding_completed_at, Unset):
            onboarding_completed_at = UNSET
        elif isinstance(self.onboarding_completed_at, datetime.datetime):
            onboarding_completed_at = self.onboarding_completed_at.isoformat()
        else:
            onboarding_completed_at = self.onboarding_completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "full_name": full_name,
                "role": role,
                "org_id": org_id,
                "is_verified": is_verified,
                "is_active": is_active,
                "mfa_enabled": mfa_enabled,
                "profile_picture_url": profile_picture_url,
                "agi_name": agi_name,
                "bot_id": bot_id,
                "position": position,
                "age": age,
                "phone_number": phone_number,
                "about": about,
                "created_at": created_at,
                "last_login_at": last_login_at,
            }
        )
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if subscription_tier is not UNSET:
            field_dict["subscription_tier"] = subscription_tier
        if plan_name is not UNSET:
            field_dict["plan_name"] = plan_name
        if onboarding_completed_at is not UNSET:
            field_dict["onboarding_completed_at"] = onboarding_completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        email = d.pop("email")

        full_name = d.pop("full_name")

        role = d.pop("role")

        def _parse_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        org_id = _parse_org_id(d.pop("org_id"))

        is_verified = d.pop("is_verified")

        is_active = d.pop("is_active")

        mfa_enabled = d.pop("mfa_enabled")

        def _parse_profile_picture_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url"))

        def _parse_agi_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agi_name = _parse_agi_name(d.pop("agi_name"))

        def _parse_bot_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bot_id = _parse_bot_id(d.pop("bot_id"))

        def _parse_position(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        position = _parse_position(d.pop("position"))

        def _parse_age(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        age = _parse_age(d.pop("age"))

        def _parse_phone_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone_number = _parse_phone_number(d.pop("phone_number"))

        def _parse_about(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        about = _parse_about(d.pop("about"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_last_login_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_login_at = _parse_last_login_at(d.pop("last_login_at"))

        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = datetime.date.fromisoformat(data)

                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        def _parse_subscription_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subscription_tier = _parse_subscription_tier(d.pop("subscription_tier", UNSET))

        def _parse_plan_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_name = _parse_plan_name(d.pop("plan_name", UNSET))

        def _parse_onboarding_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                onboarding_completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return onboarding_completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        onboarding_completed_at = _parse_onboarding_completed_at(d.pop("onboarding_completed_at", UNSET))

        user_response = cls(
            id=id,
            email=email,
            full_name=full_name,
            role=role,
            org_id=org_id,
            is_verified=is_verified,
            is_active=is_active,
            mfa_enabled=mfa_enabled,
            profile_picture_url=profile_picture_url,
            agi_name=agi_name,
            bot_id=bot_id,
            position=position,
            age=age,
            phone_number=phone_number,
            about=about,
            created_at=created_at,
            last_login_at=last_login_at,
            date_of_birth=date_of_birth,
            subscription_tier=subscription_tier,
            plan_name=plan_name,
            onboarding_completed_at=onboarding_completed_at,
        )

        user_response.additional_properties = d
        return user_response

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
