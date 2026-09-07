from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clone_and_run_request_parent_context_type_0 import CloneAndRunRequestParentContextType0


T = TypeVar("T", bound="CloneAndRunRequest")


@_attrs_define
class CloneAndRunRequest:
    """Spawn N parallel clones of the calling bot (one per slice), auto-merge results.

    Attributes:
        slices (list[str]): One instruction per clone
        merge_strategy (str | Unset): concatenate | vote | summarize Default: 'concatenate'.
        share_parent_context (bool | Unset):  Default: False.
        parent_context (CloneAndRunRequestParentContextType0 | None | Unset):
        deepagent_config_id (None | Unset | UUID):
        thread_id (None | Unset | UUID):
        title (None | str | Unset):
    """

    slices: list[str]
    merge_strategy: str | Unset = "concatenate"
    share_parent_context: bool | Unset = False
    parent_context: CloneAndRunRequestParentContextType0 | None | Unset = UNSET
    deepagent_config_id: None | Unset | UUID = UNSET
    thread_id: None | Unset | UUID = UNSET
    title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clone_and_run_request_parent_context_type_0 import (
            CloneAndRunRequestParentContextType0,  # noqa: PLC0415
        )

        slices = self.slices

        merge_strategy = self.merge_strategy

        share_parent_context = self.share_parent_context

        parent_context: dict[str, Any] | None | Unset
        if isinstance(self.parent_context, Unset):
            parent_context = UNSET
        elif isinstance(self.parent_context, CloneAndRunRequestParentContextType0):
            parent_context = self.parent_context.to_dict()
        else:
            parent_context = self.parent_context

        deepagent_config_id: None | str | Unset
        if isinstance(self.deepagent_config_id, Unset):
            deepagent_config_id = UNSET
        elif isinstance(self.deepagent_config_id, UUID):
            deepagent_config_id = str(self.deepagent_config_id)
        else:
            deepagent_config_id = self.deepagent_config_id

        thread_id: None | str | Unset
        if isinstance(self.thread_id, Unset):
            thread_id = UNSET
        elif isinstance(self.thread_id, UUID):
            thread_id = str(self.thread_id)
        else:
            thread_id = self.thread_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slices": slices,
            }
        )
        if merge_strategy is not UNSET:
            field_dict["merge_strategy"] = merge_strategy
        if share_parent_context is not UNSET:
            field_dict["share_parent_context"] = share_parent_context
        if parent_context is not UNSET:
            field_dict["parent_context"] = parent_context
        if deepagent_config_id is not UNSET:
            field_dict["deepagent_config_id"] = deepagent_config_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clone_and_run_request_parent_context_type_0 import (
            CloneAndRunRequestParentContextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        slices = cast(list[str], d.pop("slices"))

        merge_strategy = d.pop("merge_strategy", UNSET)

        share_parent_context = d.pop("share_parent_context", UNSET)

        def _parse_parent_context(data: object) -> CloneAndRunRequestParentContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_context_type_0 = CloneAndRunRequestParentContextType0.from_dict(data)

                return parent_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CloneAndRunRequestParentContextType0 | None | Unset, data)

        parent_context = _parse_parent_context(d.pop("parent_context", UNSET))

        def _parse_deepagent_config_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deepagent_config_id_type_0 = UUID(data)

                return deepagent_config_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deepagent_config_id = _parse_deepagent_config_id(d.pop("deepagent_config_id", UNSET))

        def _parse_thread_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                thread_id_type_0 = UUID(data)

                return thread_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        thread_id = _parse_thread_id(d.pop("thread_id", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        clone_and_run_request = cls(
            slices=slices,
            merge_strategy=merge_strategy,
            share_parent_context=share_parent_context,
            parent_context=parent_context,
            deepagent_config_id=deepagent_config_id,
            thread_id=thread_id,
            title=title,
        )

        clone_and_run_request.additional_properties = d
        return clone_and_run_request

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
