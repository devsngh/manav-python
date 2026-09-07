from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.public_persona_response_signature_elements_type_0 import PublicPersonaResponseSignatureElementsType0


T = TypeVar("T", bound="PublicPersonaResponse")


@_attrs_define
class PublicPersonaResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        subject_type (str):
        subject_bot_id (None | UUID):
        subject_user_id (None | UUID):
        persona_name (str):
        display_title (None | str):
        bio_short (None | str):
        bio_long (None | str):
        profile_image_asset_id (None | UUID):
        voice_description (None | str):
        tone_keywords (list[str] | None):
        color_palette_hex (list[str] | None):
        signature_elements (None | PublicPersonaResponseSignatureElementsType0):
        character_reference_id (None | UUID):
        is_public (bool):
        approved_by_user_id (None | UUID):
        approved_at (datetime.datetime | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    org_id: UUID
    subject_type: str
    subject_bot_id: None | UUID
    subject_user_id: None | UUID
    persona_name: str
    display_title: None | str
    bio_short: None | str
    bio_long: None | str
    profile_image_asset_id: None | UUID
    voice_description: None | str
    tone_keywords: list[str] | None
    color_palette_hex: list[str] | None
    signature_elements: None | PublicPersonaResponseSignatureElementsType0
    character_reference_id: None | UUID
    is_public: bool
    approved_by_user_id: None | UUID
    approved_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_persona_response_signature_elements_type_0 import (
            PublicPersonaResponseSignatureElementsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        subject_type = self.subject_type

        subject_bot_id: None | str
        if isinstance(self.subject_bot_id, UUID):
            subject_bot_id = str(self.subject_bot_id)
        else:
            subject_bot_id = self.subject_bot_id

        subject_user_id: None | str
        if isinstance(self.subject_user_id, UUID):
            subject_user_id = str(self.subject_user_id)
        else:
            subject_user_id = self.subject_user_id

        persona_name = self.persona_name

        display_title: None | str
        display_title = self.display_title

        bio_short: None | str
        bio_short = self.bio_short

        bio_long: None | str
        bio_long = self.bio_long

        profile_image_asset_id: None | str
        if isinstance(self.profile_image_asset_id, UUID):
            profile_image_asset_id = str(self.profile_image_asset_id)
        else:
            profile_image_asset_id = self.profile_image_asset_id

        voice_description: None | str
        voice_description = self.voice_description

        tone_keywords: list[str] | None
        if isinstance(self.tone_keywords, list):
            tone_keywords = self.tone_keywords

        else:
            tone_keywords = self.tone_keywords

        color_palette_hex: list[str] | None
        if isinstance(self.color_palette_hex, list):
            color_palette_hex = self.color_palette_hex

        else:
            color_palette_hex = self.color_palette_hex

        signature_elements: dict[str, Any] | None
        if isinstance(self.signature_elements, PublicPersonaResponseSignatureElementsType0):
            signature_elements = self.signature_elements.to_dict()
        else:
            signature_elements = self.signature_elements

        character_reference_id: None | str
        if isinstance(self.character_reference_id, UUID):
            character_reference_id = str(self.character_reference_id)
        else:
            character_reference_id = self.character_reference_id

        is_public = self.is_public

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "subject_type": subject_type,
                "subject_bot_id": subject_bot_id,
                "subject_user_id": subject_user_id,
                "persona_name": persona_name,
                "display_title": display_title,
                "bio_short": bio_short,
                "bio_long": bio_long,
                "profile_image_asset_id": profile_image_asset_id,
                "voice_description": voice_description,
                "tone_keywords": tone_keywords,
                "color_palette_hex": color_palette_hex,
                "signature_elements": signature_elements,
                "character_reference_id": character_reference_id,
                "is_public": is_public,
                "approved_by_user_id": approved_by_user_id,
                "approved_at": approved_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_persona_response_signature_elements_type_0 import (
            PublicPersonaResponseSignatureElementsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        subject_type = d.pop("subject_type")

        def _parse_subject_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_bot_id_type_0 = UUID(data)

                return subject_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        subject_bot_id = _parse_subject_bot_id(d.pop("subject_bot_id"))

        def _parse_subject_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_user_id_type_0 = UUID(data)

                return subject_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        subject_user_id = _parse_subject_user_id(d.pop("subject_user_id"))

        persona_name = d.pop("persona_name")

        def _parse_display_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_title = _parse_display_title(d.pop("display_title"))

        def _parse_bio_short(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio_short = _parse_bio_short(d.pop("bio_short"))

        def _parse_bio_long(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio_long = _parse_bio_long(d.pop("bio_long"))

        def _parse_profile_image_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_image_asset_id_type_0 = UUID(data)

                return profile_image_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        profile_image_asset_id = _parse_profile_image_asset_id(d.pop("profile_image_asset_id"))

        def _parse_voice_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        voice_description = _parse_voice_description(d.pop("voice_description"))

        def _parse_tone_keywords(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tone_keywords_type_0 = cast(list[str], data)

                return tone_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tone_keywords = _parse_tone_keywords(d.pop("tone_keywords"))

        def _parse_color_palette_hex(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                color_palette_hex_type_0 = cast(list[str], data)

                return color_palette_hex_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        color_palette_hex = _parse_color_palette_hex(d.pop("color_palette_hex"))

        def _parse_signature_elements(data: object) -> None | PublicPersonaResponseSignatureElementsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signature_elements_type_0 = PublicPersonaResponseSignatureElementsType0.from_dict(data)

                return signature_elements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicPersonaResponseSignatureElementsType0, data)

        signature_elements = _parse_signature_elements(d.pop("signature_elements"))

        def _parse_character_reference_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                character_reference_id_type_0 = UUID(data)

                return character_reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        character_reference_id = _parse_character_reference_id(d.pop("character_reference_id"))

        is_public = d.pop("is_public")

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        def _parse_approved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        approved_at = _parse_approved_at(d.pop("approved_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        public_persona_response = cls(
            id=id,
            org_id=org_id,
            subject_type=subject_type,
            subject_bot_id=subject_bot_id,
            subject_user_id=subject_user_id,
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
            is_public=is_public,
            approved_by_user_id=approved_by_user_id,
            approved_at=approved_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        public_persona_response.additional_properties = d
        return public_persona_response

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
