from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateContinuityScoresRequest")


@_attrs_define
class UpdateContinuityScoresRequest:
    """
    Attributes:
        style_match_score (float | None | str | Unset):
        character_continuity_score (float | None | str | Unset):
    """

    style_match_score: float | None | str | Unset = UNSET
    character_continuity_score: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        style_match_score: float | None | str | Unset
        if isinstance(self.style_match_score, Unset):
            style_match_score = UNSET
        else:
            style_match_score = self.style_match_score

        character_continuity_score: float | None | str | Unset
        if isinstance(self.character_continuity_score, Unset):
            character_continuity_score = UNSET
        else:
            character_continuity_score = self.character_continuity_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if style_match_score is not UNSET:
            field_dict["style_match_score"] = style_match_score
        if character_continuity_score is not UNSET:
            field_dict["character_continuity_score"] = character_continuity_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_style_match_score(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        style_match_score = _parse_style_match_score(d.pop("style_match_score", UNSET))

        def _parse_character_continuity_score(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        character_continuity_score = _parse_character_continuity_score(d.pop("character_continuity_score", UNSET))

        update_continuity_scores_request = cls(
            style_match_score=style_match_score,
            character_continuity_score=character_continuity_score,
        )

        update_continuity_scores_request.additional_properties = d
        return update_continuity_scores_request

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
