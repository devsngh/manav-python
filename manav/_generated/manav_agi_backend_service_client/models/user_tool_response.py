from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.existing_listing_ref import ExistingListingRef


T = TypeVar("T", bound="UserToolResponse")


@_attrs_define
class UserToolResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        source (str):
        description (None | str | Unset):
        mcp_type (None | str | Unset):
        connection_status (str | Unset):  Default: 'disconnected'.
        datasource_id (None | Unset | UUID):
        existing_listing (ExistingListingRef | None | Unset):
    """

    id: UUID
    name: str
    source: str
    description: None | str | Unset = UNSET
    mcp_type: None | str | Unset = UNSET
    connection_status: str | Unset = "disconnected"
    datasource_id: None | Unset | UUID = UNSET
    existing_listing: ExistingListingRef | None | Unset = UNSET
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

        mcp_type: None | str | Unset
        if isinstance(self.mcp_type, Unset):
            mcp_type = UNSET
        else:
            mcp_type = self.mcp_type

        connection_status = self.connection_status

        datasource_id: None | str | Unset
        if isinstance(self.datasource_id, Unset):
            datasource_id = UNSET
        elif isinstance(self.datasource_id, UUID):
            datasource_id = str(self.datasource_id)
        else:
            datasource_id = self.datasource_id

        existing_listing: dict[str, Any] | None | Unset
        if isinstance(self.existing_listing, Unset):
            existing_listing = UNSET
        elif isinstance(self.existing_listing, ExistingListingRef):
            existing_listing = self.existing_listing.to_dict()
        else:
            existing_listing = self.existing_listing

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
        if mcp_type is not UNSET:
            field_dict["mcp_type"] = mcp_type
        if connection_status is not UNSET:
            field_dict["connection_status"] = connection_status
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id
        if existing_listing is not UNSET:
            field_dict["existing_listing"] = existing_listing

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

        def _parse_mcp_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mcp_type = _parse_mcp_type(d.pop("mcp_type", UNSET))

        connection_status = d.pop("connection_status", UNSET)

        def _parse_datasource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datasource_id_type_0 = UUID(data)

                return datasource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        datasource_id = _parse_datasource_id(d.pop("datasource_id", UNSET))

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

        user_tool_response = cls(
            id=id,
            name=name,
            source=source,
            description=description,
            mcp_type=mcp_type,
            connection_status=connection_status,
            datasource_id=datasource_id,
            existing_listing=existing_listing,
        )

        user_tool_response.additional_properties = d
        return user_tool_response

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
