from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_send_request_metadata_type_0 import EmailSendRequestMetadataType0


T = TypeVar("T", bound="EmailSendRequest")


@_attrs_define
class EmailSendRequest:
    """High-level send request — provider is resolved via Datasource.

    Attributes:
        to (list[str]):
        subject (str):
        body_text (None | str | Unset):
        body_html (None | str | Unset):
        cc (list[str] | None | Unset):
        bcc (list[str] | None | Unset):
        reply_to (None | str | Unset):
        from_persona_id (None | Unset | UUID): If set, picks the Datasource owned by this persona. Otherwise uses org's
            marketing default.
        source_dept (str | Unset):  Default: 'generic'.
        source_agent_id (None | Unset | UUID):
        source_user_id (None | Unset | UUID):
        source_campaign_id (None | Unset | UUID):
        source_task_id (None | Unset | UUID):
        source_template_id (None | Unset | UUID):
        reply_to_thread_id (None | Unset | UUID):
        attachment_asset_ids (list[UUID] | None | Unset):
        schedule_at (datetime.datetime | None | Unset):
        metadata (EmailSendRequestMetadataType0 | None | Unset):
    """

    to: list[str]
    subject: str
    body_text: None | str | Unset = UNSET
    body_html: None | str | Unset = UNSET
    cc: list[str] | None | Unset = UNSET
    bcc: list[str] | None | Unset = UNSET
    reply_to: None | str | Unset = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    source_dept: str | Unset = "generic"
    source_agent_id: None | Unset | UUID = UNSET
    source_user_id: None | Unset | UUID = UNSET
    source_campaign_id: None | Unset | UUID = UNSET
    source_task_id: None | Unset | UUID = UNSET
    source_template_id: None | Unset | UUID = UNSET
    reply_to_thread_id: None | Unset | UUID = UNSET
    attachment_asset_ids: list[UUID] | None | Unset = UNSET
    schedule_at: datetime.datetime | None | Unset = UNSET
    metadata: EmailSendRequestMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.email_send_request_metadata_type_0 import EmailSendRequestMetadataType0  # noqa: PLC0415

        to = self.to

        subject = self.subject

        body_text: None | str | Unset
        if isinstance(self.body_text, Unset):
            body_text = UNSET
        else:
            body_text = self.body_text

        body_html: None | str | Unset
        if isinstance(self.body_html, Unset):
            body_html = UNSET
        else:
            body_html = self.body_html

        cc: list[str] | None | Unset
        if isinstance(self.cc, Unset):
            cc = UNSET
        elif isinstance(self.cc, list):
            cc = self.cc

        else:
            cc = self.cc

        bcc: list[str] | None | Unset
        if isinstance(self.bcc, Unset):
            bcc = UNSET
        elif isinstance(self.bcc, list):
            bcc = self.bcc

        else:
            bcc = self.bcc

        reply_to: None | str | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

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

        source_template_id: None | str | Unset
        if isinstance(self.source_template_id, Unset):
            source_template_id = UNSET
        elif isinstance(self.source_template_id, UUID):
            source_template_id = str(self.source_template_id)
        else:
            source_template_id = self.source_template_id

        reply_to_thread_id: None | str | Unset
        if isinstance(self.reply_to_thread_id, Unset):
            reply_to_thread_id = UNSET
        elif isinstance(self.reply_to_thread_id, UUID):
            reply_to_thread_id = str(self.reply_to_thread_id)
        else:
            reply_to_thread_id = self.reply_to_thread_id

        attachment_asset_ids: list[str] | None | Unset
        if isinstance(self.attachment_asset_ids, Unset):
            attachment_asset_ids = UNSET
        elif isinstance(self.attachment_asset_ids, list):
            attachment_asset_ids = []
            for attachment_asset_ids_type_0_item_data in self.attachment_asset_ids:
                attachment_asset_ids_type_0_item = str(attachment_asset_ids_type_0_item_data)
                attachment_asset_ids.append(attachment_asset_ids_type_0_item)

        else:
            attachment_asset_ids = self.attachment_asset_ids

        schedule_at: None | str | Unset
        if isinstance(self.schedule_at, Unset):
            schedule_at = UNSET
        elif isinstance(self.schedule_at, datetime.datetime):
            schedule_at = self.schedule_at.isoformat()
        else:
            schedule_at = self.schedule_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, EmailSendRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
                "subject": subject,
            }
        )
        if body_text is not UNSET:
            field_dict["body_text"] = body_text
        if body_html is not UNSET:
            field_dict["body_html"] = body_html
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
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
        if source_template_id is not UNSET:
            field_dict["source_template_id"] = source_template_id
        if reply_to_thread_id is not UNSET:
            field_dict["reply_to_thread_id"] = reply_to_thread_id
        if attachment_asset_ids is not UNSET:
            field_dict["attachment_asset_ids"] = attachment_asset_ids
        if schedule_at is not UNSET:
            field_dict["schedule_at"] = schedule_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_send_request_metadata_type_0 import EmailSendRequestMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        to = cast(list[str], d.pop("to"))

        subject = d.pop("subject")

        def _parse_body_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_text = _parse_body_text(d.pop("body_text", UNSET))

        def _parse_body_html(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_html = _parse_body_html(d.pop("body_html", UNSET))

        def _parse_cc(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cc_type_0 = cast(list[str], data)

                return cc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cc = _parse_cc(d.pop("cc", UNSET))

        def _parse_bcc(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bcc_type_0 = cast(list[str], data)

                return bcc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bcc = _parse_bcc(d.pop("bcc", UNSET))

        def _parse_reply_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

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

        def _parse_source_template_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_template_id_type_0 = UUID(data)

                return source_template_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_template_id = _parse_source_template_id(d.pop("source_template_id", UNSET))

        def _parse_reply_to_thread_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reply_to_thread_id_type_0 = UUID(data)

                return reply_to_thread_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reply_to_thread_id = _parse_reply_to_thread_id(d.pop("reply_to_thread_id", UNSET))

        def _parse_attachment_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachment_asset_ids_type_0 = []
                _attachment_asset_ids_type_0 = data
                for attachment_asset_ids_type_0_item_data in _attachment_asset_ids_type_0:
                    attachment_asset_ids_type_0_item = UUID(attachment_asset_ids_type_0_item_data)

                    attachment_asset_ids_type_0.append(attachment_asset_ids_type_0_item)

                return attachment_asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        attachment_asset_ids = _parse_attachment_asset_ids(d.pop("attachment_asset_ids", UNSET))

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

        def _parse_metadata(data: object) -> EmailSendRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EmailSendRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmailSendRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        email_send_request = cls(
            to=to,
            subject=subject,
            body_text=body_text,
            body_html=body_html,
            cc=cc,
            bcc=bcc,
            reply_to=reply_to,
            from_persona_id=from_persona_id,
            source_dept=source_dept,
            source_agent_id=source_agent_id,
            source_user_id=source_user_id,
            source_campaign_id=source_campaign_id,
            source_task_id=source_task_id,
            source_template_id=source_template_id,
            reply_to_thread_id=reply_to_thread_id,
            attachment_asset_ids=attachment_asset_ids,
            schedule_at=schedule_at,
            metadata=metadata,
        )

        email_send_request.additional_properties = d
        return email_send_request

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
