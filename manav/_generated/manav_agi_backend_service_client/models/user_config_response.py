from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_parameter_value_response import UserParameterValueResponse


T = TypeVar("T", bound="UserConfigResponse")


@_attrs_define
class UserConfigResponse:
    """User config response

    Attributes:
        id (UUID):
        llm_id (UUID):
        user_id (UUID):
        config_name (str):
        is_enabled (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        llm_name (str):
        llm_provider (str):
        has_user_credentials (bool | Unset):  Default: False.
        user_endpoint_url (None | str | Unset):
        locked_by_listing_id (None | Unset | UUID):
        parameter_values (list[UserParameterValueResponse] | Unset):
    """

    id: UUID
    llm_id: UUID
    user_id: UUID
    config_name: str
    is_enabled: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    llm_name: str
    llm_provider: str
    has_user_credentials: bool | Unset = False
    user_endpoint_url: None | str | Unset = UNSET
    locked_by_listing_id: None | Unset | UUID = UNSET
    parameter_values: list[UserParameterValueResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        llm_id = str(self.llm_id)

        user_id = str(self.user_id)

        config_name = self.config_name

        is_enabled = self.is_enabled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        llm_name = self.llm_name

        llm_provider = self.llm_provider

        has_user_credentials = self.has_user_credentials

        user_endpoint_url: None | str | Unset
        if isinstance(self.user_endpoint_url, Unset):
            user_endpoint_url = UNSET
        else:
            user_endpoint_url = self.user_endpoint_url

        locked_by_listing_id: None | str | Unset
        if isinstance(self.locked_by_listing_id, Unset):
            locked_by_listing_id = UNSET
        elif isinstance(self.locked_by_listing_id, UUID):
            locked_by_listing_id = str(self.locked_by_listing_id)
        else:
            locked_by_listing_id = self.locked_by_listing_id

        parameter_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameter_values, Unset):
            parameter_values = []
            for parameter_values_item_data in self.parameter_values:
                parameter_values_item = parameter_values_item_data.to_dict()
                parameter_values.append(parameter_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "llm_id": llm_id,
                "user_id": user_id,
                "config_name": config_name,
                "is_enabled": is_enabled,
                "created_at": created_at,
                "updated_at": updated_at,
                "llm_name": llm_name,
                "llm_provider": llm_provider,
            }
        )
        if has_user_credentials is not UNSET:
            field_dict["has_user_credentials"] = has_user_credentials
        if user_endpoint_url is not UNSET:
            field_dict["user_endpoint_url"] = user_endpoint_url
        if locked_by_listing_id is not UNSET:
            field_dict["locked_by_listing_id"] = locked_by_listing_id
        if parameter_values is not UNSET:
            field_dict["parameter_values"] = parameter_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_parameter_value_response import UserParameterValueResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        llm_id = UUID(d.pop("llm_id"))

        user_id = UUID(d.pop("user_id"))

        config_name = d.pop("config_name")

        is_enabled = d.pop("is_enabled")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        llm_name = d.pop("llm_name")

        llm_provider = d.pop("llm_provider")

        has_user_credentials = d.pop("has_user_credentials", UNSET)

        def _parse_user_endpoint_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_endpoint_url = _parse_user_endpoint_url(d.pop("user_endpoint_url", UNSET))

        def _parse_locked_by_listing_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_by_listing_id_type_0 = UUID(data)

                return locked_by_listing_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        locked_by_listing_id = _parse_locked_by_listing_id(d.pop("locked_by_listing_id", UNSET))

        _parameter_values = d.pop("parameter_values", UNSET)
        parameter_values: list[UserParameterValueResponse] | Unset = UNSET
        if _parameter_values is not UNSET:
            parameter_values = []
            for parameter_values_item_data in _parameter_values:
                parameter_values_item = UserParameterValueResponse.from_dict(parameter_values_item_data)

                parameter_values.append(parameter_values_item)

        user_config_response = cls(
            id=id,
            llm_id=llm_id,
            user_id=user_id,
            config_name=config_name,
            is_enabled=is_enabled,
            created_at=created_at,
            updated_at=updated_at,
            llm_name=llm_name,
            llm_provider=llm_provider,
            has_user_credentials=has_user_credentials,
            user_endpoint_url=user_endpoint_url,
            locked_by_listing_id=locked_by_listing_id,
            parameter_values=parameter_values,
        )

        user_config_response.additional_properties = d
        return user_config_response

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
