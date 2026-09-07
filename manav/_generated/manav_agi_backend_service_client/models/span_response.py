from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_response_attributes_type_0 import SpanResponseAttributesType0


T = TypeVar("T", bound="SpanResponse")


@_attrs_define
class SpanResponse:
    """
    Attributes:
        id (UUID):
        trace_id (str):
        operation (str):
        kind (str):
        service (str):
        start_time (datetime.datetime):
        status (str):
        depth (int):
        parent_id (None | Unset | UUID):
        end_time (datetime.datetime | None | Unset):
        duration_ms (float | None | Unset):
        status_code (int | None | Unset):
        method (None | str | Unset):
        path (None | str | Unset):
        user_id (None | Unset | UUID):
        error_type (None | str | Unset):
        error_message (None | str | Unset):
        attributes (None | SpanResponseAttributesType0 | Unset):
        subject_type (None | str | Unset):
        subject_id (None | Unset | UUID):
        story_bucket (list[str] | Unset):
        caused_by_span_id (None | Unset | UUID):
        caused_by_reasoning_excerpt (None | str | Unset):
        triggered_span_ids (list[str] | Unset):
        dept_id (None | Unset | UUID):
        dept_path (None | str | Unset):
        dept_from (None | Unset | UUID):
        dept_to (None | Unset | UUID):
        error_signature (None | str | Unset):
        endpoint_pattern (None | str | Unset):
        org_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        dialogue_id (None | Unset | UUID):
        source_type (None | str | Unset):
        source_id (None | Unset | UUID):
        category (None | str | Unset):
        initiator_kind (None | str | Unset):
        initiator_bot_id (None | Unset | UUID):
        initiator_user_id (None | Unset | UUID):
    """

    id: UUID
    trace_id: str
    operation: str
    kind: str
    service: str
    start_time: datetime.datetime
    status: str
    depth: int
    parent_id: None | Unset | UUID = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    status_code: int | None | Unset = UNSET
    method: None | str | Unset = UNSET
    path: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    error_type: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    attributes: None | SpanResponseAttributesType0 | Unset = UNSET
    subject_type: None | str | Unset = UNSET
    subject_id: None | Unset | UUID = UNSET
    story_bucket: list[str] | Unset = UNSET
    caused_by_span_id: None | Unset | UUID = UNSET
    caused_by_reasoning_excerpt: None | str | Unset = UNSET
    triggered_span_ids: list[str] | Unset = UNSET
    dept_id: None | Unset | UUID = UNSET
    dept_path: None | str | Unset = UNSET
    dept_from: None | Unset | UUID = UNSET
    dept_to: None | Unset | UUID = UNSET
    error_signature: None | str | Unset = UNSET
    endpoint_pattern: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    bot_id: None | Unset | UUID = UNSET
    dialogue_id: None | Unset | UUID = UNSET
    source_type: None | str | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    category: None | str | Unset = UNSET
    initiator_kind: None | str | Unset = UNSET
    initiator_bot_id: None | Unset | UUID = UNSET
    initiator_user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.span_response_attributes_type_0 import SpanResponseAttributesType0  # noqa: PLC0415

        id = str(self.id)

        trace_id = self.trace_id

        operation = self.operation

        kind = self.kind

        service = self.service

        start_time = self.start_time.isoformat()

        status = self.status

        depth = self.depth

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        duration_ms: float | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        method: None | str | Unset
        if isinstance(self.method, Unset):
            method = UNSET
        else:
            method = self.method

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        error_type: None | str | Unset
        if isinstance(self.error_type, Unset):
            error_type = UNSET
        else:
            error_type = self.error_type

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        attributes: dict[str, Any] | None | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, SpanResponseAttributesType0):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes

        subject_type: None | str | Unset
        if isinstance(self.subject_type, Unset):
            subject_type = UNSET
        else:
            subject_type = self.subject_type

        subject_id: None | str | Unset
        if isinstance(self.subject_id, Unset):
            subject_id = UNSET
        elif isinstance(self.subject_id, UUID):
            subject_id = str(self.subject_id)
        else:
            subject_id = self.subject_id

        story_bucket: list[str] | Unset = UNSET
        if not isinstance(self.story_bucket, Unset):
            story_bucket = self.story_bucket

        caused_by_span_id: None | str | Unset
        if isinstance(self.caused_by_span_id, Unset):
            caused_by_span_id = UNSET
        elif isinstance(self.caused_by_span_id, UUID):
            caused_by_span_id = str(self.caused_by_span_id)
        else:
            caused_by_span_id = self.caused_by_span_id

        caused_by_reasoning_excerpt: None | str | Unset
        if isinstance(self.caused_by_reasoning_excerpt, Unset):
            caused_by_reasoning_excerpt = UNSET
        else:
            caused_by_reasoning_excerpt = self.caused_by_reasoning_excerpt

        triggered_span_ids: list[str] | Unset = UNSET
        if not isinstance(self.triggered_span_ids, Unset):
            triggered_span_ids = self.triggered_span_ids

        dept_id: None | str | Unset
        if isinstance(self.dept_id, Unset):
            dept_id = UNSET
        elif isinstance(self.dept_id, UUID):
            dept_id = str(self.dept_id)
        else:
            dept_id = self.dept_id

        dept_path: None | str | Unset
        if isinstance(self.dept_path, Unset):
            dept_path = UNSET
        else:
            dept_path = self.dept_path

        dept_from: None | str | Unset
        if isinstance(self.dept_from, Unset):
            dept_from = UNSET
        elif isinstance(self.dept_from, UUID):
            dept_from = str(self.dept_from)
        else:
            dept_from = self.dept_from

        dept_to: None | str | Unset
        if isinstance(self.dept_to, Unset):
            dept_to = UNSET
        elif isinstance(self.dept_to, UUID):
            dept_to = str(self.dept_to)
        else:
            dept_to = self.dept_to

        error_signature: None | str | Unset
        if isinstance(self.error_signature, Unset):
            error_signature = UNSET
        else:
            error_signature = self.error_signature

        endpoint_pattern: None | str | Unset
        if isinstance(self.endpoint_pattern, Unset):
            endpoint_pattern = UNSET
        else:
            endpoint_pattern = self.endpoint_pattern

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        dialogue_id: None | str | Unset
        if isinstance(self.dialogue_id, Unset):
            dialogue_id = UNSET
        elif isinstance(self.dialogue_id, UUID):
            dialogue_id = str(self.dialogue_id)
        else:
            dialogue_id = self.dialogue_id

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        source_id: None | str | Unset
        if isinstance(self.source_id, Unset):
            source_id = UNSET
        elif isinstance(self.source_id, UUID):
            source_id = str(self.source_id)
        else:
            source_id = self.source_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        initiator_kind: None | str | Unset
        if isinstance(self.initiator_kind, Unset):
            initiator_kind = UNSET
        else:
            initiator_kind = self.initiator_kind

        initiator_bot_id: None | str | Unset
        if isinstance(self.initiator_bot_id, Unset):
            initiator_bot_id = UNSET
        elif isinstance(self.initiator_bot_id, UUID):
            initiator_bot_id = str(self.initiator_bot_id)
        else:
            initiator_bot_id = self.initiator_bot_id

        initiator_user_id: None | str | Unset
        if isinstance(self.initiator_user_id, Unset):
            initiator_user_id = UNSET
        elif isinstance(self.initiator_user_id, UUID):
            initiator_user_id = str(self.initiator_user_id)
        else:
            initiator_user_id = self.initiator_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "trace_id": trace_id,
                "operation": operation,
                "kind": kind,
                "service": service,
                "start_time": start_time,
                "status": status,
                "depth": depth,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if subject_type is not UNSET:
            field_dict["subject_type"] = subject_type
        if subject_id is not UNSET:
            field_dict["subject_id"] = subject_id
        if story_bucket is not UNSET:
            field_dict["story_bucket"] = story_bucket
        if caused_by_span_id is not UNSET:
            field_dict["caused_by_span_id"] = caused_by_span_id
        if caused_by_reasoning_excerpt is not UNSET:
            field_dict["caused_by_reasoning_excerpt"] = caused_by_reasoning_excerpt
        if triggered_span_ids is not UNSET:
            field_dict["triggered_span_ids"] = triggered_span_ids
        if dept_id is not UNSET:
            field_dict["dept_id"] = dept_id
        if dept_path is not UNSET:
            field_dict["dept_path"] = dept_path
        if dept_from is not UNSET:
            field_dict["dept_from"] = dept_from
        if dept_to is not UNSET:
            field_dict["dept_to"] = dept_to
        if error_signature is not UNSET:
            field_dict["error_signature"] = error_signature
        if endpoint_pattern is not UNSET:
            field_dict["endpoint_pattern"] = endpoint_pattern
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if dialogue_id is not UNSET:
            field_dict["dialogue_id"] = dialogue_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if category is not UNSET:
            field_dict["category"] = category
        if initiator_kind is not UNSET:
            field_dict["initiator_kind"] = initiator_kind
        if initiator_bot_id is not UNSET:
            field_dict["initiator_bot_id"] = initiator_bot_id
        if initiator_user_id is not UNSET:
            field_dict["initiator_user_id"] = initiator_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_response_attributes_type_0 import SpanResponseAttributesType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        trace_id = d.pop("trace_id")

        operation = d.pop("operation")

        kind = d.pop("kind")

        service = d.pop("service")

        start_time = datetime.datetime.fromisoformat(d.pop("start_time"))

        status = d.pop("status")

        depth = d.pop("depth")

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_duration_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("status_code", UNSET))

        def _parse_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        method = _parse_method(d.pop("method", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_error_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_type = _parse_error_type(d.pop("error_type", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_attributes(data: object) -> None | SpanResponseAttributesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = SpanResponseAttributesType0.from_dict(data)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpanResponseAttributesType0 | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        def _parse_subject_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_type = _parse_subject_type(d.pop("subject_type", UNSET))

        def _parse_subject_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_id_type_0 = UUID(data)

                return subject_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subject_id = _parse_subject_id(d.pop("subject_id", UNSET))

        story_bucket = cast(list[str], d.pop("story_bucket", UNSET))

        def _parse_caused_by_span_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                caused_by_span_id_type_0 = UUID(data)

                return caused_by_span_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        caused_by_span_id = _parse_caused_by_span_id(d.pop("caused_by_span_id", UNSET))

        def _parse_caused_by_reasoning_excerpt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caused_by_reasoning_excerpt = _parse_caused_by_reasoning_excerpt(d.pop("caused_by_reasoning_excerpt", UNSET))

        triggered_span_ids = cast(list[str], d.pop("triggered_span_ids", UNSET))

        def _parse_dept_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dept_id_type_0 = UUID(data)

                return dept_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dept_id = _parse_dept_id(d.pop("dept_id", UNSET))

        def _parse_dept_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dept_path = _parse_dept_path(d.pop("dept_path", UNSET))

        def _parse_dept_from(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dept_from_type_0 = UUID(data)

                return dept_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dept_from = _parse_dept_from(d.pop("dept_from", UNSET))

        def _parse_dept_to(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dept_to_type_0 = UUID(data)

                return dept_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dept_to = _parse_dept_to(d.pop("dept_to", UNSET))

        def _parse_error_signature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_signature = _parse_error_signature(d.pop("error_signature", UNSET))

        def _parse_endpoint_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint_pattern = _parse_endpoint_pattern(d.pop("endpoint_pattern", UNSET))

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

        def _parse_dialogue_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dialogue_id_type_0 = UUID(data)

                return dialogue_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dialogue_id = _parse_dialogue_id(d.pop("dialogue_id", UNSET))

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_source_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_id_type_0 = UUID(data)

                return source_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_id = _parse_source_id(d.pop("source_id", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_initiator_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiator_kind = _parse_initiator_kind(d.pop("initiator_kind", UNSET))

        def _parse_initiator_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initiator_bot_id_type_0 = UUID(data)

                return initiator_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        initiator_bot_id = _parse_initiator_bot_id(d.pop("initiator_bot_id", UNSET))

        def _parse_initiator_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initiator_user_id_type_0 = UUID(data)

                return initiator_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        initiator_user_id = _parse_initiator_user_id(d.pop("initiator_user_id", UNSET))

        span_response = cls(
            id=id,
            trace_id=trace_id,
            operation=operation,
            kind=kind,
            service=service,
            start_time=start_time,
            status=status,
            depth=depth,
            parent_id=parent_id,
            end_time=end_time,
            duration_ms=duration_ms,
            status_code=status_code,
            method=method,
            path=path,
            user_id=user_id,
            error_type=error_type,
            error_message=error_message,
            attributes=attributes,
            subject_type=subject_type,
            subject_id=subject_id,
            story_bucket=story_bucket,
            caused_by_span_id=caused_by_span_id,
            caused_by_reasoning_excerpt=caused_by_reasoning_excerpt,
            triggered_span_ids=triggered_span_ids,
            dept_id=dept_id,
            dept_path=dept_path,
            dept_from=dept_from,
            dept_to=dept_to,
            error_signature=error_signature,
            endpoint_pattern=endpoint_pattern,
            org_id=org_id,
            bot_id=bot_id,
            dialogue_id=dialogue_id,
            source_type=source_type,
            source_id=source_id,
            category=category,
            initiator_kind=initiator_kind,
            initiator_bot_id=initiator_bot_id,
            initiator_user_id=initiator_user_id,
        )

        span_response.additional_properties = d
        return span_response

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
