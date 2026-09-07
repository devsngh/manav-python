from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.human_task_complete_output_data_type_0 import HumanTaskCompleteOutputDataType0


T = TypeVar("T", bound="HumanTaskComplete")


@_attrs_define
class HumanTaskComplete:
    """
    Attributes:
        note (None | str | Unset):
        output_data (HumanTaskCompleteOutputDataType0 | None | Unset):
    """

    note: None | str | Unset = UNSET
    output_data: HumanTaskCompleteOutputDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.human_task_complete_output_data_type_0 import HumanTaskCompleteOutputDataType0  # noqa: PLC0415

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        output_data: dict[str, Any] | None | Unset
        if isinstance(self.output_data, Unset):
            output_data = UNSET
        elif isinstance(self.output_data, HumanTaskCompleteOutputDataType0):
            output_data = self.output_data.to_dict()
        else:
            output_data = self.output_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note
        if output_data is not UNSET:
            field_dict["output_data"] = output_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.human_task_complete_output_data_type_0 import HumanTaskCompleteOutputDataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_output_data(data: object) -> HumanTaskCompleteOutputDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_data_type_0 = HumanTaskCompleteOutputDataType0.from_dict(data)

                return output_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HumanTaskCompleteOutputDataType0 | None | Unset, data)

        output_data = _parse_output_data(d.pop("output_data", UNSET))

        human_task_complete = cls(
            note=note,
            output_data=output_data,
        )

        human_task_complete.additional_properties = d
        return human_task_complete

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
