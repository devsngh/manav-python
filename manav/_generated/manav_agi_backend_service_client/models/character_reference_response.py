from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CharacterReferenceResponse")


@_attrs_define
class CharacterReferenceResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        character_name (str):
        subject_type (str):
        subject_bot_id (None | UUID):
        subject_user_id (None | UUID):
        subject_persona_id (None | UUID):
        reference_image_asset_ids (list[UUID] | None):
        wardrobe_notes (None | str):
        appearance_notes (None | str):
        voice_notes (None | str):
        motion_notes (None | str):
        version (str):
        is_active (bool):
        parent_reference_id (None | UUID):
        approved_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        approved_at (datetime.datetime | None):
        created_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
    """

    id: UUID
    org_id: UUID
    character_name: str
    subject_type: str
    subject_bot_id: None | UUID
    subject_user_id: None | UUID
    subject_persona_id: None | UUID
    reference_image_asset_ids: list[UUID] | None
    wardrobe_notes: None | str
    appearance_notes: None | str
    voice_notes: None | str
    motion_notes: None | str
    version: str
    is_active: bool
    parent_reference_id: None | UUID
    approved_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    approved_at: datetime.datetime | None
    created_at: datetime.datetime
    deleted_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        character_name = self.character_name

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

        subject_persona_id: None | str
        if isinstance(self.subject_persona_id, UUID):
            subject_persona_id = str(self.subject_persona_id)
        else:
            subject_persona_id = self.subject_persona_id

        reference_image_asset_ids: list[str] | None
        if isinstance(self.reference_image_asset_ids, list):
            reference_image_asset_ids = []
            for reference_image_asset_ids_type_0_item_data in self.reference_image_asset_ids:
                reference_image_asset_ids_type_0_item = str(reference_image_asset_ids_type_0_item_data)
                reference_image_asset_ids.append(reference_image_asset_ids_type_0_item)

        else:
            reference_image_asset_ids = self.reference_image_asset_ids

        wardrobe_notes: None | str
        wardrobe_notes = self.wardrobe_notes

        appearance_notes: None | str
        appearance_notes = self.appearance_notes

        voice_notes: None | str
        voice_notes = self.voice_notes

        motion_notes: None | str
        motion_notes = self.motion_notes

        version = self.version

        is_active = self.is_active

        parent_reference_id: None | str
        if isinstance(self.parent_reference_id, UUID):
            parent_reference_id = str(self.parent_reference_id)
        else:
            parent_reference_id = self.parent_reference_id

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

        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        created_at = self.created_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "character_name": character_name,
                "subject_type": subject_type,
                "subject_bot_id": subject_bot_id,
                "subject_user_id": subject_user_id,
                "subject_persona_id": subject_persona_id,
                "reference_image_asset_ids": reference_image_asset_ids,
                "wardrobe_notes": wardrobe_notes,
                "appearance_notes": appearance_notes,
                "voice_notes": voice_notes,
                "motion_notes": motion_notes,
                "version": version,
                "is_active": is_active,
                "parent_reference_id": parent_reference_id,
                "approved_by_bot_id": approved_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "approved_at": approved_at,
                "created_at": created_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        character_name = d.pop("character_name")

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

        def _parse_subject_persona_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_persona_id_type_0 = UUID(data)

                return subject_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        subject_persona_id = _parse_subject_persona_id(d.pop("subject_persona_id"))

        def _parse_reference_image_asset_ids(data: object) -> list[UUID] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reference_image_asset_ids_type_0 = []
                _reference_image_asset_ids_type_0 = data
                for reference_image_asset_ids_type_0_item_data in _reference_image_asset_ids_type_0:
                    reference_image_asset_ids_type_0_item = UUID(reference_image_asset_ids_type_0_item_data)

                    reference_image_asset_ids_type_0.append(reference_image_asset_ids_type_0_item)

                return reference_image_asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None, data)

        reference_image_asset_ids = _parse_reference_image_asset_ids(d.pop("reference_image_asset_ids"))

        def _parse_wardrobe_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        wardrobe_notes = _parse_wardrobe_notes(d.pop("wardrobe_notes"))

        def _parse_appearance_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        appearance_notes = _parse_appearance_notes(d.pop("appearance_notes"))

        def _parse_voice_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        voice_notes = _parse_voice_notes(d.pop("voice_notes"))

        def _parse_motion_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        motion_notes = _parse_motion_notes(d.pop("motion_notes"))

        version = d.pop("version")

        is_active = d.pop("is_active")

        def _parse_parent_reference_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_reference_id_type_0 = UUID(data)

                return parent_reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_reference_id = _parse_parent_reference_id(d.pop("parent_reference_id"))

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

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        character_reference_response = cls(
            id=id,
            org_id=org_id,
            character_name=character_name,
            subject_type=subject_type,
            subject_bot_id=subject_bot_id,
            subject_user_id=subject_user_id,
            subject_persona_id=subject_persona_id,
            reference_image_asset_ids=reference_image_asset_ids,
            wardrobe_notes=wardrobe_notes,
            appearance_notes=appearance_notes,
            voice_notes=voice_notes,
            motion_notes=motion_notes,
            version=version,
            is_active=is_active,
            parent_reference_id=parent_reference_id,
            approved_by_bot_id=approved_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            approved_at=approved_at,
            created_at=created_at,
            deleted_at=deleted_at,
        )

        character_reference_response.additional_properties = d
        return character_reference_response

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
