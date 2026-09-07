from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkpoint_detail_checkpoint import CheckpointDetailCheckpoint
    from ..models.checkpoint_detail_metadata import CheckpointDetailMetadata


T = TypeVar("T", bound="CheckpointDetail")


@_attrs_define
class CheckpointDetail:
    """
    Attributes:
        thread_id (str):
        checkpoint_ns (str):
        checkpoint_id (str):
        checkpoint (CheckpointDetailCheckpoint):
        metadata (CheckpointDetailMetadata):
        parent_checkpoint_id (None | str | Unset):
        type_ (None | str | Unset):
    """

    thread_id: str
    checkpoint_ns: str
    checkpoint_id: str
    checkpoint: CheckpointDetailCheckpoint
    metadata: CheckpointDetailMetadata
    parent_checkpoint_id: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        checkpoint_ns = self.checkpoint_ns

        checkpoint_id = self.checkpoint_id

        checkpoint = self.checkpoint.to_dict()

        metadata = self.metadata.to_dict()

        parent_checkpoint_id: None | str | Unset
        if isinstance(self.parent_checkpoint_id, Unset):
            parent_checkpoint_id = UNSET
        else:
            parent_checkpoint_id = self.parent_checkpoint_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_id": thread_id,
                "checkpoint_ns": checkpoint_ns,
                "checkpoint_id": checkpoint_id,
                "checkpoint": checkpoint,
                "metadata": metadata,
            }
        )
        if parent_checkpoint_id is not UNSET:
            field_dict["parent_checkpoint_id"] = parent_checkpoint_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkpoint_detail_checkpoint import CheckpointDetailCheckpoint  # noqa: PLC0415
        from ..models.checkpoint_detail_metadata import CheckpointDetailMetadata  # noqa: PLC0415

        d = dict(src_dict)
        thread_id = d.pop("thread_id")

        checkpoint_ns = d.pop("checkpoint_ns")

        checkpoint_id = d.pop("checkpoint_id")

        checkpoint = CheckpointDetailCheckpoint.from_dict(d.pop("checkpoint"))

        metadata = CheckpointDetailMetadata.from_dict(d.pop("metadata"))

        def _parse_parent_checkpoint_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_checkpoint_id = _parse_parent_checkpoint_id(d.pop("parent_checkpoint_id", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        checkpoint_detail = cls(
            thread_id=thread_id,
            checkpoint_ns=checkpoint_ns,
            checkpoint_id=checkpoint_id,
            checkpoint=checkpoint,
            metadata=metadata,
            parent_checkpoint_id=parent_checkpoint_id,
            type_=type_,
        )

        checkpoint_detail.additional_properties = d
        return checkpoint_detail

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
