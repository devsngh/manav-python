from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_send_request_metadata_type_0 import SmsSendRequestMetadataType0


T = TypeVar("T", bound="SmsSendRequest")


@_attrs_define
class SmsSendRequest:
    """
    Attributes:
        to (str): E.164 destination phone number (e.g. +15551234567)
        body (str):
        from_number (None | str | Unset): Override the datasource's default sms_from_number
        media_urls (list[str] | None | Unset):
        schedule_at (datetime.datetime | None | Unset):
        from_persona_id (None | Unset | UUID):
        source_dept (str | Unset):  Default: 'generic'.
        source_agent_id (None | Unset | UUID):
        source_user_id (None | Unset | UUID):
        source_campaign_id (None | Unset | UUID):
        source_task_id (None | Unset | UUID):
        explicit_datasource_id (None | Unset | UUID):
        metadata (None | SmsSendRequestMetadataType0 | Unset):
    """

    to: str
    body: str
    from_number: None | str | Unset = UNSET
    media_urls: list[str] | None | Unset = UNSET
    schedule_at: datetime.datetime | None | Unset = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    source_dept: str | Unset = "generic"
    source_agent_id: None | Unset | UUID = UNSET
    source_user_id: None | Unset | UUID = UNSET
    source_campaign_id: None | Unset | UUID = UNSET
    source_task_id: None | Unset | UUID = UNSET
    explicit_datasource_id: None | Unset | UUID = UNSET
    metadata: None | SmsSendRequestMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sms_send_request_metadata_type_0 import SmsSendRequestMetadataType0  # noqa: PLC0415

        to = self.to

        body = self.body

        from_number: None | str | Unset
        if isinstance(self.from_number, Unset):
            from_number = UNSET
        else:
            from_number = self.from_number

        media_urls: list[str] | None | Unset
        if isinstance(self.media_urls, Unset):
            media_urls = UNSET
        elif isinstance(self.media_urls, list):
            media_urls = self.media_urls

        else:
            media_urls = self.media_urls

        schedule_at: None | str | Unset
        if isinstance(self.schedule_at, Unset):
            schedule_at = UNSET
        elif isinstance(self.schedule_at, datetime.datetime):
            schedule_at = self.schedule_at.isoformat()
        else:
            schedule_at = self.schedule_at

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        source_dept = self.source_dept

        source_agent_id: None | str | Unset
        if isinstance(self.source_agent_id, Unset):
            source_agent_id = UNSET
        elif isinstance(self.source_agent_id, UUID):
            source_agent_id = str(self.source_agent_id)
        else:
            source_agent_id = self.source_agent_id

        source_user_id: None | str | Unset
        if isinstance(self.source_user_id, Unset):
            source_user_id = UNSET
        elif isinstance(self.source_user_id, UUID):
            source_user_id = str(self.source_user_id)
        else:
            source_user_id = self.source_user_id

        source_campaign_id: None | str | Unset
        if isinstance(self.source_campaign_id, Unset):
            source_campaign_id = UNSET
        elif isinstance(self.source_campaign_id, UUID):
            source_campaign_id = str(self.source_campaign_id)
        else:
            source_campaign_id = self.source_campaign_id

        source_task_id: None | str | Unset
        if isinstance(self.source_task_id, Unset):
            source_task_id = UNSET
        elif isinstance(self.source_task_id, UUID):
            source_task_id = str(self.source_task_id)
        else:
            source_task_id = self.source_task_id

        explicit_datasource_id: None | str | Unset
        if isinstance(self.explicit_datasource_id, Unset):
            explicit_datasource_id = UNSET
        elif isinstance(self.explicit_datasource_id, UUID):
            explicit_datasource_id = str(self.explicit_datasource_id)
        else:
            explicit_datasource_id = self.explicit_datasource_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SmsSendRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
                "body": body,
            }
        )
        if from_number is not UNSET:
            field_dict["from_number"] = from_number
        if media_urls is not UNSET:
            field_dict["media_urls"] = media_urls
        if schedule_at is not UNSET:
            field_dict["schedule_at"] = schedule_at
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if source_dept is not UNSET:
            field_dict["source_dept"] = source_dept
        if source_agent_id is not UNSET:
            field_dict["source_agent_id"] = source_agent_id
        if source_user_id is not UNSET:
            field_dict["source_user_id"] = source_user_id
        if source_campaign_id is not UNSET:
            field_dict["source_campaign_id"] = source_campaign_id
        if source_task_id is not UNSET:
            field_dict["source_task_id"] = source_task_id
        if explicit_datasource_id is not UNSET:
            field_dict["explicit_datasource_id"] = explicit_datasource_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sms_send_request_metadata_type_0 import SmsSendRequestMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        to = d.pop("to")

        body = d.pop("body")

        def _parse_from_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_number = _parse_from_number(d.pop("from_number", UNSET))

        def _parse_media_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_urls_type_0 = cast(list[str], data)

                return media_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        media_urls = _parse_media_urls(d.pop("media_urls", UNSET))

        def _parse_schedule_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_at_type_0 = datetime.datetime.fromisoformat(data)

                return schedule_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        schedule_at = _parse_schedule_at(d.pop("schedule_at", UNSET))

        def _parse_from_persona_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_persona_id_type_0 = UUID(data)

                return from_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        from_persona_id = _parse_from_persona_id(d.pop("from_persona_id", UNSET))

        source_dept = d.pop("source_dept", UNSET)

        def _parse_source_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_agent_id_type_0 = UUID(data)

                return source_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_agent_id = _parse_source_agent_id(d.pop("source_agent_id", UNSET))

        def _parse_source_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_user_id_type_0 = UUID(data)

                return source_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_user_id = _parse_source_user_id(d.pop("source_user_id", UNSET))

        def _parse_source_campaign_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_campaign_id_type_0 = UUID(data)

                return source_campaign_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_campaign_id = _parse_source_campaign_id(d.pop("source_campaign_id", UNSET))

        def _parse_source_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_task_id_type_0 = UUID(data)

                return source_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_task_id = _parse_source_task_id(d.pop("source_task_id", UNSET))

        def _parse_explicit_datasource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                explicit_datasource_id_type_0 = UUID(data)

                return explicit_datasource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        explicit_datasource_id = _parse_explicit_datasource_id(d.pop("explicit_datasource_id", UNSET))

        def _parse_metadata(data: object) -> None | SmsSendRequestMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SmsSendRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SmsSendRequestMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        sms_send_request = cls(
            to=to,
            body=body,
            from_number=from_number,
            media_urls=media_urls,
            schedule_at=schedule_at,
            from_persona_id=from_persona_id,
            source_dept=source_dept,
            source_agent_id=source_agent_id,
            source_user_id=source_user_id,
            source_campaign_id=source_campaign_id,
            source_task_id=source_task_id,
            explicit_datasource_id=explicit_datasource_id,
            metadata=metadata,
        )

        sms_send_request.additional_properties = d
        return sms_send_request

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
