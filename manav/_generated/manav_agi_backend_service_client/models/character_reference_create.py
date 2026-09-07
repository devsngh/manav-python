from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CharacterReferenceCreate")


@_attrs_define
class CharacterReferenceCreate:
    """
    Attributes:
        character_name (str):
        subject_type (str): bot / human / fictional_persona
        version (str):
        subject_bot_id (None | Unset | UUID):
        subject_user_id (None | Unset | UUID):
        subject_persona_id (None | Unset | UUID):
        reference_image_asset_ids (list[UUID] | None | Unset):
        face_embedding_vector (list[float] | None | Unset):
        wardrobe_notes (None | str | Unset):
        appearance_notes (None | str | Unset):
        voice_notes (None | str | Unset):
        motion_notes (None | str | Unset):
        is_active (bool | Unset):  Default: True.
        parent_reference_id (None | Unset | UUID):
    """

    character_name: str
    subject_type: str
    version: str
    subject_bot_id: None | Unset | UUID = UNSET
    subject_user_id: None | Unset | UUID = UNSET
    subject_persona_id: None | Unset | UUID = UNSET
    reference_image_asset_ids: list[UUID] | None | Unset = UNSET
    face_embedding_vector: list[float] | None | Unset = UNSET
    wardrobe_notes: None | str | Unset = UNSET
    appearance_notes: None | str | Unset = UNSET
    voice_notes: None | str | Unset = UNSET
    motion_notes: None | str | Unset = UNSET
    is_active: bool | Unset = True
    parent_reference_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        character_name = self.character_name

        subject_type = self.subject_type

        version = self.version

        subject_bot_id: None | str | Unset
        if isinstance(self.subject_bot_id, Unset):
            subject_bot_id = UNSET
        elif isinstance(self.subject_bot_id, UUID):
            subject_bot_id = str(self.subject_bot_id)
        else:
            subject_bot_id = self.subject_bot_id

        subject_user_id: None | str | Unset
        if isinstance(self.subject_user_id, Unset):
            subject_user_id = UNSET
        elif isinstance(self.subject_user_id, UUID):
            subject_user_id = str(self.subject_user_id)
        else:
            subject_user_id = self.subject_user_id

        subject_persona_id: None | str | Unset
        if isinstance(self.subject_persona_id, Unset):
            subject_persona_id = UNSET
        elif isinstance(self.subject_persona_id, UUID):
            subject_persona_id = str(self.subject_persona_id)
        else:
            subject_persona_id = self.subject_persona_id

        reference_image_asset_ids: list[str] | None | Unset
        if isinstance(self.reference_image_asset_ids, Unset):
            reference_image_asset_ids = UNSET
        elif isinstance(self.reference_image_asset_ids, list):
            reference_image_asset_ids = []
            for reference_image_asset_ids_type_0_item_data in self.reference_image_asset_ids:
                reference_image_asset_ids_type_0_item = str(reference_image_asset_ids_type_0_item_data)
                reference_image_asset_ids.append(reference_image_asset_ids_type_0_item)

        else:
            reference_image_asset_ids = self.reference_image_asset_ids

        face_embedding_vector: list[float] | None | Unset
        if isinstance(self.face_embedding_vector, Unset):
            face_embedding_vector = UNSET
        elif isinstance(self.face_embedding_vector, list):
            face_embedding_vector = self.face_embedding_vector

        else:
            face_embedding_vector = self.face_embedding_vector

        wardrobe_notes: None | str | Unset
        if isinstance(self.wardrobe_notes, Unset):
            wardrobe_notes = UNSET
        else:
            wardrobe_notes = self.wardrobe_notes

        appearance_notes: None | str | Unset
        if isinstance(self.appearance_notes, Unset):
            appearance_notes = UNSET
        else:
            appearance_notes = self.appearance_notes

        voice_notes: None | str | Unset
        if isinstance(self.voice_notes, Unset):
            voice_notes = UNSET
        else:
            voice_notes = self.voice_notes

        motion_notes: None | str | Unset
        if isinstance(self.motion_notes, Unset):
            motion_notes = UNSET
        else:
            motion_notes = self.motion_notes

        is_active = self.is_active

        parent_reference_id: None | str | Unset
        if isinstance(self.parent_reference_id, Unset):
            parent_reference_id = UNSET
        elif isinstance(self.parent_reference_id, UUID):
            parent_reference_id = str(self.parent_reference_id)
        else:
            parent_reference_id = self.parent_reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "character_name": character_name,
                "subject_type": subject_type,
                "version": version,
            }
        )
        if subject_bot_id is not UNSET:
            field_dict["subject_bot_id"] = subject_bot_id
        if subject_user_id is not UNSET:
            field_dict["subject_user_id"] = subject_user_id
        if subject_persona_id is not UNSET:
            field_dict["subject_persona_id"] = subject_persona_id
        if reference_image_asset_ids is not UNSET:
            field_dict["reference_image_asset_ids"] = reference_image_asset_ids
        if face_embedding_vector is not UNSET:
            field_dict["face_embedding_vector"] = face_embedding_vector
        if wardrobe_notes is not UNSET:
            field_dict["wardrobe_notes"] = wardrobe_notes
        if appearance_notes is not UNSET:
            field_dict["appearance_notes"] = appearance_notes
        if voice_notes is not UNSET:
            field_dict["voice_notes"] = voice_notes
        if motion_notes is not UNSET:
            field_dict["motion_notes"] = motion_notes
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if parent_reference_id is not UNSET:
            field_dict["parent_reference_id"] = parent_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        character_name = d.pop("character_name")

        subject_type = d.pop("subject_type")

        version = d.pop("version")

        def _parse_subject_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_bot_id_type_0 = UUID(data)

                return subject_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subject_bot_id = _parse_subject_bot_id(d.pop("subject_bot_id", UNSET))

        def _parse_subject_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_user_id_type_0 = UUID(data)

                return subject_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subject_user_id = _parse_subject_user_id(d.pop("subject_user_id", UNSET))

        def _parse_subject_persona_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subject_persona_id_type_0 = UUID(data)

                return subject_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subject_persona_id = _parse_subject_persona_id(d.pop("subject_persona_id", UNSET))

        def _parse_reference_image_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(list[UUID] | None | Unset, data)

        reference_image_asset_ids = _parse_reference_image_asset_ids(d.pop("reference_image_asset_ids", UNSET))

        def _parse_face_embedding_vector(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                face_embedding_vector_type_0 = cast(list[float], data)

                return face_embedding_vector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        face_embedding_vector = _parse_face_embedding_vector(d.pop("face_embedding_vector", UNSET))

        def _parse_wardrobe_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wardrobe_notes = _parse_wardrobe_notes(d.pop("wardrobe_notes", UNSET))

        def _parse_appearance_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appearance_notes = _parse_appearance_notes(d.pop("appearance_notes", UNSET))

        def _parse_voice_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_notes = _parse_voice_notes(d.pop("voice_notes", UNSET))

        def _parse_motion_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        motion_notes = _parse_motion_notes(d.pop("motion_notes", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_parent_reference_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_reference_id_type_0 = UUID(data)

                return parent_reference_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_reference_id = _parse_parent_reference_id(d.pop("parent_reference_id", UNSET))

        character_reference_create = cls(
            character_name=character_name,
            subject_type=subject_type,
            version=version,
            subject_bot_id=subject_bot_id,
            subject_user_id=subject_user_id,
            subject_persona_id=subject_persona_id,
            reference_image_asset_ids=reference_image_asset_ids,
            face_embedding_vector=face_embedding_vector,
            wardrobe_notes=wardrobe_notes,
            appearance_notes=appearance_notes,
            voice_notes=voice_notes,
            motion_notes=motion_notes,
            is_active=is_active,
            parent_reference_id=parent_reference_id,
        )

        character_reference_create.additional_properties = d
        return character_reference_create

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
