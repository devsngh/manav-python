from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbox_section import InboxSection
    from ..models.inbox_thread import InboxThread


T = TypeVar("T", bound="InboxResponse")


@_attrs_define
class InboxResponse:
    """
    Attributes:
        sections (list[InboxSection]):
        main_channel (InboxThread | None | Unset):
    """

    sections: list[InboxSection]
    main_channel: InboxThread | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inbox_thread import InboxThread  # noqa: PLC0415

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        main_channel: dict[str, Any] | None | Unset
        if isinstance(self.main_channel, Unset):
            main_channel = UNSET
        elif isinstance(self.main_channel, InboxThread):
            main_channel = self.main_channel.to_dict()
        else:
            main_channel = self.main_channel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sections": sections,
            }
        )
        if main_channel is not UNSET:
            field_dict["main_channel"] = main_channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbox_section import InboxSection  # noqa: PLC0415
        from ..models.inbox_thread import InboxThread  # noqa: PLC0415

        d = dict(src_dict)
        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = InboxSection.from_dict(sections_item_data)

            sections.append(sections_item)

        def _parse_main_channel(data: object) -> InboxThread | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                main_channel_type_0 = InboxThread.from_dict(data)

                return main_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InboxThread | None | Unset, data)

        main_channel = _parse_main_channel(d.pop("main_channel", UNSET))

        inbox_response = cls(
            sections=sections,
            main_channel=main_channel,
        )

        inbox_response.additional_properties = d
        return inbox_response

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
