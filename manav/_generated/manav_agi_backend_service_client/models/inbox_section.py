from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbox_thread import InboxThread


T = TypeVar("T", bound="InboxSection")


@_attrs_define
class InboxSection:
    """One collapsible section of the launcher.

    Attributes:
        key (str):
        label (str):
        threads (list[InboxThread] | Unset):
    """

    key: str
    label: str
    threads: list[InboxThread] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        threads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.threads, Unset):
            threads = []
            for threads_item_data in self.threads:
                threads_item = threads_item_data.to_dict()
                threads.append(threads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
            }
        )
        if threads is not UNSET:
            field_dict["threads"] = threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbox_thread import InboxThread  # noqa: PLC0415

        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        _threads = d.pop("threads", UNSET)
        threads: list[InboxThread] | Unset = UNSET
        if _threads is not UNSET:
            threads = []
            for threads_item_data in _threads:
                threads_item = InboxThread.from_dict(threads_item_data)

                threads.append(threads_item)

        inbox_section = cls(
            key=key,
            label=label,
            threads=threads,
        )

        inbox_section.additional_properties = d
        return inbox_section

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
