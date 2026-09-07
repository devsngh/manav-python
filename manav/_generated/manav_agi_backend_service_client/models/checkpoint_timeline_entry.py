from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckpointTimelineEntry")


@_attrs_define
class CheckpointTimelineEntry:
    """
    Attributes:
        checkpoint_id (str):
        parent_checkpoint_id (None | str | Unset):
        step (int | None | Unset):
        source (None | str | Unset):
        writes_preview (str | Unset):  Default: ''.
    """

    checkpoint_id: str
    parent_checkpoint_id: None | str | Unset = UNSET
    step: int | None | Unset = UNSET
    source: None | str | Unset = UNSET
    writes_preview: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checkpoint_id = self.checkpoint_id

        parent_checkpoint_id: None | str | Unset
        if isinstance(self.parent_checkpoint_id, Unset):
            parent_checkpoint_id = UNSET
        else:
            parent_checkpoint_id = self.parent_checkpoint_id

        step: int | None | Unset
        if isinstance(self.step, Unset):
            step = UNSET
        else:
            step = self.step

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        writes_preview = self.writes_preview

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checkpoint_id": checkpoint_id,
            }
        )
        if parent_checkpoint_id is not UNSET:
            field_dict["parent_checkpoint_id"] = parent_checkpoint_id
        if step is not UNSET:
            field_dict["step"] = step
        if source is not UNSET:
            field_dict["source"] = source
        if writes_preview is not UNSET:
            field_dict["writes_preview"] = writes_preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checkpoint_id = d.pop("checkpoint_id")

        def _parse_parent_checkpoint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_checkpoint_id = _parse_parent_checkpoint_id(d.pop("parent_checkpoint_id", UNSET))

        def _parse_step(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        step = _parse_step(d.pop("step", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        writes_preview = d.pop("writes_preview", UNSET)

        checkpoint_timeline_entry = cls(
            checkpoint_id=checkpoint_id,
            parent_checkpoint_id=parent_checkpoint_id,
            step=step,
            source=source,
            writes_preview=writes_preview,
        )

        checkpoint_timeline_entry.additional_properties = d
        return checkpoint_timeline_entry

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
