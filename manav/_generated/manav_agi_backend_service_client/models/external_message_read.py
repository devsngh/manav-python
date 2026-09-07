from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.external_message_read_channel_type import ExternalMessageReadChannelType
from ..models.external_message_read_classification_type_0 import ExternalMessageReadClassificationType0
from ..models.external_message_read_direction import ExternalMessageReadDirection
from ..models.external_message_read_status import ExternalMessageReadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalMessageRead")


@_attrs_define
class ExternalMessageRead:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        channel_type (ExternalMessageReadChannelType):
        direction (ExternalMessageReadDirection):
        provider (None | str):
        provider_message_id (None | str):
        thread_id (None | UUID):
        from_address (str):
        from_display_name (None | str):
        to_addresses (list[str]):
        subject (None | str):
        body_text (None | str):
        body_html (None | str):
        sender_dept (None | str):
        sender_agent_id (None | UUID):
        sender_persona_id (None | UUID):
        classification (ExternalMessageReadClassificationType0 | None):
        classification_confidence (float | None):
        routed_to_dept (None | str):
        routed_to_agent_id (None | UUID):
        handled_at (datetime.datetime | None):
        sent_at (datetime.datetime | None):
        received_at (datetime.datetime | None):
        delivered_at (datetime.datetime | None):
        opened_at (datetime.datetime | None):
        first_clicked_at (datetime.datetime | None):
        first_replied_at (datetime.datetime | None):
        bounced_at (datetime.datetime | None):
        status (ExternalMessageReadStatus):
        signature_verified (bool | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        cc_addresses (list[str] | None | Unset):
        bcc_addresses (list[str] | None | Unset):
        reply_to_address (None | str | Unset):
    """

    id: UUID
    org_id: UUID
    channel_type: ExternalMessageReadChannelType
    direction: ExternalMessageReadDirection
    provider: None | str
    provider_message_id: None | str
    thread_id: None | UUID
    from_address: str
    from_display_name: None | str
    to_addresses: list[str]
    subject: None | str
    body_text: None | str
    body_html: None | str
    sender_dept: None | str
    sender_agent_id: None | UUID
    sender_persona_id: None | UUID
    classification: ExternalMessageReadClassificationType0 | None
    classification_confidence: float | None
    routed_to_dept: None | str
    routed_to_agent_id: None | UUID
    handled_at: datetime.datetime | None
    sent_at: datetime.datetime | None
    received_at: datetime.datetime | None
    delivered_at: datetime.datetime | None
    opened_at: datetime.datetime | None
    first_clicked_at: datetime.datetime | None
    first_replied_at: datetime.datetime | None
    bounced_at: datetime.datetime | None
    status: ExternalMessageReadStatus
    signature_verified: bool | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    cc_addresses: list[str] | None | Unset = UNSET
    bcc_addresses: list[str] | None | Unset = UNSET
    reply_to_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        channel_type = self.channel_type.value

        direction = self.direction.value

        provider: None | str
        provider = self.provider

        provider_message_id: None | str
        provider_message_id = self.provider_message_id

        thread_id: None | str
        if isinstance(self.thread_id, UUID):
            thread_id = str(self.thread_id)
        else:
            thread_id = self.thread_id

        from_address = self.from_address

        from_display_name: None | str
        from_display_name = self.from_display_name

        to_addresses = self.to_addresses

        subject: None | str
        subject = self.subject

        body_text: None | str
        body_text = self.body_text

        body_html: None | str
        body_html = self.body_html

        sender_dept: None | str
        sender_dept = self.sender_dept

        sender_agent_id: None | str
        if isinstance(self.sender_agent_id, UUID):
            sender_agent_id = str(self.sender_agent_id)
        else:
            sender_agent_id = self.sender_agent_id

        sender_persona_id: None | str
        if isinstance(self.sender_persona_id, UUID):
            sender_persona_id = str(self.sender_persona_id)
        else:
            sender_persona_id = self.sender_persona_id

        classification: None | str
        if isinstance(self.classification, ExternalMessageReadClassificationType0):
            classification = self.classification.value
        else:
            classification = self.classification

        classification_confidence: float | None
        classification_confidence = self.classification_confidence

        routed_to_dept: None | str
        routed_to_dept = self.routed_to_dept

        routed_to_agent_id: None | str
        if isinstance(self.routed_to_agent_id, UUID):
            routed_to_agent_id = str(self.routed_to_agent_id)
        else:
            routed_to_agent_id = self.routed_to_agent_id

        handled_at: None | str
        if isinstance(self.handled_at, datetime.datetime):
            handled_at = self.handled_at.isoformat()
        else:
            handled_at = self.handled_at

        sent_at: None | str
        if isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        received_at: None | str
        if isinstance(self.received_at, datetime.datetime):
            received_at = self.received_at.isoformat()
        else:
            received_at = self.received_at

        delivered_at: None | str
        if isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        opened_at: None | str
        if isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        first_clicked_at: None | str
        if isinstance(self.first_clicked_at, datetime.datetime):
            first_clicked_at = self.first_clicked_at.isoformat()
        else:
            first_clicked_at = self.first_clicked_at

        first_replied_at: None | str
        if isinstance(self.first_replied_at, datetime.datetime):
            first_replied_at = self.first_replied_at.isoformat()
        else:
            first_replied_at = self.first_replied_at

        bounced_at: None | str
        if isinstance(self.bounced_at, datetime.datetime):
            bounced_at = self.bounced_at.isoformat()
        else:
            bounced_at = self.bounced_at

        status = self.status.value

        signature_verified: bool | None
        signature_verified = self.signature_verified

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cc_addresses: list[str] | None | Unset
        if isinstance(self.cc_addresses, Unset):
            cc_addresses = UNSET
        elif isinstance(self.cc_addresses, list):
            cc_addresses = self.cc_addresses

        else:
            cc_addresses = self.cc_addresses

        bcc_addresses: list[str] | None | Unset
        if isinstance(self.bcc_addresses, Unset):
            bcc_addresses = UNSET
        elif isinstance(self.bcc_addresses, list):
            bcc_addresses = self.bcc_addresses

        else:
            bcc_addresses = self.bcc_addresses

        reply_to_address: None | str | Unset
        if isinstance(self.reply_to_address, Unset):
            reply_to_address = UNSET
        else:
            reply_to_address = self.reply_to_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "channel_type": channel_type,
                "direction": direction,
                "provider": provider,
                "provider_message_id": provider_message_id,
                "thread_id": thread_id,
                "from_address": from_address,
                "from_display_name": from_display_name,
                "to_addresses": to_addresses,
                "subject": subject,
                "body_text": body_text,
                "body_html": body_html,
                "sender_dept": sender_dept,
                "sender_agent_id": sender_agent_id,
                "sender_persona_id": sender_persona_id,
                "classification": classification,
                "classification_confidence": classification_confidence,
                "routed_to_dept": routed_to_dept,
                "routed_to_agent_id": routed_to_agent_id,
                "handled_at": handled_at,
                "sent_at": sent_at,
                "received_at": received_at,
                "delivered_at": delivered_at,
                "opened_at": opened_at,
                "first_clicked_at": first_clicked_at,
                "first_replied_at": first_replied_at,
                "bounced_at": bounced_at,
                "status": status,
                "signature_verified": signature_verified,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if cc_addresses is not UNSET:
            field_dict["cc_addresses"] = cc_addresses
        if bcc_addresses is not UNSET:
            field_dict["bcc_addresses"] = bcc_addresses
        if reply_to_address is not UNSET:
            field_dict["reply_to_address"] = reply_to_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        channel_type = ExternalMessageReadChannelType(d.pop("channel_type"))

        direction = ExternalMessageReadDirection(d.pop("direction"))

        def _parse_provider(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider = _parse_provider(d.pop("provider"))

        def _parse_provider_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_message_id = _parse_provider_message_id(d.pop("provider_message_id"))

        def _parse_thread_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thread_id_type_0 = UUID(data)

                return thread_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        from_address = d.pop("from_address")

        def _parse_from_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        from_display_name = _parse_from_display_name(d.pop("from_display_name"))

        to_addresses = cast(list[str], d.pop("to_addresses"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_body_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body_text = _parse_body_text(d.pop("body_text"))

        def _parse_body_html(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body_html = _parse_body_html(d.pop("body_html"))

        def _parse_sender_dept(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sender_dept = _parse_sender_dept(d.pop("sender_dept"))

        def _parse_sender_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_agent_id_type_0 = UUID(data)

                return sender_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        sender_agent_id = _parse_sender_agent_id(d.pop("sender_agent_id"))

        def _parse_sender_persona_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_persona_id_type_0 = UUID(data)

                return sender_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        sender_persona_id = _parse_sender_persona_id(d.pop("sender_persona_id"))

        def _parse_classification(data: object) -> ExternalMessageReadClassificationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                classification_type_0 = ExternalMessageReadClassificationType0(data)

                return classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExternalMessageReadClassificationType0 | None, data)

        classification = _parse_classification(d.pop("classification"))

        def _parse_classification_confidence(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        classification_confidence = _parse_classification_confidence(d.pop("classification_confidence"))

        def _parse_routed_to_dept(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        routed_to_dept = _parse_routed_to_dept(d.pop("routed_to_dept"))

        def _parse_routed_to_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                routed_to_agent_id_type_0 = UUID(data)

                return routed_to_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        routed_to_agent_id = _parse_routed_to_agent_id(d.pop("routed_to_agent_id"))

        def _parse_handled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                handled_at_type_0 = datetime.datetime.fromisoformat(data)

                return handled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        handled_at = _parse_handled_at(d.pop("handled_at"))

        def _parse_sent_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sent_at = _parse_sent_at(d.pop("sent_at"))

        def _parse_received_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_at_type_0 = datetime.datetime.fromisoformat(data)

                return received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        received_at = _parse_received_at(d.pop("received_at"))

        def _parse_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

        def _parse_opened_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        opened_at = _parse_opened_at(d.pop("opened_at"))

        def _parse_first_clicked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_clicked_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_clicked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        first_clicked_at = _parse_first_clicked_at(d.pop("first_clicked_at"))

        def _parse_first_replied_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_replied_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_replied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        first_replied_at = _parse_first_replied_at(d.pop("first_replied_at"))

        def _parse_bounced_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bounced_at_type_0 = datetime.datetime.fromisoformat(data)

                return bounced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        bounced_at = _parse_bounced_at(d.pop("bounced_at"))

        status = ExternalMessageReadStatus(d.pop("status"))

        def _parse_signature_verified(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        signature_verified = _parse_signature_verified(d.pop("signature_verified"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_cc_addresses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cc_addresses_type_0 = cast(list[str], data)

                return cc_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cc_addresses = _parse_cc_addresses(d.pop("cc_addresses", UNSET))

        def _parse_bcc_addresses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bcc_addresses_type_0 = cast(list[str], data)

                return bcc_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bcc_addresses = _parse_bcc_addresses(d.pop("bcc_addresses", UNSET))

        def _parse_reply_to_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to_address = _parse_reply_to_address(d.pop("reply_to_address", UNSET))

        external_message_read = cls(
            id=id,
            org_id=org_id,
            channel_type=channel_type,
            direction=direction,
            provider=provider,
            provider_message_id=provider_message_id,
            thread_id=thread_id,
            from_address=from_address,
            from_display_name=from_display_name,
            to_addresses=to_addresses,
            subject=subject,
            body_text=body_text,
            body_html=body_html,
            sender_dept=sender_dept,
            sender_agent_id=sender_agent_id,
            sender_persona_id=sender_persona_id,
            classification=classification,
            classification_confidence=classification_confidence,
            routed_to_dept=routed_to_dept,
            routed_to_agent_id=routed_to_agent_id,
            handled_at=handled_at,
            sent_at=sent_at,
            received_at=received_at,
            delivered_at=delivered_at,
            opened_at=opened_at,
            first_clicked_at=first_clicked_at,
            first_replied_at=first_replied_at,
            bounced_at=bounced_at,
            status=status,
            signature_verified=signature_verified,
            created_at=created_at,
            updated_at=updated_at,
            cc_addresses=cc_addresses,
            bcc_addresses=bcc_addresses,
            reply_to_address=reply_to_address,
        )

        external_message_read.additional_properties = d
        return external_message_read

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
