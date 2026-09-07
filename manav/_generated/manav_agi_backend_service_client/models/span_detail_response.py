from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.span_detail_response_attributes_type_0 import SpanDetailResponseAttributesType0


T = TypeVar("T", bound="SpanDetailResponse")


@_attrs_define
class SpanDetailResponse:
    """Full single-span detail for Pane-3.

    Attributes:
        id (UUID):
        trace_id (str):
        operation (str):
        parent_id (None | Unset | UUID):
        category (None | str | Unset):
        kind (str | Unset):  Default: 'INTERNAL'.
        service (str | Unset):  Default: 'orchestrator'.
        start_time (datetime.datetime | None | Unset):
        end_time (datetime.datetime | None | Unset):
        duration_ms (float | None | Unset):
        status (str | Unset):  Default: 'OK'.
        error_type (None | str | Unset):
        error_message (None | str | Unset):
        attributes (None | SpanDetailResponseAttributesType0 | Unset):
        dialogue_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        org_id (None | Unset | UUID):
        source_type (None | str | Unset):
        source_id (None | Unset | UUID):
        user_id (None | Unset | UUID):
    """

    id: UUID
    trace_id: str
    operation: str
    parent_id: None | Unset | UUID = UNSET
    category: None | str | Unset = UNSET
    kind: str | Unset = "INTERNAL"
    service: str | Unset = "orchestrator"
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    duration_ms: float | None | Unset = UNSET
    status: str | Unset = "OK"
    error_type: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    attributes: None | SpanDetailResponseAttributesType0 | Unset = UNSET
    dialogue_id: None | Unset | UUID = UNSET
    bot_id: None | Unset | UUID = UNSET
    org_id: None | Unset | UUID = UNSET
    source_type: None | str | Unset = UNSET
    source_id: None | Unset | UUID = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.span_detail_response_attributes_type_0 import SpanDetailResponseAttributesType0  # noqa: PLC0415

        id = str(self.id)

        trace_id = self.trace_id

        operation = self.operation

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        kind = self.kind

        service = self.service

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

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

        status = self.status

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
        elif isinstance(self.attributes, SpanDetailResponseAttributesType0):
            attributes = self.attributes.to_dict()
        else:
            attributes = self.attributes

        dialogue_id: None | str | Unset
        if isinstance(self.dialogue_id, Unset):
            dialogue_id = UNSET
        elif isinstance(self.dialogue_id, UUID):
            dialogue_id = str(self.dialogue_id)
        else:
            dialogue_id = self.dialogue_id

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

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

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "trace_id": trace_id,
                "operation": operation,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if category is not UNSET:
            field_dict["category"] = category
        if kind is not UNSET:
            field_dict["kind"] = kind
        if service is not UNSET:
            field_dict["service"] = service
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if status is not UNSET:
            field_dict["status"] = status
        if error_type is not UNSET:
            field_dict["error_type"] = error_type
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if dialogue_id is not UNSET:
            field_dict["dialogue_id"] = dialogue_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.span_detail_response_attributes_type_0 import SpanDetailResponseAttributesType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        trace_id = d.pop("trace_id")

        operation = d.pop("operation")

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

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        kind = d.pop("kind", UNSET)

        service = d.pop("service", UNSET)

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

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

        status = d.pop("status", UNSET)

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

        def _parse_attributes(data: object) -> None | SpanDetailResponseAttributesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attributes_type_0 = SpanDetailResponseAttributesType0.from_dict(data)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpanDetailResponseAttributesType0 | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

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

        span_detail_response = cls(
            id=id,
            trace_id=trace_id,
            operation=operation,
            parent_id=parent_id,
            category=category,
            kind=kind,
            service=service,
            start_time=start_time,
            end_time=end_time,
            duration_ms=duration_ms,
            status=status,
            error_type=error_type,
            error_message=error_message,
            attributes=attributes,
            dialogue_id=dialogue_id,
            bot_id=bot_id,
            org_id=org_id,
            source_type=source_type,
            source_id=source_id,
            user_id=user_id,
        )

        span_detail_response.additional_properties = d
        return span_detail_response

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
