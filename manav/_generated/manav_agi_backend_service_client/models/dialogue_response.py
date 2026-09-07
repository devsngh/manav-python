from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dialogue_response_interrupt_data_type_0 import DialogueResponseInterruptDataType0
    from ..models.dialogue_response_response_metadata_type_0 import DialogueResponseResponseMetadataType0


T = TypeVar("T", bound="DialogueResponse")


@_attrs_define
class DialogueResponse:
    """Schema for dialogue response

    Attributes:
        id (UUID):
        thread_id (UUID):
        query (str):
        response (str):
        sequence_number (int):
        query_tokens (int | None):
        response_tokens (int | None):
        processing_time_ms (int | None):
        is_liked (bool):
        is_disliked (bool):
        feedback (None | str):
        feedback_rating (int | None):
        feedback_at (datetime.datetime | None):
        is_edited (bool):
        edit_count (int):
        original_query (None | str):
        is_deleted (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        response_format (None | str | Unset):
        response_metadata (DialogueResponseResponseMetadataType0 | None | Unset):
        file_urls (list[Any] | None | Unset):
        interrupted (bool | Unset):  Default: False.
        interrupt_data (DialogueResponseInterruptDataType0 | list[Any] | None | Unset):
    """

    id: UUID
    thread_id: UUID
    query: str
    response: str
    sequence_number: int
    query_tokens: int | None
    response_tokens: int | None
    processing_time_ms: int | None
    is_liked: bool
    is_disliked: bool
    feedback: None | str
    feedback_rating: int | None
    feedback_at: datetime.datetime | None
    is_edited: bool
    edit_count: int
    original_query: None | str
    is_deleted: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    response_format: None | str | Unset = UNSET
    response_metadata: DialogueResponseResponseMetadataType0 | None | Unset = UNSET
    file_urls: list[Any] | None | Unset = UNSET
    interrupted: bool | Unset = False
    interrupt_data: DialogueResponseInterruptDataType0 | list[Any] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dialogue_response_interrupt_data_type_0 import DialogueResponseInterruptDataType0  # noqa: PLC0415
        from ..models.dialogue_response_response_metadata_type_0 import (
            DialogueResponseResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        thread_id = str(self.thread_id)

        query = self.query

        response = self.response

        sequence_number = self.sequence_number

        query_tokens: int | None
        query_tokens = self.query_tokens

        response_tokens: int | None
        response_tokens = self.response_tokens

        processing_time_ms: int | None
        processing_time_ms = self.processing_time_ms

        is_liked = self.is_liked

        is_disliked = self.is_disliked

        feedback: None | str
        feedback = self.feedback

        feedback_rating: int | None
        feedback_rating = self.feedback_rating

        feedback_at: None | str
        if isinstance(self.feedback_at, datetime.datetime):
            feedback_at = self.feedback_at.isoformat()
        else:
            feedback_at = self.feedback_at

        is_edited = self.is_edited

        edit_count = self.edit_count

        original_query: None | str
        original_query = self.original_query

        is_deleted = self.is_deleted

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        response_format: None | str | Unset
        if isinstance(self.response_format, Unset):
            response_format = UNSET
        else:
            response_format = self.response_format

        response_metadata: dict[str, Any] | None | Unset
        if isinstance(self.response_metadata, Unset):
            response_metadata = UNSET
        elif isinstance(self.response_metadata, DialogueResponseResponseMetadataType0):
            response_metadata = self.response_metadata.to_dict()
        else:
            response_metadata = self.response_metadata

        file_urls: list[Any] | None | Unset
        if isinstance(self.file_urls, Unset):
            file_urls = UNSET
        elif isinstance(self.file_urls, list):
            file_urls = self.file_urls

        else:
            file_urls = self.file_urls

        interrupted = self.interrupted

        interrupt_data: dict[str, Any] | list[Any] | None | Unset
        if isinstance(self.interrupt_data, Unset):
            interrupt_data = UNSET
        elif isinstance(self.interrupt_data, DialogueResponseInterruptDataType0):
            interrupt_data = self.interrupt_data.to_dict()
        elif isinstance(self.interrupt_data, list):
            interrupt_data = self.interrupt_data

        else:
            interrupt_data = self.interrupt_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "thread_id": thread_id,
                "query": query,
                "response": response,
                "sequence_number": sequence_number,
                "query_tokens": query_tokens,
                "response_tokens": response_tokens,
                "processing_time_ms": processing_time_ms,
                "is_liked": is_liked,
                "is_disliked": is_disliked,
                "feedback": feedback,
                "feedback_rating": feedback_rating,
                "feedback_at": feedback_at,
                "is_edited": is_edited,
                "edit_count": edit_count,
                "original_query": original_query,
                "is_deleted": is_deleted,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata
        if file_urls is not UNSET:
            field_dict["file_urls"] = file_urls
        if interrupted is not UNSET:
            field_dict["interrupted"] = interrupted
        if interrupt_data is not UNSET:
            field_dict["interrupt_data"] = interrupt_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dialogue_response_interrupt_data_type_0 import DialogueResponseInterruptDataType0  # noqa: PLC0415
        from ..models.dialogue_response_response_metadata_type_0 import (
            DialogueResponseResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        thread_id = UUID(d.pop("thread_id"))

        query = d.pop("query")

        response = d.pop("response")

        sequence_number = d.pop("sequence_number")

        def _parse_query_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        query_tokens = _parse_query_tokens(d.pop("query_tokens"))

        def _parse_response_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        response_tokens = _parse_response_tokens(d.pop("response_tokens"))

        def _parse_processing_time_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        processing_time_ms = _parse_processing_time_ms(d.pop("processing_time_ms"))

        is_liked = d.pop("is_liked")

        is_disliked = d.pop("is_disliked")

        def _parse_feedback(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        feedback = _parse_feedback(d.pop("feedback"))

        def _parse_feedback_rating(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        feedback_rating = _parse_feedback_rating(d.pop("feedback_rating"))

        def _parse_feedback_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feedback_at_type_0 = datetime.datetime.fromisoformat(data)

                return feedback_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        feedback_at = _parse_feedback_at(d.pop("feedback_at"))

        is_edited = d.pop("is_edited")

        edit_count = d.pop("edit_count")

        def _parse_original_query(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        original_query = _parse_original_query(d.pop("original_query"))

        is_deleted = d.pop("is_deleted")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_response_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_format = _parse_response_format(d.pop("response_format", UNSET))

        def _parse_response_metadata(data: object) -> DialogueResponseResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_metadata_type_0 = DialogueResponseResponseMetadataType0.from_dict(data)

                return response_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DialogueResponseResponseMetadataType0 | None | Unset, data)

        response_metadata = _parse_response_metadata(d.pop("response_metadata", UNSET))

        def _parse_file_urls(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_urls_type_0 = cast(list[Any], data)

                return file_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        file_urls = _parse_file_urls(d.pop("file_urls", UNSET))

        interrupted = d.pop("interrupted", UNSET)

        def _parse_interrupt_data(data: object) -> DialogueResponseInterruptDataType0 | list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interrupt_data_type_0 = DialogueResponseInterruptDataType0.from_dict(data)

                return interrupt_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                interrupt_data_type_1 = cast(list[Any], data)

                return interrupt_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DialogueResponseInterruptDataType0 | list[Any] | None | Unset, data)

        interrupt_data = _parse_interrupt_data(d.pop("interrupt_data", UNSET))

        dialogue_response = cls(
            id=id,
            thread_id=thread_id,
            query=query,
            response=response,
            sequence_number=sequence_number,
            query_tokens=query_tokens,
            response_tokens=response_tokens,
            processing_time_ms=processing_time_ms,
            is_liked=is_liked,
            is_disliked=is_disliked,
            feedback=feedback,
            feedback_rating=feedback_rating,
            feedback_at=feedback_at,
            is_edited=is_edited,
            edit_count=edit_count,
            original_query=original_query,
            is_deleted=is_deleted,
            created_at=created_at,
            updated_at=updated_at,
            response_format=response_format,
            response_metadata=response_metadata,
            file_urls=file_urls,
            interrupted=interrupted,
            interrupt_data=interrupt_data,
        )

        dialogue_response.additional_properties = d
        return dialogue_response

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
