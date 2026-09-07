from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_tool_call_read_status import VoiceToolCallReadStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voice_tool_call_read_arguments import VoiceToolCallReadArguments
    from ..models.voice_tool_call_read_result_type_0 import VoiceToolCallReadResultType0


T = TypeVar("T", bound="VoiceToolCallRead")


@_attrs_define
class VoiceToolCallRead:
    """
    Attributes:
        id (UUID):
        tool_namespace (str):
        tool_name (str):
        status (VoiceToolCallReadStatus):
        invoked_at (datetime.datetime):
        turn_id (None | Unset | UUID):
        arguments (VoiceToolCallReadArguments | Unset):
        result (None | Unset | VoiceToolCallReadResultType0):
        error_message (None | str | Unset):
        completed_at (datetime.datetime | None | Unset):
        duration_ms (int | None | Unset):
        response_id (None | str | Unset):
        call_id (None | str | Unset):
    """

    id: UUID
    tool_namespace: str
    tool_name: str
    status: VoiceToolCallReadStatus
    invoked_at: datetime.datetime
    turn_id: None | Unset | UUID = UNSET
    arguments: VoiceToolCallReadArguments | Unset = UNSET
    result: None | Unset | VoiceToolCallReadResultType0 = UNSET
    error_message: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    response_id: None | str | Unset = UNSET
    call_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.voice_tool_call_read_result_type_0 import VoiceToolCallReadResultType0  # noqa: PLC0415

        id = str(self.id)

        tool_namespace = self.tool_namespace

        tool_name = self.tool_name

        status = self.status.value

        invoked_at = self.invoked_at.isoformat()

        turn_id: None | str | Unset
        if isinstance(self.turn_id, Unset):
            turn_id = UNSET
        elif isinstance(self.turn_id, UUID):
            turn_id = str(self.turn_id)
        else:
            turn_id = self.turn_id

        arguments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, VoiceToolCallReadResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        response_id: None | str | Unset
        if isinstance(self.response_id, Unset):
            response_id = UNSET
        else:
            response_id = self.response_id

        call_id: None | str | Unset
        if isinstance(self.call_id, Unset):
            call_id = UNSET
        else:
            call_id = self.call_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tool_namespace": tool_namespace,
                "tool_name": tool_name,
                "status": status,
                "invoked_at": invoked_at,
            }
        )
        if turn_id is not UNSET:
            field_dict["turn_id"] = turn_id
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if result is not UNSET:
            field_dict["result"] = result
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if response_id is not UNSET:
            field_dict["response_id"] = response_id
        if call_id is not UNSET:
            field_dict["call_id"] = call_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voice_tool_call_read_arguments import VoiceToolCallReadArguments  # noqa: PLC0415
        from ..models.voice_tool_call_read_result_type_0 import VoiceToolCallReadResultType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        tool_namespace = d.pop("tool_namespace")

        tool_name = d.pop("tool_name")

        status = VoiceToolCallReadStatus(d.pop("status"))

        invoked_at = datetime.datetime.fromisoformat(d.pop("invoked_at"))

        def _parse_turn_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                turn_id_type_0 = UUID(data)

                return turn_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        turn_id = _parse_turn_id(d.pop("turn_id", UNSET))

        _arguments = d.pop("arguments", UNSET)
        arguments: VoiceToolCallReadArguments | Unset
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = VoiceToolCallReadArguments.from_dict(_arguments)

        def _parse_result(data: object) -> None | Unset | VoiceToolCallReadResultType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = VoiceToolCallReadResultType0.from_dict(data)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VoiceToolCallReadResultType0, data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_response_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_id = _parse_response_id(d.pop("response_id", UNSET))

        def _parse_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        call_id = _parse_call_id(d.pop("call_id", UNSET))

        voice_tool_call_read = cls(
            id=id,
            tool_namespace=tool_namespace,
            tool_name=tool_name,
            status=status,
            invoked_at=invoked_at,
            turn_id=turn_id,
            arguments=arguments,
            result=result,
            error_message=error_message,
            completed_at=completed_at,
            duration_ms=duration_ms,
            response_id=response_id,
            call_id=call_id,
        )

        voice_tool_call_read.additional_properties = d
        return voice_tool_call_read

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
