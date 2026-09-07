from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_persona_update_signature_elements_type_0 import PublicPersonaUpdateSignatureElementsType0


T = TypeVar("T", bound="PublicPersonaUpdate")


@_attrs_define
class PublicPersonaUpdate:
    """
    Attributes:
        persona_name (None | str | Unset):
        display_title (None | str | Unset):
        bio_short (None | str | Unset):
        bio_long (None | str | Unset):
        profile_image_asset_id (None | Unset | UUID):
        voice_description (None | str | Unset):
        tone_keywords (list[str] | None | Unset):
        color_palette_hex (list[str] | None | Unset):
        signature_elements (None | PublicPersonaUpdateSignatureElementsType0 | Unset):
        character_reference_id (None | Unset | UUID):
    """

    persona_name: None | str | Unset = UNSET
    display_title: None | str | Unset = UNSET
    bio_short: None | str | Unset = UNSET
    bio_long: None | str | Unset = UNSET
    profile_image_asset_id: None | Unset | UUID = UNSET
    voice_description: None | str | Unset = UNSET
    tone_keywords: list[str] | None | Unset = UNSET
    color_palette_hex: list[str] | None | Unset = UNSET
    signature_elements: None | PublicPersonaUpdateSignatureElementsType0 | Unset = UNSET
    character_reference_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_persona_update_signature_elements_type_0 import (
            PublicPersonaUpdateSignatureElementsType0,  # noqa: PLC0415
        )

        persona_name: None | str | Unset
        if isinstance(self.persona_name, Unset):
            persona_name = UNSET
        else:
            persona_name = self.persona_name

        display_title: None | str | Unset
        if isinstance(self.display_title, Unset):
            display_title = UNSET
        else:
            display_title = self.display_title

        bio_short: None | str | Unset
        if isinstance(self.bio_short, Unset):
            bio_short = UNSET
        else:
            bio_short = self.bio_short

        bio_long: None | str | Unset
        if isinstance(self.bio_long, Unset):
            bio_long = UNSET
        else:
            bio_long = self.bio_long

        profile_image_asset_id: None | str | Unset
        if isinstance(self.profile_image_asset_id, Unset):
            profile_image_asset_id = UNSET
        elif isinstance(self.profile_image_asset_id, UUID):
            profile_image_asset_id = str(self.profile_image_asset_id)
        else:
            profile_image_asset_id = self.profile_image_asset_id

        voice_description: None | str | Unset
        if isinstance(self.voice_description, Unset):
            voice_description = UNSET
        else:
            voice_description = self.voice_description

        tone_keywords: list[str] | None | Unset
        if isinstance(self.tone_keywords, Unset):
            tone_keywords = UNSET
        elif isinstance(self.tone_keywords, list):
            tone_keywords = self.tone_keywords

        else:
            tone_keywords = self.tone_keywords

        color_palette_hex: list[str] | None | Unset
        if isinstance(self.color_palette_hex, Unset):
            color_palette_hex = UNSET
        elif isinstance(self.color_palette_hex, list):
            color_palette_hex = self.color_palette_hex

        else:
            color_palette_hex = self.color_palette_hex

        signature_elements: dict[str, Any] | None | Unset
        if isinstance(self.signature_elements, Unset):
            signature_elements = UNSET
        elif isinstance(self.signature_elements, PublicPersonaUpdateSignatureElementsType0):
            signature_elements = self.signature_elements.to_dict()
        else:
            signature_elements = self.signature_elements

        character_reference_id: None | str | Unset
        if isinstance(self.character_reference_id, Unset):
            character_reference_id = UNSET
        elif isinstance(self.character_reference_id, UUID):
            character_reference_id = str(self.character_reference_id)
        else:
            character_reference_id = self.character_reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if persona_name is not UNSET:
            field_dict["persona_name"] = persona_name
        if display_title is not UNSET:
            field_dict["display_title"] = display_title
        if bio_short is not UNSET:
            field_dict["bio_short"] = bio_short
        if bio_long is not UNSET:
            field_dict["bio_long"] = bio_long
        if profile_image_asset_id is not UNSET:
            field_dict["profile_image_asset_id"] = profile_image_asset_id
        if voice_description is not UNSET:
            field_dict["voice_description"] = voice_description
        if tone_keywords is not UNSET:
            field_dict["tone_keywords"] = tone_keywords
        if color_palette_hex is not UNSET:
            field_dict["color_palette_hex"] = color_palette_hex
        if signature_elements is not UNSET:
            field_dict["signature_elements"] = signature_elements
        if character_reference_id is not UNSET:
            field_dict["character_reference_id"] = character_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_persona_update_signature_elements_type_0 import (
            PublicPersonaUpdateSignatureElementsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_persona_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        persona_name = _parse_persona_name(d.pop("persona_name", UNSET))

        def _parse_display_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_title = _parse_display_title(d.pop("display_title", UNSET))

        def _parse_bio_short(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio_short = _parse_bio_short(d.pop("bio_short", UNSET))

        def _parse_bio_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio_long = _parse_bio_long(d.pop("bio_long", UNSET))

        def _parse_profile_image_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_image_asset_id_type_0 = UUID(data)

                return profile_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        profile_image_asset_id = _parse_profile_image_asset_id(d.pop("profile_image_asset_id", UNSET))

        def _parse_voice_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_description = _parse_voice_description(d.pop("voice_description", UNSET))

        def _parse_tone_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tone_keywords_type_0 = cast(list[str], data)

                return tone_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tone_keywords = _parse_tone_keywords(d.pop("tone_keywords", UNSET))

        def _parse_color_palette_hex(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                color_palette_hex_type_0 = cast(list[str], data)

                return color_palette_hex_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        color_palette_hex = _parse_color_palette_hex(d.pop("color_palette_hex", UNSET))

        def _parse_signature_elements(data: object) -> None | PublicPersonaUpdateSignatureElementsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signature_elements_type_0 = PublicPersonaUpdateSignatureElementsType0.from_dict(data)

                return signature_elements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicPersonaUpdateSignatureElementsType0 | Unset, data)

        signature_elements = _parse_signature_elements(d.pop("signature_elements", UNSET))

        def _parse_character_reference_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                character_reference_id_type_0 = UUID(data)

                return character_reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        character_reference_id = _parse_character_reference_id(d.pop("character_reference_id", UNSET))

        public_persona_update = cls(
            persona_name=persona_name,
            display_title=display_title,
            bio_short=bio_short,
            bio_long=bio_long,
            profile_image_asset_id=profile_image_asset_id,
            voice_description=voice_description,
            tone_keywords=tone_keywords,
            color_palette_hex=color_palette_hex,
            signature_elements=signature_elements,
            character_reference_id=character_reference_id,
        )

        public_persona_update.additional_properties = d
        return public_persona_update

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
