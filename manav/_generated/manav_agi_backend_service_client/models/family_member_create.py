from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FamilyMemberCreate")


@_attrs_define
class FamilyMemberCreate:
    """
    Attributes:
        full_name (str):
        relation (None | str | Unset):
        gender (None | str | Unset):
        generation (int | None | Unset):
        parent_member_id (None | Unset | UUID):
        spouse_member_id (None | Unset | UUID):
        date_of_birth (datetime.date | None | Unset):
        date_of_death (datetime.date | None | Unset):
        is_alive (bool | Unset):  Default: True.
        photo_url (None | str | Unset):
        notes (None | str | Unset):
    """

    full_name: str
    relation: None | str | Unset = UNSET
    gender: None | str | Unset = UNSET
    generation: int | None | Unset = UNSET
    parent_member_id: None | Unset | UUID = UNSET
    spouse_member_id: None | Unset | UUID = UNSET
    date_of_birth: datetime.date | None | Unset = UNSET
    date_of_death: datetime.date | None | Unset = UNSET
    is_alive: bool | Unset = True
    photo_url: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name = self.full_name

        relation: None | str | Unset
        if isinstance(self.relation, Unset):
            relation = UNSET
        else:
            relation = self.relation

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        generation: int | None | Unset
        if isinstance(self.generation, Unset):
            generation = UNSET
        else:
            generation = self.generation

        parent_member_id: None | str | Unset
        if isinstance(self.parent_member_id, Unset):
            parent_member_id = UNSET
        elif isinstance(self.parent_member_id, UUID):
            parent_member_id = str(self.parent_member_id)
        else:
            parent_member_id = self.parent_member_id

        spouse_member_id: None | str | Unset
        if isinstance(self.spouse_member_id, Unset):
            spouse_member_id = UNSET
        elif isinstance(self.spouse_member_id, UUID):
            spouse_member_id = str(self.spouse_member_id)
        else:
            spouse_member_id = self.spouse_member_id

        date_of_birth: None | str | Unset
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        date_of_death: None | str | Unset
        if isinstance(self.date_of_death, Unset):
            date_of_death = UNSET
        elif isinstance(self.date_of_death, datetime.date):
            date_of_death = self.date_of_death.isoformat()
        else:
            date_of_death = self.date_of_death

        is_alive = self.is_alive

        photo_url: None | str | Unset
        if isinstance(self.photo_url, Unset):
            photo_url = UNSET
        else:
            photo_url = self.photo_url

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "full_name": full_name,
            }
        )
        if relation is not UNSET:
            field_dict["relation"] = relation
        if gender is not UNSET:
            field_dict["gender"] = gender
        if generation is not UNSET:
            field_dict["generation"] = generation
        if parent_member_id is not UNSET:
            field_dict["parent_member_id"] = parent_member_id
        if spouse_member_id is not UNSET:
            field_dict["spouse_member_id"] = spouse_member_id
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if date_of_death is not UNSET:
            field_dict["date_of_death"] = date_of_death
        if is_alive is not UNSET:
            field_dict["is_alive"] = is_alive
        if photo_url is not UNSET:
            field_dict["photo_url"] = photo_url
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_name = d.pop("full_name")

        def _parse_relation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation = _parse_relation(d.pop("relation", UNSET))

        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_generation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        generation = _parse_generation(d.pop("generation", UNSET))

        def _parse_parent_member_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_member_id_type_0 = UUID(data)

                return parent_member_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_member_id = _parse_parent_member_id(d.pop("parent_member_id", UNSET))

        def _parse_spouse_member_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                spouse_member_id_type_0 = UUID(data)

                return spouse_member_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        spouse_member_id = _parse_spouse_member_id(d.pop("spouse_member_id", UNSET))

        def _parse_date_of_birth(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = datetime.date.fromisoformat(data)

                return date_of_birth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_birth = _parse_date_of_birth(d.pop("date_of_birth", UNSET))

        def _parse_date_of_death(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_death_type_0 = datetime.date.fromisoformat(data)

                return date_of_death_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date_of_death = _parse_date_of_death(d.pop("date_of_death", UNSET))

        is_alive = d.pop("is_alive", UNSET)

        def _parse_photo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_url = _parse_photo_url(d.pop("photo_url", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        family_member_create = cls(
            full_name=full_name,
            relation=relation,
            gender=gender,
            generation=generation,
            parent_member_id=parent_member_id,
            spouse_member_id=spouse_member_id,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            is_alive=is_alive,
            photo_url=photo_url,
            notes=notes,
        )

        family_member_create.additional_properties = d
        return family_member_create

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
