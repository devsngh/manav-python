from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckFaithfulnessRequest")


@_attrs_define
class CheckFaithfulnessRequest:
    """
    Attributes:
        dialogue_id (str):
        judge_deepagent_config_id (None | str | Unset):
    """

    dialogue_id: str
    judge_deepagent_config_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dialogue_id = self.dialogue_id

        judge_deepagent_config_id: None | str | Unset
        if isinstance(self.judge_deepagent_config_id, Unset):
            judge_deepagent_config_id = UNSET
        else:
            judge_deepagent_config_id = self.judge_deepagent_config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dialogue_id": dialogue_id,
            }
        )
        if judge_deepagent_config_id is not UNSET:
            field_dict["judge_deepagent_config_id"] = judge_deepagent_config_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dialogue_id = d.pop("dialogue_id")

        def _parse_judge_deepagent_config_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        judge_deepagent_config_id = _parse_judge_deepagent_config_id(d.pop("judge_deepagent_config_id", UNSET))

        check_faithfulness_request = cls(
            dialogue_id=dialogue_id,
            judge_deepagent_config_id=judge_deepagent_config_id,
        )

        check_faithfulness_request.additional_properties = d
        return check_faithfulness_request

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
