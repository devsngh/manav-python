from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_tree_member_bot_type_0 import OrgTreeMemberBotType0


T = TypeVar("T", bound="OrgTreeMember")


@_attrs_define
class OrgTreeMember:
    """A user/bot assigned to a position in the org tree

    Attributes:
        user_id (str):
        full_name (str):
        email (str):
        profile_picture_url (None | str | Unset):
        bot (None | OrgTreeMemberBotType0 | Unset):
    """

    user_id: str
    full_name: str
    email: str
    profile_picture_url: None | str | Unset = UNSET
    bot: None | OrgTreeMemberBotType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.org_tree_member_bot_type_0 import OrgTreeMemberBotType0  # noqa: PLC0415

        user_id = self.user_id

        full_name = self.full_name

        email = self.email

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        bot: dict[str, Any] | None | Unset
        if isinstance(self.bot, Unset):
            bot = UNSET
        elif isinstance(self.bot, OrgTreeMemberBotType0):
            bot = self.bot.to_dict()
        else:
            bot = self.bot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "full_name": full_name,
                "email": email,
            }
        )
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if bot is not UNSET:
            field_dict["bot"] = bot

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_tree_member_bot_type_0 import OrgTreeMemberBotType0  # noqa: PLC0415

        d = dict(src_dict)
        user_id = d.pop("user_id")

        full_name = d.pop("full_name")

        email = d.pop("email")

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url", UNSET))

        def _parse_bot(data: object) -> None | OrgTreeMemberBotType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bot_type_0 = OrgTreeMemberBotType0.from_dict(data)

                return bot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrgTreeMemberBotType0 | Unset, data)

        bot = _parse_bot(d.pop("bot", UNSET))

        org_tree_member = cls(
            user_id=user_id,
            full_name=full_name,
            email=email,
            profile_picture_url=profile_picture_url,
            bot=bot,
        )

        org_tree_member.additional_properties = d
        return org_tree_member

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
