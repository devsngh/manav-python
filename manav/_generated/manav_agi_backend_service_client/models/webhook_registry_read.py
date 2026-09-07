from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_registry_read_category import WebhookRegistryReadCategory
from ..models.webhook_registry_read_status import WebhookRegistryReadStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_registry_read_provider_metadata_type_0 import WebhookRegistryReadProviderMetadataType0


T = TypeVar("T", bound="WebhookRegistryRead")


@_attrs_define
class WebhookRegistryRead:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        description (None | str):
        category (WebhookRegistryReadCategory):
        provider (None | str):
        provider_event_type (None | str):
        provider_metadata (None | WebhookRegistryReadProviderMetadataType0):
        handler_type (str):
        workspace_id (None | UUID):
        legacy_ingestion_source_id (None | UUID):
        datasource_id (None | UUID):
        trigger_agent_id (None | UUID):
        secret_algorithm (str):
        secret_rotated_at (datetime.datetime | None):
        signature_header_name (str):
        status (WebhookRegistryReadStatus):
        rate_limit_per_min (int | None):
        rate_limit_per_hour (int | None):
        max_payload_bytes (int | None):
        last_received_at (datetime.datetime | None):
        last_handler_status (None | str):
        last_error (None | str):
        total_received (int):
        total_failed (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        webhook_url (None | str | Unset):
        has_secret (bool | Unset):  Default: False.
    """

    id: UUID
    org_id: UUID
    name: str
    description: None | str
    category: WebhookRegistryReadCategory
    provider: None | str
    provider_event_type: None | str
    provider_metadata: None | WebhookRegistryReadProviderMetadataType0
    handler_type: str
    workspace_id: None | UUID
    legacy_ingestion_source_id: None | UUID
    datasource_id: None | UUID
    trigger_agent_id: None | UUID
    secret_algorithm: str
    secret_rotated_at: datetime.datetime | None
    signature_header_name: str
    status: WebhookRegistryReadStatus
    rate_limit_per_min: int | None
    rate_limit_per_hour: int | None
    max_payload_bytes: int | None
    last_received_at: datetime.datetime | None
    last_handler_status: None | str
    last_error: None | str
    total_received: int
    total_failed: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    webhook_url: None | str | Unset = UNSET
    has_secret: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_registry_read_provider_metadata_type_0 import (
            WebhookRegistryReadProviderMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        description: None | str
        description = self.description

        category = self.category.value

        provider: None | str
        provider = self.provider

        provider_event_type: None | str
        provider_event_type = self.provider_event_type

        provider_metadata: dict[str, Any] | None
        if isinstance(self.provider_metadata, WebhookRegistryReadProviderMetadataType0):
            provider_metadata = self.provider_metadata.to_dict()
        else:
            provider_metadata = self.provider_metadata

        handler_type = self.handler_type

        workspace_id: None | str
        if isinstance(self.workspace_id, UUID):
            workspace_id = str(self.workspace_id)
        else:
            workspace_id = self.workspace_id

        legacy_ingestion_source_id: None | str
        if isinstance(self.legacy_ingestion_source_id, UUID):
            legacy_ingestion_source_id = str(self.legacy_ingestion_source_id)
        else:
            legacy_ingestion_source_id = self.legacy_ingestion_source_id

        datasource_id: None | str
        if isinstance(self.datasource_id, UUID):
            datasource_id = str(self.datasource_id)
        else:
            datasource_id = self.datasource_id

        trigger_agent_id: None | str
        if isinstance(self.trigger_agent_id, UUID):
            trigger_agent_id = str(self.trigger_agent_id)
        else:
            trigger_agent_id = self.trigger_agent_id

        secret_algorithm = self.secret_algorithm

        secret_rotated_at: None | str
        if isinstance(self.secret_rotated_at, datetime.datetime):
            secret_rotated_at = self.secret_rotated_at.isoformat()
        else:
            secret_rotated_at = self.secret_rotated_at

        signature_header_name = self.signature_header_name

        status = self.status.value

        rate_limit_per_min: int | None
        rate_limit_per_min = self.rate_limit_per_min

        rate_limit_per_hour: int | None
        rate_limit_per_hour = self.rate_limit_per_hour

        max_payload_bytes: int | None
        max_payload_bytes = self.max_payload_bytes

        last_received_at: None | str
        if isinstance(self.last_received_at, datetime.datetime):
            last_received_at = self.last_received_at.isoformat()
        else:
            last_received_at = self.last_received_at

        last_handler_status: None | str
        last_handler_status = self.last_handler_status

        last_error: None | str
        last_error = self.last_error

        total_received = self.total_received

        total_failed = self.total_failed

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        webhook_url: None | str | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        else:
            webhook_url = self.webhook_url

        has_secret = self.has_secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "name": name,
                "description": description,
                "category": category,
                "provider": provider,
                "provider_event_type": provider_event_type,
                "provider_metadata": provider_metadata,
                "handler_type": handler_type,
                "workspace_id": workspace_id,
                "legacy_ingestion_source_id": legacy_ingestion_source_id,
                "datasource_id": datasource_id,
                "trigger_agent_id": trigger_agent_id,
                "secret_algorithm": secret_algorithm,
                "secret_rotated_at": secret_rotated_at,
                "signature_header_name": signature_header_name,
                "status": status,
                "rate_limit_per_min": rate_limit_per_min,
                "rate_limit_per_hour": rate_limit_per_hour,
                "max_payload_bytes": max_payload_bytes,
                "last_received_at": last_received_at,
                "last_handler_status": last_handler_status,
                "last_error": last_error,
                "total_received": total_received,
                "total_failed": total_failed,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if has_secret is not UNSET:
            field_dict["has_secret"] = has_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_registry_read_provider_metadata_type_0 import (
            WebhookRegistryReadProviderMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        category = WebhookRegistryReadCategory(d.pop("category"))

        def _parse_provider(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider = _parse_provider(d.pop("provider"))

        def _parse_provider_event_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_event_type = _parse_provider_event_type(d.pop("provider_event_type"))

        def _parse_provider_metadata(data: object) -> None | WebhookRegistryReadProviderMetadataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_metadata_type_0 = WebhookRegistryReadProviderMetadataType0.from_dict(data)

                return provider_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WebhookRegistryReadProviderMetadataType0, data)

        provider_metadata = _parse_provider_metadata(d.pop("provider_metadata"))

        handler_type = d.pop("handler_type")

        def _parse_workspace_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                workspace_id_type_0 = UUID(data)

                return workspace_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        def _parse_legacy_ingestion_source_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legacy_ingestion_source_id_type_0 = UUID(data)

                return legacy_ingestion_source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        legacy_ingestion_source_id = _parse_legacy_ingestion_source_id(d.pop("legacy_ingestion_source_id"))

        def _parse_datasource_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datasource_id_type_0 = UUID(data)

                return datasource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        datasource_id = _parse_datasource_id(d.pop("datasource_id"))

        def _parse_trigger_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trigger_agent_id_type_0 = UUID(data)

                return trigger_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        trigger_agent_id = _parse_trigger_agent_id(d.pop("trigger_agent_id"))

        secret_algorithm = d.pop("secret_algorithm")

        def _parse_secret_rotated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secret_rotated_at_type_0 = datetime.datetime.fromisoformat(data)

                return secret_rotated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        secret_rotated_at = _parse_secret_rotated_at(d.pop("secret_rotated_at"))

        signature_header_name = d.pop("signature_header_name")

        status = WebhookRegistryReadStatus(d.pop("status"))

        def _parse_rate_limit_per_min(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rate_limit_per_min = _parse_rate_limit_per_min(d.pop("rate_limit_per_min"))

        def _parse_rate_limit_per_hour(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rate_limit_per_hour = _parse_rate_limit_per_hour(d.pop("rate_limit_per_hour"))

        def _parse_max_payload_bytes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_payload_bytes = _parse_max_payload_bytes(d.pop("max_payload_bytes"))

        def _parse_last_received_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_received_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_received_at = _parse_last_received_at(d.pop("last_received_at"))

        def _parse_last_handler_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_handler_status = _parse_last_handler_status(d.pop("last_handler_status"))

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("last_error"))

        total_received = d.pop("total_received")

        total_failed = d.pop("total_failed")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_webhook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        webhook_url = _parse_webhook_url(d.pop("webhook_url", UNSET))

        has_secret = d.pop("has_secret", UNSET)

        webhook_registry_read = cls(
            id=id,
            org_id=org_id,
            name=name,
            description=description,
            category=category,
            provider=provider,
            provider_event_type=provider_event_type,
            provider_metadata=provider_metadata,
            handler_type=handler_type,
            workspace_id=workspace_id,
            legacy_ingestion_source_id=legacy_ingestion_source_id,
            datasource_id=datasource_id,
            trigger_agent_id=trigger_agent_id,
            secret_algorithm=secret_algorithm,
            secret_rotated_at=secret_rotated_at,
            signature_header_name=signature_header_name,
            status=status,
            rate_limit_per_min=rate_limit_per_min,
            rate_limit_per_hour=rate_limit_per_hour,
            max_payload_bytes=max_payload_bytes,
            last_received_at=last_received_at,
            last_handler_status=last_handler_status,
            last_error=last_error,
            total_received=total_received,
            total_failed=total_failed,
            created_at=created_at,
            updated_at=updated_at,
            webhook_url=webhook_url,
            has_secret=has_secret,
        )

        webhook_registry_read.additional_properties = d
        return webhook_registry_read

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
