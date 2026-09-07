from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CharacterReferenceUpdate")


@_attrs_define
class CharacterReferenceUpdate:
    """
    Attributes:
        reference_image_asset_ids (list[UUID] | None | Unset):
        face_embedding_vector (list[float] | None | Unset):
        wardrobe_notes (None | str | Unset):
        appearance_notes (None | str | Unset):
        voice_notes (None | str | Unset):
        motion_notes (None | str | Unset):
        is_active (bool | None | Unset):
    """

    reference_image_asset_ids: list[UUID] | None | Unset = UNSET
    face_embedding_vector: list[float] | None | Unset = UNSET
    wardrobe_notes: None | str | Unset = UNSET
    appearance_notes: None | str | Unset = UNSET
    voice_notes: None | str | Unset = UNSET
    motion_notes: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        character_reference_update = cls(
            reference_image_asset_ids=reference_image_asset_ids,
            face_embedding_vector=face_embedding_vector,
            wardrobe_notes=wardrobe_notes,
            appearance_notes=appearance_notes,
            voice_notes=voice_notes,
            motion_notes=motion_notes,
            is_active=is_active,
        )

        character_reference_update.additional_properties = d
        return character_reference_update

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
