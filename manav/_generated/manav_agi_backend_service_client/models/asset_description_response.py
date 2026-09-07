from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_description_response_generation_metadata_type_0 import (
        AssetDescriptionResponseGenerationMetadataType0,
    )
    from ..models.asset_description_response_type_specific_fields_type_0 import (
        AssetDescriptionResponseTypeSpecificFieldsType0,
    )


T = TypeVar("T", bound="AssetDescriptionResponse")


@_attrs_define
class AssetDescriptionResponse:
    """
    Attributes:
        id (UUID):
        asset_id (UUID):
        prompt_text (None | str):
        negative_prompt (None | str):
        generation_model (None | str):
        generation_seed (int | None):
        generation_metadata (AssetDescriptionResponseGenerationMetadataType0 | None):
        character_reference_ids (list[UUID] | None):
        style_reference_ids (list[UUID] | None):
        subject (None | str):
        setting (None | str):
        mood (None | str):
        composition (None | str):
        visible_text (None | str):
        visible_brand_marks (None | str):
        characters_present (list[UUID] | None):
        palette_hex (list[str] | None):
        type_specific_fields (AssetDescriptionResponseTypeSpecificFieldsType0 | None):
        style_match_score (None | str):
        character_continuity_score (None | str):
        description_generated_at (datetime.datetime | None):
        description_generated_by (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    asset_id: UUID
    prompt_text: None | str
    negative_prompt: None | str
    generation_model: None | str
    generation_seed: int | None
    generation_metadata: AssetDescriptionResponseGenerationMetadataType0 | None
    character_reference_ids: list[UUID] | None
    style_reference_ids: list[UUID] | None
    subject: None | str
    setting: None | str
    mood: None | str
    composition: None | str
    visible_text: None | str
    visible_brand_marks: None | str
    characters_present: list[UUID] | None
    palette_hex: list[str] | None
    type_specific_fields: AssetDescriptionResponseTypeSpecificFieldsType0 | None
    style_match_score: None | str
    character_continuity_score: None | str
    description_generated_at: datetime.datetime | None
    description_generated_by: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_description_response_generation_metadata_type_0 import (
            AssetDescriptionResponseGenerationMetadataType0,  # noqa: PLC0415
        )
        from ..models.asset_description_response_type_specific_fields_type_0 import (
            AssetDescriptionResponseTypeSpecificFieldsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        asset_id = str(self.asset_id)

        prompt_text: None | str
        prompt_text = self.prompt_text

        negative_prompt: None | str
        negative_prompt = self.negative_prompt

        generation_model: None | str
        generation_model = self.generation_model

        generation_seed: int | None
        generation_seed = self.generation_seed

        generation_metadata: dict[str, Any] | None
        if isinstance(self.generation_metadata, AssetDescriptionResponseGenerationMetadataType0):
            generation_metadata = self.generation_metadata.to_dict()
        else:
            generation_metadata = self.generation_metadata

        character_reference_ids: list[str] | None
        if isinstance(self.character_reference_ids, list):
            character_reference_ids = []
            for character_reference_ids_type_0_item_data in self.character_reference_ids:
                character_reference_ids_type_0_item = str(character_reference_ids_type_0_item_data)
                character_reference_ids.append(character_reference_ids_type_0_item)

        else:
            character_reference_ids = self.character_reference_ids

        style_reference_ids: list[str] | None
        if isinstance(self.style_reference_ids, list):
            style_reference_ids = []
            for style_reference_ids_type_0_item_data in self.style_reference_ids:
                style_reference_ids_type_0_item = str(style_reference_ids_type_0_item_data)
                style_reference_ids.append(style_reference_ids_type_0_item)

        else:
            style_reference_ids = self.style_reference_ids

        subject: None | str
        subject = self.subject

        setting: None | str
        setting = self.setting

        mood: None | str
        mood = self.mood

        composition: None | str
        composition = self.composition

        visible_text: None | str
        visible_text = self.visible_text

        visible_brand_marks: None | str
        visible_brand_marks = self.visible_brand_marks

        characters_present: list[str] | None
        if isinstance(self.characters_present, list):
            characters_present = []
            for characters_present_type_0_item_data in self.characters_present:
                characters_present_type_0_item = str(characters_present_type_0_item_data)
                characters_present.append(characters_present_type_0_item)

        else:
            characters_present = self.characters_present

        palette_hex: list[str] | None
        if isinstance(self.palette_hex, list):
            palette_hex = self.palette_hex

        else:
            palette_hex = self.palette_hex

        type_specific_fields: dict[str, Any] | None
        if isinstance(self.type_specific_fields, AssetDescriptionResponseTypeSpecificFieldsType0):
            type_specific_fields = self.type_specific_fields.to_dict()
        else:
            type_specific_fields = self.type_specific_fields

        style_match_score: None | str
        style_match_score = self.style_match_score

        character_continuity_score: None | str
        character_continuity_score = self.character_continuity_score

        description_generated_at: None | str
        if isinstance(self.description_generated_at, datetime.datetime):
            description_generated_at = self.description_generated_at.isoformat()
        else:
            description_generated_at = self.description_generated_at

        description_generated_by: None | str
        description_generated_by = self.description_generated_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "asset_id": asset_id,
                "prompt_text": prompt_text,
                "negative_prompt": negative_prompt,
                "generation_model": generation_model,
                "generation_seed": generation_seed,
                "generation_metadata": generation_metadata,
                "character_reference_ids": character_reference_ids,
                "style_reference_ids": style_reference_ids,
                "subject": subject,
                "setting": setting,
                "mood": mood,
                "composition": composition,
                "visible_text": visible_text,
                "visible_brand_marks": visible_brand_marks,
                "characters_present": characters_present,
                "palette_hex": palette_hex,
                "type_specific_fields": type_specific_fields,
                "style_match_score": style_match_score,
                "character_continuity_score": character_continuity_score,
                "description_generated_at": description_generated_at,
                "description_generated_by": description_generated_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_description_response_generation_metadata_type_0 import (
            AssetDescriptionResponseGenerationMetadataType0,  # noqa: PLC0415
        )
        from ..models.asset_description_response_type_specific_fields_type_0 import (
            AssetDescriptionResponseTypeSpecificFieldsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        asset_id = UUID(d.pop("asset_id"))

        def _parse_prompt_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prompt_text = _parse_prompt_text(d.pop("prompt_text"))

        def _parse_negative_prompt(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        negative_prompt = _parse_negative_prompt(d.pop("negative_prompt"))

        def _parse_generation_model(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        generation_model = _parse_generation_model(d.pop("generation_model"))

        def _parse_generation_seed(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        generation_seed = _parse_generation_seed(d.pop("generation_seed"))

        def _parse_generation_metadata(data: object) -> AssetDescriptionResponseGenerationMetadataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                generation_metadata_type_0 = AssetDescriptionResponseGenerationMetadataType0.from_dict(data)

                return generation_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetDescriptionResponseGenerationMetadataType0 | None, data)

        generation_metadata = _parse_generation_metadata(d.pop("generation_metadata"))

        def _parse_character_reference_ids(data: object) -> list[UUID] | None:
            if data is None:
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
            return cast(list[UUID] | None, data)

        character_reference_ids = _parse_character_reference_ids(d.pop("character_reference_ids"))

        def _parse_style_reference_ids(data: object) -> list[UUID] | None:
            if data is None:
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
            return cast(list[UUID] | None, data)

        style_reference_ids = _parse_style_reference_ids(d.pop("style_reference_ids"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(d.pop("subject"))

        def _parse_setting(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        setting = _parse_setting(d.pop("setting"))

        def _parse_mood(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mood = _parse_mood(d.pop("mood"))

        def _parse_composition(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        composition = _parse_composition(d.pop("composition"))

        def _parse_visible_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        visible_text = _parse_visible_text(d.pop("visible_text"))

        def _parse_visible_brand_marks(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        visible_brand_marks = _parse_visible_brand_marks(d.pop("visible_brand_marks"))

        def _parse_characters_present(data: object) -> list[UUID] | None:
            if data is None:
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
            return cast(list[UUID] | None, data)

        characters_present = _parse_characters_present(d.pop("characters_present"))

        def _parse_palette_hex(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                palette_hex_type_0 = cast(list[str], data)

                return palette_hex_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        palette_hex = _parse_palette_hex(d.pop("palette_hex"))

        def _parse_type_specific_fields(data: object) -> AssetDescriptionResponseTypeSpecificFieldsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_specific_fields_type_0 = AssetDescriptionResponseTypeSpecificFieldsType0.from_dict(data)

                return type_specific_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetDescriptionResponseTypeSpecificFieldsType0 | None, data)

        type_specific_fields = _parse_type_specific_fields(d.pop("type_specific_fields"))

        def _parse_style_match_score(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        style_match_score = _parse_style_match_score(d.pop("style_match_score"))

        def _parse_character_continuity_score(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        character_continuity_score = _parse_character_continuity_score(d.pop("character_continuity_score"))

        def _parse_description_generated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                description_generated_at_type_0 = datetime.datetime.fromisoformat(data)

                return description_generated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        description_generated_at = _parse_description_generated_at(d.pop("description_generated_at"))

        def _parse_description_generated_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description_generated_by = _parse_description_generated_by(d.pop("description_generated_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        asset_description_response = cls(
            id=id,
            asset_id=asset_id,
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
            description_generated_at=description_generated_at,
            description_generated_by=description_generated_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        asset_description_response.additional_properties = d
        return asset_description_response

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
