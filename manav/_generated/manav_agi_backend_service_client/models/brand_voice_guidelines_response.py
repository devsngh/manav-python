from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brand_voice_guidelines_response_approved_synonyms_type_0 import (
        BrandVoiceGuidelinesResponseApprovedSynonymsType0,
    )
    from ..models.brand_voice_guidelines_response_example_passages_type_0_item import (
        BrandVoiceGuidelinesResponseExamplePassagesType0Item,
    )
    from ..models.brand_voice_guidelines_response_tone_attributes_type_0 import (
        BrandVoiceGuidelinesResponseToneAttributesType0,
    )


T = TypeVar("T", bound="BrandVoiceGuidelinesResponse")


@_attrs_define
class BrandVoiceGuidelinesResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        version (str):
        is_active (bool):
        voice_summary (str):
        tone_attributes (BrandVoiceGuidelinesResponseToneAttributesType0 | None):
        voice_dos (list[str] | None):
        voice_donts (list[str] | None):
        banned_phrases (list[str] | None):
        approved_synonyms (BrandVoiceGuidelinesResponseApprovedSynonymsType0 | None):
        example_passages (list[BrandVoiceGuidelinesResponseExamplePassagesType0Item] | None):
        authored_by_bot_id (None | UUID):
        approved_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        effective_from (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: UUID
    org_id: UUID
    version: str
    is_active: bool
    voice_summary: str
    tone_attributes: BrandVoiceGuidelinesResponseToneAttributesType0 | None
    voice_dos: list[str] | None
    voice_donts: list[str] | None
    banned_phrases: list[str] | None
    approved_synonyms: BrandVoiceGuidelinesResponseApprovedSynonymsType0 | None
    example_passages: list[BrandVoiceGuidelinesResponseExamplePassagesType0Item] | None
    authored_by_bot_id: None | UUID
    approved_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    effective_from: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brand_voice_guidelines_response_approved_synonyms_type_0 import (
            BrandVoiceGuidelinesResponseApprovedSynonymsType0,  # noqa: PLC0415
        )
        from ..models.brand_voice_guidelines_response_tone_attributes_type_0 import (
            BrandVoiceGuidelinesResponseToneAttributesType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        version = self.version

        is_active = self.is_active

        voice_summary = self.voice_summary

        tone_attributes: dict[str, Any] | None
        if isinstance(self.tone_attributes, BrandVoiceGuidelinesResponseToneAttributesType0):
            tone_attributes = self.tone_attributes.to_dict()
        else:
            tone_attributes = self.tone_attributes

        voice_dos: list[str] | None
        if isinstance(self.voice_dos, list):
            voice_dos = self.voice_dos

        else:
            voice_dos = self.voice_dos

        voice_donts: list[str] | None
        if isinstance(self.voice_donts, list):
            voice_donts = self.voice_donts

        else:
            voice_donts = self.voice_donts

        banned_phrases: list[str] | None
        if isinstance(self.banned_phrases, list):
            banned_phrases = self.banned_phrases

        else:
            banned_phrases = self.banned_phrases

        approved_synonyms: dict[str, Any] | None
        if isinstance(self.approved_synonyms, BrandVoiceGuidelinesResponseApprovedSynonymsType0):
            approved_synonyms = self.approved_synonyms.to_dict()
        else:
            approved_synonyms = self.approved_synonyms

        example_passages: list[dict[str, Any]] | None
        if isinstance(self.example_passages, list):
            example_passages = []
            for example_passages_type_0_item_data in self.example_passages:
                example_passages_type_0_item = example_passages_type_0_item_data.to_dict()
                example_passages.append(example_passages_type_0_item)

        else:
            example_passages = self.example_passages

        authored_by_bot_id: None | str
        if isinstance(self.authored_by_bot_id, UUID):
            authored_by_bot_id = str(self.authored_by_bot_id)
        else:
            authored_by_bot_id = self.authored_by_bot_id

        approved_by_bot_id: None | str
        if isinstance(self.approved_by_bot_id, UUID):
            approved_by_bot_id = str(self.approved_by_bot_id)
        else:
            approved_by_bot_id = self.approved_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        effective_from: None | str
        if isinstance(self.effective_from, datetime.datetime):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "version": version,
                "is_active": is_active,
                "voice_summary": voice_summary,
                "tone_attributes": tone_attributes,
                "voice_dos": voice_dos,
                "voice_donts": voice_donts,
                "banned_phrases": banned_phrases,
                "approved_synonyms": approved_synonyms,
                "example_passages": example_passages,
                "authored_by_bot_id": authored_by_bot_id,
                "approved_by_bot_id": approved_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "effective_from": effective_from,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand_voice_guidelines_response_approved_synonyms_type_0 import (
            BrandVoiceGuidelinesResponseApprovedSynonymsType0,  # noqa: PLC0415
        )
        from ..models.brand_voice_guidelines_response_example_passages_type_0_item import (
            BrandVoiceGuidelinesResponseExamplePassagesType0Item,  # noqa: PLC0415
        )
        from ..models.brand_voice_guidelines_response_tone_attributes_type_0 import (
            BrandVoiceGuidelinesResponseToneAttributesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        version = d.pop("version")

        is_active = d.pop("is_active")

        voice_summary = d.pop("voice_summary")

        def _parse_tone_attributes(data: object) -> BrandVoiceGuidelinesResponseToneAttributesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tone_attributes_type_0 = BrandVoiceGuidelinesResponseToneAttributesType0.from_dict(data)

                return tone_attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandVoiceGuidelinesResponseToneAttributesType0 | None, data)

        tone_attributes = _parse_tone_attributes(d.pop("tone_attributes"))

        def _parse_voice_dos(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voice_dos_type_0 = cast(list[str], data)

                return voice_dos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        voice_dos = _parse_voice_dos(d.pop("voice_dos"))

        def _parse_voice_donts(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                voice_donts_type_0 = cast(list[str], data)

                return voice_donts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        voice_donts = _parse_voice_donts(d.pop("voice_donts"))

        def _parse_banned_phrases(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                banned_phrases_type_0 = cast(list[str], data)

                return banned_phrases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        banned_phrases = _parse_banned_phrases(d.pop("banned_phrases"))

        def _parse_approved_synonyms(data: object) -> BrandVoiceGuidelinesResponseApprovedSynonymsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approved_synonyms_type_0 = BrandVoiceGuidelinesResponseApprovedSynonymsType0.from_dict(data)

                return approved_synonyms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BrandVoiceGuidelinesResponseApprovedSynonymsType0 | None, data)

        approved_synonyms = _parse_approved_synonyms(d.pop("approved_synonyms"))

        def _parse_example_passages(data: object) -> list[BrandVoiceGuidelinesResponseExamplePassagesType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                example_passages_type_0 = []
                _example_passages_type_0 = data
                for example_passages_type_0_item_data in _example_passages_type_0:
                    example_passages_type_0_item = BrandVoiceGuidelinesResponseExamplePassagesType0Item.from_dict(
                        example_passages_type_0_item_data
                    )

                    example_passages_type_0.append(example_passages_type_0_item)

                return example_passages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BrandVoiceGuidelinesResponseExamplePassagesType0Item] | None, data)

        example_passages = _parse_example_passages(d.pop("example_passages"))

        def _parse_authored_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authored_by_bot_id_type_0 = UUID(data)

                return authored_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        authored_by_bot_id = _parse_authored_by_bot_id(d.pop("authored_by_bot_id"))

        def _parse_approved_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_bot_id_type_0 = UUID(data)

                return approved_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_bot_id = _parse_approved_by_bot_id(d.pop("approved_by_bot_id"))

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

        def _parse_effective_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.datetime.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        effective_from = _parse_effective_from(d.pop("effective_from"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        brand_voice_guidelines_response = cls(
            id=id,
            org_id=org_id,
            version=version,
            is_active=is_active,
            voice_summary=voice_summary,
            tone_attributes=tone_attributes,
            voice_dos=voice_dos,
            voice_donts=voice_donts,
            banned_phrases=banned_phrases,
            approved_synonyms=approved_synonyms,
            example_passages=example_passages,
            authored_by_bot_id=authored_by_bot_id,
            approved_by_bot_id=approved_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            effective_from=effective_from,
            created_at=created_at,
        )

        brand_voice_guidelines_response.additional_properties = d
        return brand_voice_guidelines_response

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
