from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_description_upsert_generation_metadata_type_0 import (
        AssetDescriptionUpsertGenerationMetadataType0,
    )
    from ..models.asset_description_upsert_type_specific_fields_type_0 import (
        AssetDescriptionUpsertTypeSpecificFieldsType0,
    )


T = TypeVar("T", bound="AssetDescriptionUpsert")


@_attrs_define
class AssetDescriptionUpsert:
    """
    Attributes:
        prompt_text (None | str | Unset):
        negative_prompt (None | str | Unset):
        generation_model (None | str | Unset):
        generation_seed (int | None | Unset):
        generation_metadata (AssetDescriptionUpsertGenerationMetadataType0 | None | Unset):
        character_reference_ids (list[UUID] | None | Unset):
        style_reference_ids (list[UUID] | None | Unset):
        subject (None | str | Unset):
        setting (None | str | Unset):
        mood (None | str | Unset):
        composition (None | str | Unset):
        visible_text (None | str | Unset):
        visible_brand_marks (None | str | Unset):
        characters_present (list[UUID] | None | Unset):
        palette_hex (list[str] | None | Unset):
        type_specific_fields (AssetDescriptionUpsertTypeSpecificFieldsType0 | None | Unset):
        style_match_score (float | None | str | Unset):
        character_continuity_score (float | None | str | Unset):
    """

    prompt_text: None | str | Unset = UNSET
    negative_prompt: None | str | Unset = UNSET
    generation_model: None | str | Unset = UNSET
    generation_seed: int | None | Unset = UNSET
    generation_metadata: AssetDescriptionUpsertGenerationMetadataType0 | None | Unset = UNSET
    character_reference_ids: list[UUID] | None | Unset = UNSET
    style_reference_ids: list[UUID] | None | Unset = UNSET
    subject: None | str | Unset = UNSET
    setting: None | str | Unset = UNSET
    mood: None | str | Unset = UNSET
    composition: None | str | Unset = UNSET
    visible_text: None | str | Unset = UNSET
    visible_brand_marks: None | str | Unset = UNSET
    characters_present: list[UUID] | None | Unset = UNSET
    palette_hex: list[str] | None | Unset = UNSET
    type_specific_fields: AssetDescriptionUpsertTypeSpecificFieldsType0 | None | Unset = UNSET
    style_match_score: float | None | str | Unset = UNSET
    character_continuity_score: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_description_upsert_generation_metadata_type_0 import (
            AssetDescriptionUpsertGenerationMetadataType0,  # noqa: PLC0415
        )
        from ..models.asset_description_upsert_type_specific_fields_type_0 import (
            AssetDescriptionUpsertTypeSpecificFieldsType0,  # noqa: PLC0415
        )

        prompt_text: None | str | Unset
        if isinstance(self.prompt_text, Unset):
            prompt_text = UNSET
        else:
            prompt_text = self.prompt_text

        negative_prompt: None | str | Unset
        if isinstance(self.negative_prompt, Unset):
            negative_prompt = UNSET
        else:
            negative_prompt = self.negative_prompt

        generation_model: None | str | Unset
        if isinstance(self.generation_model, Unset):
            generation_model = UNSET
        else:
            generation_model = self.generation_model

        generation_seed: int | None | Unset
        if isinstance(self.generation_seed, Unset):
            generation_seed = UNSET
        else:
            generation_seed = self.generation_seed

        generation_metadata: dict[str, Any] | None | Unset
        if isinstance(self.generation_metadata, Unset):
            generation_metadata = UNSET
        elif isinstance(self.generation_metadata, AssetDescriptionUpsertGenerationMetadataType0):
            generation_metadata = self.generation_metadata.to_dict()
        else:
            generation_metadata = self.generation_metadata

        character_reference_ids: list[str] | None | Unset
        if isinstance(self.character_reference_ids, Unset):
            character_reference_ids = UNSET
        elif isinstance(self.character_reference_ids, list):
            character_reference_ids = []
            for character_reference_ids_type_0_item_data in self.character_reference_ids:
                character_reference_ids_type_0_item = str(character_reference_ids_type_0_item_data)
                character_reference_ids.append(character_reference_ids_type_0_item)

        else:
            character_reference_ids = self.character_reference_ids

        style_reference_ids: list[str] | None | Unset
        if isinstance(self.style_reference_ids, Unset):
            style_reference_ids = UNSET
        elif isinstance(self.style_reference_ids, list):
            style_reference_ids = []
            for style_reference_ids_type_0_item_data in self.style_reference_ids:
                style_reference_ids_type_0_item = str(style_reference_ids_type_0_item_data)
                style_reference_ids.append(style_reference_ids_type_0_item)

        else:
            style_reference_ids = self.style_reference_ids

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        setting: None | str | Unset
        if isinstance(self.setting, Unset):
            setting = UNSET
        else:
            setting = self.setting

        mood: None | str | Unset
        if isinstance(self.mood, Unset):
            mood = UNSET
        else:
            mood = self.mood

        composition: None | str | Unset
        if isinstance(self.composition, Unset):
            composition = UNSET
        else:
            composition = self.composition

        visible_text: None | str | Unset
        if isinstance(self.visible_text, Unset):
            visible_text = UNSET
        else:
            visible_text = self.visible_text

        visible_brand_marks: None | str | Unset
        if isinstance(self.visible_brand_marks, Unset):
            visible_brand_marks = UNSET
        else:
            visible_brand_marks = self.visible_brand_marks

        characters_present: list[str] | None | Unset
        if isinstance(self.characters_present, Unset):
            characters_present = UNSET
        elif isinstance(self.characters_present, list):
            characters_present = []
            for characters_present_type_0_item_data in self.characters_present:
                characters_present_type_0_item = str(characters_present_type_0_item_data)
                characters_present.append(characters_present_type_0_item)

        else:
            characters_present = self.characters_present

        palette_hex: list[str] | None | Unset
        if isinstance(self.palette_hex, Unset):
            palette_hex = UNSET
        elif isinstance(self.palette_hex, list):
            palette_hex = self.palette_hex

        else:
            palette_hex = self.palette_hex

        type_specific_fields: dict[str, Any] | None | Unset
        if isinstance(self.type_specific_fields, Unset):
            type_specific_fields = UNSET
        elif isinstance(self.type_specific_fields, AssetDescriptionUpsertTypeSpecificFieldsType0):
            type_specific_fields = self.type_specific_fields.to_dict()
        else:
            type_specific_fields = self.type_specific_fields

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
        if prompt_text is not UNSET:
            field_dict["prompt_text"] = prompt_text
        if negative_prompt is not UNSET:
            field_dict["negative_prompt"] = negative_prompt
        if generation_model is not UNSET:
            field_dict["generation_model"] = generation_model
        if generation_seed is not UNSET:
            field_dict["generation_seed"] = generation_seed
        if generation_metadata is not UNSET:
            field_dict["generation_metadata"] = generation_metadata
        if character_reference_ids is not UNSET:
            field_dict["character_reference_ids"] = character_reference_ids
        if style_reference_ids is not UNSET:
            field_dict["style_reference_ids"] = style_reference_ids
        if subject is not UNSET:
            field_dict["subject"] = subject
        if setting is not UNSET:
            field_dict["setting"] = setting
        if mood is not UNSET:
            field_dict["mood"] = mood
        if composition is not UNSET:
            field_dict["composition"] = composition
        if visible_text is not UNSET:
            field_dict["visible_text"] = visible_text
        if visible_brand_marks is not UNSET:
            field_dict["visible_brand_marks"] = visible_brand_marks
        if characters_present is not UNSET:
            field_dict["characters_present"] = characters_present
        if palette_hex is not UNSET:
            field_dict["palette_hex"] = palette_hex
        if type_specific_fields is not UNSET:
            field_dict["type_specific_fields"] = type_specific_fields
        if style_match_score is not UNSET:
            field_dict["style_match_score"] = style_match_score
        if character_continuity_score is not UNSET:
            field_dict["character_continuity_score"] = character_continuity_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_description_upsert_generation_metadata_type_0 import (
            AssetDescriptionUpsertGenerationMetadataType0,  # noqa: PLC0415
        )
        from ..models.asset_description_upsert_type_specific_fields_type_0 import (
            AssetDescriptionUpsertTypeSpecificFieldsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_prompt_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_text = _parse_prompt_text(d.pop("prompt_text", UNSET))

        def _parse_negative_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        negative_prompt = _parse_negative_prompt(d.pop("negative_prompt", UNSET))

        def _parse_generation_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        generation_model = _parse_generation_model(d.pop("generation_model", UNSET))

        def _parse_generation_seed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        generation_seed = _parse_generation_seed(d.pop("generation_seed", UNSET))

        def _parse_generation_metadata(data: object) -> AssetDescriptionUpsertGenerationMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                generation_metadata_type_0 = AssetDescriptionUpsertGenerationMetadataType0.from_dict(data)

                return generation_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetDescriptionUpsertGenerationMetadataType0 | None | Unset, data)

        generation_metadata = _parse_generation_metadata(d.pop("generation_metadata", UNSET))

        def _parse_character_reference_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                character_reference_ids_type_0 = []
                _character_reference_ids_type_0 = data
                for character_reference_ids_type_0_item_data in _character_reference_ids_type_0:
                    character_reference_ids_type_0_item = UUID(character_reference_ids_type_0_item_data)

                    character_reference_ids_type_0.append(character_reference_ids_type_0_item)

                return character_reference_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        character_reference_ids = _parse_character_reference_ids(d.pop("character_reference_ids", UNSET))

        def _parse_style_reference_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                style_reference_ids_type_0 = []
                _style_reference_ids_type_0 = data
                for style_reference_ids_type_0_item_data in _style_reference_ids_type_0:
                    style_reference_ids_type_0_item = UUID(style_reference_ids_type_0_item_data)

                    style_reference_ids_type_0.append(style_reference_ids_type_0_item)

                return style_reference_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        style_reference_ids = _parse_style_reference_ids(d.pop("style_reference_ids", UNSET))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_setting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        setting = _parse_setting(d.pop("setting", UNSET))

        def _parse_mood(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mood = _parse_mood(d.pop("mood", UNSET))

        def _parse_composition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        composition = _parse_composition(d.pop("composition", UNSET))

        def _parse_visible_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visible_text = _parse_visible_text(d.pop("visible_text", UNSET))

        def _parse_visible_brand_marks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visible_brand_marks = _parse_visible_brand_marks(d.pop("visible_brand_marks", UNSET))

        def _parse_characters_present(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                characters_present_type_0 = []
                _characters_present_type_0 = data
                for characters_present_type_0_item_data in _characters_present_type_0:
                    characters_present_type_0_item = UUID(characters_present_type_0_item_data)

                    characters_present_type_0.append(characters_present_type_0_item)

                return characters_present_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        characters_present = _parse_characters_present(d.pop("characters_present", UNSET))

        def _parse_palette_hex(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                palette_hex_type_0 = cast(list[str], data)

                return palette_hex_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        palette_hex = _parse_palette_hex(d.pop("palette_hex", UNSET))

        def _parse_type_specific_fields(data: object) -> AssetDescriptionUpsertTypeSpecificFieldsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_specific_fields_type_0 = AssetDescriptionUpsertTypeSpecificFieldsType0.from_dict(data)

                return type_specific_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetDescriptionUpsertTypeSpecificFieldsType0 | None | Unset, data)

        type_specific_fields = _parse_type_specific_fields(d.pop("type_specific_fields", UNSET))

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

        asset_description_upsert = cls(
            prompt_text=prompt_text,
            negative_prompt=negative_prompt,
            generation_model=generation_model,
            generation_seed=generation_seed,
            generation_metadata=generation_metadata,
            character_reference_ids=character_reference_ids,
            style_reference_ids=style_reference_ids,
            subject=subject,
            setting=setting,
            mood=mood,
            composition=composition,
            visible_text=visible_text,
            visible_brand_marks=visible_brand_marks,
            characters_present=characters_present,
            palette_hex=palette_hex,
            type_specific_fields=type_specific_fields,
            style_match_score=style_match_score,
            character_continuity_score=character_continuity_score,
        )

        asset_description_upsert.additional_properties = d
        return asset_description_upsert

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
