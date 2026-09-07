from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.existing_listing_ref import ExistingListingRef


T = TypeVar("T", bound="UserAgentResponse")


@_attrs_define
class UserAgentResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        source (str):
        description (None | str | Unset):
        model_id (None | str | Unset):
        is_active (bool | Unset):  Default: True.
        purchase_id (None | Unset | UUID):
        created_at (datetime.datetime | None | Unset):
        existing_listing (ExistingListingRef | None | Unset):
        bot_id (None | Unset | UUID):
        bot_name (None | str | Unset):
        bot_profile_picture_url (None | str | Unset):
    """

    id: UUID
    name: str
    source: str
    description: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    is_active: bool | Unset = True
    purchase_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    existing_listing: ExistingListingRef | None | Unset = UNSET
    bot_id: None | Unset | UUID = UNSET
    bot_name: None | str | Unset = UNSET
    bot_profile_picture_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.existing_listing_ref import ExistingListingRef  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        source = self.source

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        is_active = self.is_active

        purchase_id: None | str | Unset
        if isinstance(self.purchase_id, Unset):
            purchase_id = UNSET
        elif isinstance(self.purchase_id, UUID):
            purchase_id = str(self.purchase_id)
        else:
            purchase_id = self.purchase_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        existing_listing: dict[str, Any] | None | Unset
        if isinstance(self.existing_listing, Unset):
            existing_listing = UNSET
        elif isinstance(self.existing_listing, ExistingListingRef):
            existing_listing = self.existing_listing.to_dict()
        else:
            existing_listing = self.existing_listing

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

        bot_profile_picture_url: None | str | Unset
        if isinstance(self.bot_profile_picture_url, Unset):
            bot_profile_picture_url = UNSET
        else:
            bot_profile_picture_url = self.bot_profile_picture_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "source": source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if purchase_id is not UNSET:
            field_dict["purchase_id"] = purchase_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if existing_listing is not UNSET:
            field_dict["existing_listing"] = existing_listing
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if bot_profile_picture_url is not UNSET:
            field_dict["bot_profile_picture_url"] = bot_profile_picture_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.existing_listing_ref import ExistingListingRef  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        source = d.pop("source")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_purchase_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purchase_id_type_0 = UUID(data)

                return purchase_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        purchase_id = _parse_purchase_id(d.pop("purchase_id", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_existing_listing(data: object) -> ExistingListingRef | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                existing_listing_type_0 = ExistingListingRef.from_dict(data)

                return existing_listing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExistingListingRef | None | Unset, data)

        existing_listing = _parse_existing_listing(d.pop("existing_listing", UNSET))

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

        def _parse_bot_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_profile_picture_url = _parse_bot_profile_picture_url(d.pop("bot_profile_picture_url", UNSET))

        user_agent_response = cls(
            id=id,
            name=name,
            source=source,
            description=description,
            model_id=model_id,
            is_active=is_active,
            purchase_id=purchase_id,
            created_at=created_at,
            existing_listing=existing_listing,
            bot_id=bot_id,
            bot_name=bot_name,
            bot_profile_picture_url=bot_profile_picture_url,
        )

        user_agent_response.additional_properties = d
        return user_agent_response

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
