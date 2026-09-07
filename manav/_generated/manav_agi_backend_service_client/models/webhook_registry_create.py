from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_registry_create_category import WebhookRegistryCreateCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_registry_create_metadata_type_0 import WebhookRegistryCreateMetadataType0
    from ..models.webhook_registry_create_provider_metadata_type_0 import WebhookRegistryCreateProviderMetadataType0


T = TypeVar("T", bound="WebhookRegistryCreate")


@_attrs_define
class WebhookRegistryCreate:
    """
    Attributes:
        name (str):
        category (WebhookRegistryCreateCategory):
        description (None | str | Unset):
        provider (None | str | Unset):
        provider_event_type (None | str | Unset):
        provider_metadata (None | Unset | WebhookRegistryCreateProviderMetadataType0):
        handler_type (None | str | Unset): Override default handler from HANDLERS registry. Usually leave None.
        org_id (None | Unset | UUID):
        workspace_id (None | Unset | UUID):
        legacy_ingestion_source_id (None | Unset | UUID):
        datasource_id (None | Unset | UUID):
        trigger_agent_id (None | Unset | UUID):
        rate_limit_per_min (int | None | Unset):
        rate_limit_per_hour (int | None | Unset):
        max_payload_bytes (int | None | Unset):
        signature_header_name (str | Unset):  Default: 'X-Platform-Signature'.
        metadata (None | Unset | WebhookRegistryCreateMetadataType0):
    """

    name: str
    category: WebhookRegistryCreateCategory
    description: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    provider_event_type: None | str | Unset = UNSET
    provider_metadata: None | Unset | WebhookRegistryCreateProviderMetadataType0 = UNSET
    handler_type: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    workspace_id: None | Unset | UUID = UNSET
    legacy_ingestion_source_id: None | Unset | UUID = UNSET
    datasource_id: None | Unset | UUID = UNSET
    trigger_agent_id: None | Unset | UUID = UNSET
    rate_limit_per_min: int | None | Unset = UNSET
    rate_limit_per_hour: int | None | Unset = UNSET
    max_payload_bytes: int | None | Unset = UNSET
    signature_header_name: str | Unset = "X-Platform-Signature"
    metadata: None | Unset | WebhookRegistryCreateMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_registry_create_metadata_type_0 import WebhookRegistryCreateMetadataType0  # noqa: PLC0415
        from ..models.webhook_registry_create_provider_metadata_type_0 import (
            WebhookRegistryCreateProviderMetadataType0,  # noqa: PLC0415
        )

        name = self.name

        category = self.category.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        provider_event_type: None | str | Unset
        if isinstance(self.provider_event_type, Unset):
            provider_event_type = UNSET
        else:
            provider_event_type = self.provider_event_type

        provider_metadata: dict[str, Any] | None | Unset
        if isinstance(self.provider_metadata, Unset):
            provider_metadata = UNSET
        elif isinstance(self.provider_metadata, WebhookRegistryCreateProviderMetadataType0):
            provider_metadata = self.provider_metadata.to_dict()
        else:
            provider_metadata = self.provider_metadata

        handler_type: None | str | Unset
        if isinstance(self.handler_type, Unset):
            handler_type = UNSET
        else:
            handler_type = self.handler_type

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        workspace_id: None | str | Unset
        if isinstance(self.workspace_id, Unset):
            workspace_id = UNSET
        elif isinstance(self.workspace_id, UUID):
            workspace_id = str(self.workspace_id)
        else:
            workspace_id = self.workspace_id

        legacy_ingestion_source_id: None | str | Unset
        if isinstance(self.legacy_ingestion_source_id, Unset):
            legacy_ingestion_source_id = UNSET
        elif isinstance(self.legacy_ingestion_source_id, UUID):
            legacy_ingestion_source_id = str(self.legacy_ingestion_source_id)
        else:
            legacy_ingestion_source_id = self.legacy_ingestion_source_id

        datasource_id: None | str | Unset
        if isinstance(self.datasource_id, Unset):
            datasource_id = UNSET
        elif isinstance(self.datasource_id, UUID):
            datasource_id = str(self.datasource_id)
        else:
            datasource_id = self.datasource_id

        trigger_agent_id: None | str | Unset
        if isinstance(self.trigger_agent_id, Unset):
            trigger_agent_id = UNSET
        elif isinstance(self.trigger_agent_id, UUID):
            trigger_agent_id = str(self.trigger_agent_id)
        else:
            trigger_agent_id = self.trigger_agent_id

        rate_limit_per_min: int | None | Unset
        if isinstance(self.rate_limit_per_min, Unset):
            rate_limit_per_min = UNSET
        else:
            rate_limit_per_min = self.rate_limit_per_min

        rate_limit_per_hour: int | None | Unset
        if isinstance(self.rate_limit_per_hour, Unset):
            rate_limit_per_hour = UNSET
        else:
            rate_limit_per_hour = self.rate_limit_per_hour

        max_payload_bytes: int | None | Unset
        if isinstance(self.max_payload_bytes, Unset):
            max_payload_bytes = UNSET
        else:
            max_payload_bytes = self.max_payload_bytes

        signature_header_name = self.signature_header_name

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WebhookRegistryCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "category": category,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_event_type is not UNSET:
            field_dict["provider_event_type"] = provider_event_type
        if provider_metadata is not UNSET:
            field_dict["provider_metadata"] = provider_metadata
        if handler_type is not UNSET:
            field_dict["handler_type"] = handler_type
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id
        if legacy_ingestion_source_id is not UNSET:
            field_dict["legacy_ingestion_source_id"] = legacy_ingestion_source_id
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id
        if trigger_agent_id is not UNSET:
            field_dict["trigger_agent_id"] = trigger_agent_id
        if rate_limit_per_min is not UNSET:
            field_dict["rate_limit_per_min"] = rate_limit_per_min
        if rate_limit_per_hour is not UNSET:
            field_dict["rate_limit_per_hour"] = rate_limit_per_hour
        if max_payload_bytes is not UNSET:
            field_dict["max_payload_bytes"] = max_payload_bytes
        if signature_header_name is not UNSET:
            field_dict["signature_header_name"] = signature_header_name
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_registry_create_metadata_type_0 import WebhookRegistryCreateMetadataType0  # noqa: PLC0415
        from ..models.webhook_registry_create_provider_metadata_type_0 import (
            WebhookRegistryCreateProviderMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        category = WebhookRegistryCreateCategory(d.pop("category"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_provider_event_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_event_type = _parse_provider_event_type(d.pop("provider_event_type", UNSET))

        def _parse_provider_metadata(data: object) -> None | Unset | WebhookRegistryCreateProviderMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_metadata_type_0 = WebhookRegistryCreateProviderMetadataType0.from_dict(data)

                return provider_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookRegistryCreateProviderMetadataType0, data)

        provider_metadata = _parse_provider_metadata(d.pop("provider_metadata", UNSET))

        def _parse_handler_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        handler_type = _parse_handler_type(d.pop("handler_type", UNSET))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_workspace_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_id_type_0 = UUID(data)

                return workspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id", UNSET))

        def _parse_legacy_ingestion_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legacy_ingestion_source_id_type_0 = UUID(data)

                return legacy_ingestion_source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        legacy_ingestion_source_id = _parse_legacy_ingestion_source_id(d.pop("legacy_ingestion_source_id", UNSET))

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

        def _parse_trigger_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_agent_id_type_0 = UUID(data)

                return trigger_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        trigger_agent_id = _parse_trigger_agent_id(d.pop("trigger_agent_id", UNSET))

        def _parse_rate_limit_per_min(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_per_min = _parse_rate_limit_per_min(d.pop("rate_limit_per_min", UNSET))

        def _parse_rate_limit_per_hour(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rate_limit_per_hour = _parse_rate_limit_per_hour(d.pop("rate_limit_per_hour", UNSET))

        def _parse_max_payload_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_payload_bytes = _parse_max_payload_bytes(d.pop("max_payload_bytes", UNSET))

        signature_header_name = d.pop("signature_header_name", UNSET)

        def _parse_metadata(data: object) -> None | Unset | WebhookRegistryCreateMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WebhookRegistryCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookRegistryCreateMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        webhook_registry_create = cls(
            name=name,
            category=category,
            description=description,
            provider=provider,
            provider_event_type=provider_event_type,
            provider_metadata=provider_metadata,
            handler_type=handler_type,
            org_id=org_id,
            workspace_id=workspace_id,
            legacy_ingestion_source_id=legacy_ingestion_source_id,
            datasource_id=datasource_id,
            trigger_agent_id=trigger_agent_id,
            rate_limit_per_min=rate_limit_per_min,
            rate_limit_per_hour=rate_limit_per_hour,
            max_payload_bytes=max_payload_bytes,
            signature_header_name=signature_header_name,
            metadata=metadata,
        )

        webhook_registry_create.additional_properties = d
        return webhook_registry_create

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
