from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_registry_update_status_type_0 import WebhookRegistryUpdateStatusType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_registry_update_metadata_type_0 import WebhookRegistryUpdateMetadataType0


T = TypeVar("T", bound="WebhookRegistryUpdate")


@_attrs_define
class WebhookRegistryUpdate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        status (None | Unset | WebhookRegistryUpdateStatusType0):
        trigger_agent_id (None | Unset | UUID):
        rate_limit_per_min (int | None | Unset):
        rate_limit_per_hour (int | None | Unset):
        max_payload_bytes (int | None | Unset):
        signature_header_name (None | str | Unset):
        metadata (None | Unset | WebhookRegistryUpdateMetadataType0):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    status: None | Unset | WebhookRegistryUpdateStatusType0 = UNSET
    trigger_agent_id: None | Unset | UUID = UNSET
    rate_limit_per_min: int | None | Unset = UNSET
    rate_limit_per_hour: int | None | Unset = UNSET
    max_payload_bytes: int | None | Unset = UNSET
    signature_header_name: None | str | Unset = UNSET
    metadata: None | Unset | WebhookRegistryUpdateMetadataType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_registry_update_metadata_type_0 import WebhookRegistryUpdateMetadataType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, WebhookRegistryUpdateStatusType0):
            status = self.status.value
        else:
            status = self.status

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

        signature_header_name: None | str | Unset
        if isinstance(self.signature_header_name, Unset):
            signature_header_name = UNSET
        else:
            signature_header_name = self.signature_header_name

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, WebhookRegistryUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
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
        from ..models.webhook_registry_update_metadata_type_0 import WebhookRegistryUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_status(data: object) -> None | Unset | WebhookRegistryUpdateStatusType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = WebhookRegistryUpdateStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookRegistryUpdateStatusType0, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_signature_header_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_header_name = _parse_signature_header_name(d.pop("signature_header_name", UNSET))

        def _parse_metadata(data: object) -> None | Unset | WebhookRegistryUpdateMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = WebhookRegistryUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookRegistryUpdateMetadataType0, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        webhook_registry_update = cls(
            name=name,
            description=description,
            status=status,
            trigger_agent_id=trigger_agent_id,
            rate_limit_per_min=rate_limit_per_min,
            rate_limit_per_hour=rate_limit_per_hour,
            max_payload_bytes=max_payload_bytes,
            signature_header_name=signature_header_name,
            metadata=metadata,
        )

        webhook_registry_update.additional_properties = d
        return webhook_registry_update

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
