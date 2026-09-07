from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brand_voice_guidelines_update_approved_synonyms_type_0 import (
        BrandVoiceGuidelinesUpdateApprovedSynonymsType0,
    )
    from ..models.brand_voice_guidelines_update_example_passages_type_0_item import (
        BrandVoiceGuidelinesUpdateExamplePassagesType0Item,
    )
    from ..models.brand_voice_guidelines_update_tone_attributes_type_0 import (
        BrandVoiceGuidelinesUpdateToneAttributesType0,
    )


T = TypeVar("T", bound="BrandVoiceGuidelinesUpdate")


@_attrs_define
class BrandVoiceGuidelinesUpdate:
    """
    Attributes:
        voice_summary (None | str | Unset):
        tone_attributes (BrandVoiceGuidelinesUpdateToneAttributesType0 | None | Unset):
        voice_dos (list[str] | None | Unset):
        voice_donts (list[str] | None | Unset):
        banned_phrases (list[str] | None | Unset):
        approved_synonyms (BrandVoiceGuidelinesUpdateApprovedSynonymsType0 | None | Unset):
        example_passages (list[BrandVoiceGuidelinesUpdateExamplePassagesType0Item] | None | Unset):
    """

    voice_summary: None | str | Unset = UNSET
    tone_attributes: BrandVoiceGuidelinesUpdateToneAttributesType0 | None | Unset = UNSET
    voice_dos: list[str] | None | Unset = UNSET
    voice_donts: list[str] | None | Unset = UNSET
    banned_phrases: list[str] | None | Unset = UNSET
    approved_synonyms: BrandVoiceGuidelinesUpdateApprovedSynonymsType0 | None | Unset = UNSET
    example_passages: list[BrandVoiceGuidelinesUpdateExamplePassagesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brand_voice_guidelines_update_approved_synonyms_type_0 import (
            BrandVoiceGuidelinesUpdateApprovedSynonymsType0,  # noqa: PLC0415
        )
        from ..models.brand_voice_guidelines_update_tone_attributes_type_0 import (
            BrandVoiceGuidelinesUpdateToneAttributesType0,  # noqa: PLC0415
        )

        voice_summary: None | str | Unset
        if isinstance(self.voice_summary, Unset):
            voice_summary = UNSET
        else:
            voice_summary = self.voice_summary

        tone_attributes: dict[str, Any] | None | Unset
        if isinstance(self.tone_attributes, Unset):
            tone_attributes = UNSET
        elif isinstance(self.tone_attributes, BrandVoiceGuidelinesUpdateToneAttributesType0):
            tone_attributes = self.tone_attributes.to_dict()
        else:
            tone_attributes = self.tone_attributes

        voice_dos: list[str] | None | Unset
        if isinstance(self.voice_dos, Unset):
            voice_dos = UNSET
        elif isinstance(self.voice_dos, list):
            voice_dos = self.voice_dos

        else:
            voice_dos = self.voice_dos

        voice_donts: list[str] | None | Unset
        if isinstance(self.voice_donts, Unset):
            voice_donts = UNSET
        elif isinstance(self.voice_donts, list):
            voice_donts = self.voice_donts

        else:
            voice_donts = self.voice_donts

        banned_phrases: list[str] | None | Unset
        if isinstance(self.banned_phrases, Unset):
            banned_phrases = UNSET
        elif isinstance(self.banned_phrases, list):
            banned_phrases = self.banned_phrases

        else:
            banned_phrases = self.banned_phrases

        approved_synonyms: dict[str, Any] | None | Unset
        if isinstance(self.approved_synonyms, Unset):
            approved_synonyms = UNSET
        elif isinstance(self.approved_synonyms, BrandVoiceGuidelinesUpdateApprovedSynonymsType0):
            approved_synonyms = self.approved_synonyms.to_dict()
        else:
            approved_synonyms = self.approved_synonyms

        example_passages: list[dict[str, Any]] | None | Unset
        if isinstance(self.example_passages, Unset):
            example_passages = UNSET
        elif isinstance(self.example_passages, list):
            example_passages = []
            for example_passages_type_0_item_data in self.example_passages:
                example_passages_type_0_item = example_passages_type_0_item_data.to_dict()
                example_passages.append(example_passages_type_0_item)

        else:
            example_passages = self.example_passages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voice_summary is not UNSET:
            field_dict["voice_summary"] = voice_summary
        if tone_attributes is not UNSET:
            field_dict["tone_attributes"] = tone_attributes
        if voice_dos is not UNSET:
            field_dict["voice_dos"] = voice_dos
        if voice_donts is not UNSET:
            field_dict["voice_donts"] = voice_donts
        if banned_phrases is not UNSET:
            field_dict["banned_phrases"] = banned_phrases
        if approved_synonyms is not UNSET:
            field_dict["approved_synonyms"] = approved_synonyms
        if example_passages is not UNSET:
            field_dict["example_passages"] = example_passages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_voice_guidelines_update_approved_synonyms_type_0 import (
            BrandVoiceGuidelinesUpdateApprovedSynonymsType0,  # noqa: PLC0415
        )
        from ..models.brand_voice_guidelines_update_example_passages_type_0_item import (
            BrandVoiceGuidelinesUpdateExamplePassagesType0Item,  # noqa: PLC0415
        )
        from ..models.brand_voice_guidelines_update_tone_attributes_type_0 import (
            BrandVoiceGuidelinesUpdateToneAttributesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_voice_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_summary = _parse_voice_summary(d.pop("voice_summary", UNSET))

        def _parse_tone_attributes(data: object) -> BrandVoiceGuidelinesUpdateToneAttributesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tone_attributes_type_0 = BrandVoiceGuidelinesUpdateToneAttributesType0.from_dict(data)

                return tone_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandVoiceGuidelinesUpdateToneAttributesType0 | None | Unset, data)

        tone_attributes = _parse_tone_attributes(d.pop("tone_attributes", UNSET))

        def _parse_voice_dos(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voice_dos_type_0 = cast(list[str], data)

                return voice_dos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        voice_dos = _parse_voice_dos(d.pop("voice_dos", UNSET))

        def _parse_voice_donts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voice_donts_type_0 = cast(list[str], data)

                return voice_donts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        voice_donts = _parse_voice_donts(d.pop("voice_donts", UNSET))

        def _parse_banned_phrases(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                banned_phrases_type_0 = cast(list[str], data)

                return banned_phrases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        banned_phrases = _parse_banned_phrases(d.pop("banned_phrases", UNSET))

        def _parse_approved_synonyms(data: object) -> BrandVoiceGuidelinesUpdateApprovedSynonymsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approved_synonyms_type_0 = BrandVoiceGuidelinesUpdateApprovedSynonymsType0.from_dict(data)

                return approved_synonyms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandVoiceGuidelinesUpdateApprovedSynonymsType0 | None | Unset, data)

        approved_synonyms = _parse_approved_synonyms(d.pop("approved_synonyms", UNSET))

        def _parse_example_passages(
            data: object,
        ) -> list[BrandVoiceGuidelinesUpdateExamplePassagesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                example_passages_type_0 = []
                _example_passages_type_0 = data
                for example_passages_type_0_item_data in _example_passages_type_0:
                    example_passages_type_0_item = BrandVoiceGuidelinesUpdateExamplePassagesType0Item.from_dict(
                        example_passages_type_0_item_data
                    )

                    example_passages_type_0.append(example_passages_type_0_item)

                return example_passages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BrandVoiceGuidelinesUpdateExamplePassagesType0Item] | None | Unset, data)

        example_passages = _parse_example_passages(d.pop("example_passages", UNSET))

        brand_voice_guidelines_update = cls(
            voice_summary=voice_summary,
            tone_attributes=tone_attributes,
            voice_dos=voice_dos,
            voice_donts=voice_donts,
            banned_phrases=banned_phrases,
            approved_synonyms=approved_synonyms,
            example_passages=example_passages,
        )

        brand_voice_guidelines_update.additional_properties = d
        return brand_voice_guidelines_update

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
