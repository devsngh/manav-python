from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.predefined_fields_response_api_key_item import PredefinedFieldsResponseApiKeyItem
    from ..models.predefined_fields_response_cloud_item import PredefinedFieldsResponseCloudItem
    from ..models.predefined_fields_response_custom_item import PredefinedFieldsResponseCustomItem
    from ..models.predefined_fields_response_database_item import PredefinedFieldsResponseDatabaseItem
    from ..models.predefined_fields_response_oauth_item import PredefinedFieldsResponseOauthItem


T = TypeVar("T", bound="PredefinedFieldsResponse")


@_attrs_define
class PredefinedFieldsResponse:
    """
    Attributes:
        database (list[PredefinedFieldsResponseDatabaseItem]):
        oauth (list[PredefinedFieldsResponseOauthItem]):
        api_key (list[PredefinedFieldsResponseApiKeyItem]):
        cloud (list[PredefinedFieldsResponseCloudItem]):
        custom (list[PredefinedFieldsResponseCustomItem]):
    """

    database: list[PredefinedFieldsResponseDatabaseItem]
    oauth: list[PredefinedFieldsResponseOauthItem]
    api_key: list[PredefinedFieldsResponseApiKeyItem]
    cloud: list[PredefinedFieldsResponseCloudItem]
    custom: list[PredefinedFieldsResponseCustomItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        database = []
        for database_item_data in self.database:
            database_item = database_item_data.to_dict()
            database.append(database_item)

        oauth = []
        for oauth_item_data in self.oauth:
            oauth_item = oauth_item_data.to_dict()
            oauth.append(oauth_item)

        api_key = []
        for api_key_item_data in self.api_key:
            api_key_item = api_key_item_data.to_dict()
            api_key.append(api_key_item)

        cloud = []
        for cloud_item_data in self.cloud:
            cloud_item = cloud_item_data.to_dict()
            cloud.append(cloud_item)

        custom = []
        for custom_item_data in self.custom:
            custom_item = custom_item_data.to_dict()
            custom.append(custom_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "database": database,
                "oauth": oauth,
                "api_key": api_key,
                "cloud": cloud,
                "custom": custom,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.predefined_fields_response_api_key_item import PredefinedFieldsResponseApiKeyItem  # noqa: PLC0415
        from ..models.predefined_fields_response_cloud_item import PredefinedFieldsResponseCloudItem  # noqa: PLC0415
        from ..models.predefined_fields_response_custom_item import PredefinedFieldsResponseCustomItem  # noqa: PLC0415
        from ..models.predefined_fields_response_database_item import (
            PredefinedFieldsResponseDatabaseItem,  # noqa: PLC0415
        )
        from ..models.predefined_fields_response_oauth_item import PredefinedFieldsResponseOauthItem  # noqa: PLC0415

        d = dict(src_dict)
        database = []
        _database = d.pop("database")
        for database_item_data in _database:
            database_item = PredefinedFieldsResponseDatabaseItem.from_dict(database_item_data)

            database.append(database_item)

        oauth = []
        _oauth = d.pop("oauth")
        for oauth_item_data in _oauth:
            oauth_item = PredefinedFieldsResponseOauthItem.from_dict(oauth_item_data)

            oauth.append(oauth_item)

        api_key = []
        _api_key = d.pop("api_key")
        for api_key_item_data in _api_key:
            api_key_item = PredefinedFieldsResponseApiKeyItem.from_dict(api_key_item_data)

            api_key.append(api_key_item)

        cloud = []
        _cloud = d.pop("cloud")
        for cloud_item_data in _cloud:
            cloud_item = PredefinedFieldsResponseCloudItem.from_dict(cloud_item_data)

            cloud.append(cloud_item)

        custom = []
        _custom = d.pop("custom")
        for custom_item_data in _custom:
            custom_item = PredefinedFieldsResponseCustomItem.from_dict(custom_item_data)

            custom.append(custom_item)

        predefined_fields_response = cls(
            database=database,
            oauth=oauth,
            api_key=api_key,
            cloud=cloud,
            custom=custom,
        )

        predefined_fields_response.additional_properties = d
        return predefined_fields_response

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
