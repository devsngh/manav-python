from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_detail_attributes import EventDetailAttributes
    from ..models.event_detail_tokens_type_0 import EventDetailTokensType0


T = TypeVar("T", bound="EventDetail")


@_attrs_define
class EventDetail:
    """Full detail for one event. Union-of-union — the frontend inspects
    `kind` to decide which sub-block to render (llm block / mcp block /
    file block / checkpoint block / error block).

        Attributes:
            id (str):
            ts (datetime.datetime):
            kind (str):
            label (str):
            subject_kind (None | str | Unset):
            status (None | str | Unset):
            error (None | str | Unset):
            model (None | str | Unset):
            tool_name (None | str | Unset):
            server (None | str | Unset):
            args (Any | None | Unset):
            result (Any | None | Unset):
            duration_ms (int | None | Unset):
            tokens (EventDetailTokensType0 | None | Unset):
            cost_usd (float | None | Unset):
            path (None | str | Unset):
            content_preview (None | str | Unset):
            content_size (int | None | Unset):
            is_seed (bool | None | Unset):
            checkpoint_id (None | str | Unset):
            thread_id (None | str | Unset):
            graph_step (int | None | Unset):
            caused_by (None | str | Unset):
            triggered (list[str] | Unset):
            attributes (EventDetailAttributes | Unset):
    """

    id: str
    ts: datetime.datetime
    kind: str
    label: str
    subject_kind: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    tool_name: None | str | Unset = UNSET
    server: None | str | Unset = UNSET
    args: Any | None | Unset = UNSET
    result: Any | None | Unset = UNSET
    duration_ms: int | None | Unset = UNSET
    tokens: EventDetailTokensType0 | None | Unset = UNSET
    cost_usd: float | None | Unset = UNSET
    path: None | str | Unset = UNSET
    content_preview: None | str | Unset = UNSET
    content_size: int | None | Unset = UNSET
    is_seed: bool | None | Unset = UNSET
    checkpoint_id: None | str | Unset = UNSET
    thread_id: None | str | Unset = UNSET
    graph_step: int | None | Unset = UNSET
    caused_by: None | str | Unset = UNSET
    triggered: list[str] | Unset = UNSET
    attributes: EventDetailAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_detail_tokens_type_0 import EventDetailTokensType0  # noqa: PLC0415

        id = self.id

        ts = self.ts.isoformat()

        kind = self.kind

        label = self.label

        subject_kind: None | str | Unset
        if isinstance(self.subject_kind, Unset):
            subject_kind = UNSET
        else:
            subject_kind = self.subject_kind

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        tool_name: None | str | Unset
        if isinstance(self.tool_name, Unset):
            tool_name = UNSET
        else:
            tool_name = self.tool_name

        server: None | str | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        args: Any | None | Unset
        if isinstance(self.args, Unset):
            args = UNSET
        else:
            args = self.args

        result: Any | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        else:
            result = self.result

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        tokens: dict[str, Any] | None | Unset
        if isinstance(self.tokens, Unset):
            tokens = UNSET
        elif isinstance(self.tokens, EventDetailTokensType0):
            tokens = self.tokens.to_dict()
        else:
            tokens = self.tokens

        cost_usd: float | None | Unset
        if isinstance(self.cost_usd, Unset):
            cost_usd = UNSET
        else:
            cost_usd = self.cost_usd

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        content_preview: None | str | Unset
        if isinstance(self.content_preview, Unset):
            content_preview = UNSET
        else:
            content_preview = self.content_preview

        content_size: int | None | Unset
        if isinstance(self.content_size, Unset):
            content_size = UNSET
        else:
            content_size = self.content_size

        is_seed: bool | None | Unset
        if isinstance(self.is_seed, Unset):
            is_seed = UNSET
        else:
            is_seed = self.is_seed

        checkpoint_id: None | str | Unset
        if isinstance(self.checkpoint_id, Unset):
            checkpoint_id = UNSET
        else:
            checkpoint_id = self.checkpoint_id

        thread_id: None | str | Unset
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        else:
            thread_id = self.thread_id

        graph_step: int | None | Unset
        if isinstance(self.graph_step, Unset):
            graph_step = UNSET
        else:
            graph_step = self.graph_step

        caused_by: None | str | Unset
        if isinstance(self.caused_by, Unset):
            caused_by = UNSET
        else:
            caused_by = self.caused_by

        triggered: list[str] | Unset = UNSET
        if not isinstance(self.triggered, Unset):
            triggered = self.triggered

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ts": ts,
                "kind": kind,
                "label": label,
            }
        )
        if subject_kind is not UNSET:
            field_dict["subject_kind"] = subject_kind
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if model is not UNSET:
            field_dict["model"] = model
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name
        if server is not UNSET:
            field_dict["server"] = server
        if args is not UNSET:
            field_dict["args"] = args
        if result is not UNSET:
            field_dict["result"] = result
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if cost_usd is not UNSET:
            field_dict["cost_usd"] = cost_usd
        if path is not UNSET:
            field_dict["path"] = path
        if content_preview is not UNSET:
            field_dict["content_preview"] = content_preview
        if content_size is not UNSET:
            field_dict["content_size"] = content_size
        if is_seed is not UNSET:
            field_dict["is_seed"] = is_seed
        if checkpoint_id is not UNSET:
            field_dict["checkpoint_id"] = checkpoint_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if graph_step is not UNSET:
            field_dict["graph_step"] = graph_step
        if caused_by is not UNSET:
            field_dict["caused_by"] = caused_by
        if triggered is not UNSET:
            field_dict["triggered"] = triggered
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_detail_attributes import EventDetailAttributes  # noqa: PLC0415
        from ..models.event_detail_tokens_type_0 import EventDetailTokensType0  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        ts = datetime.datetime.fromisoformat(d.pop("ts"))

        kind = d.pop("kind")

        label = d.pop("label")

        def _parse_subject_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject_kind = _parse_subject_kind(d.pop("subject_kind", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_tool_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tool_name = _parse_tool_name(d.pop("tool_name", UNSET))

        def _parse_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server = _parse_server(d.pop("server", UNSET))

        def _parse_args(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        args = _parse_args(d.pop("args", UNSET))

        def _parse_result(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        result = _parse_result(d.pop("result", UNSET))

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        def _parse_tokens(data: object) -> EventDetailTokensType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tokens_type_0 = EventDetailTokensType0.from_dict(data)

                return tokens_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventDetailTokensType0 | None | Unset, data)

        tokens = _parse_tokens(d.pop("tokens", UNSET))

        def _parse_cost_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_usd = _parse_cost_usd(d.pop("cost_usd", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_content_preview(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_preview = _parse_content_preview(d.pop("content_preview", UNSET))

        def _parse_content_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        content_size = _parse_content_size(d.pop("content_size", UNSET))

        def _parse_is_seed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_seed = _parse_is_seed(d.pop("is_seed", UNSET))

        def _parse_checkpoint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checkpoint_id = _parse_checkpoint_id(d.pop("checkpoint_id", UNSET))

        def _parse_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        def _parse_graph_step(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        graph_step = _parse_graph_step(d.pop("graph_step", UNSET))

        def _parse_caused_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caused_by = _parse_caused_by(d.pop("caused_by", UNSET))

        triggered = cast(list[str], d.pop("triggered", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: EventDetailAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = EventDetailAttributes.from_dict(_attributes)

        event_detail = cls(
            id=id,
            ts=ts,
            kind=kind,
            label=label,
            subject_kind=subject_kind,
            status=status,
            error=error,
            model=model,
            tool_name=tool_name,
            server=server,
            args=args,
            result=result,
            duration_ms=duration_ms,
            tokens=tokens,
            cost_usd=cost_usd,
            path=path,
            content_preview=content_preview,
            content_size=content_size,
            is_seed=is_seed,
            checkpoint_id=checkpoint_id,
            thread_id=thread_id,
            graph_step=graph_step,
            caused_by=caused_by,
            triggered=triggered,
            attributes=attributes,
        )

        event_detail.additional_properties = d
        return event_detail

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
