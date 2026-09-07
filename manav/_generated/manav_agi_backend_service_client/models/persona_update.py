from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.persona_update_content_preferences_type_0 import PersonaUpdateContentPreferencesType0
    from ..models.persona_update_demographics_type_0 import PersonaUpdateDemographicsType0
    from ..models.persona_update_psychographics_type_0 import PersonaUpdatePsychographicsType0


T = TypeVar("T", bound="PersonaUpdate")


@_attrs_define
class PersonaUpdate:
    """
    Attributes:
        name (None | str | Unset):
        archetype_label (None | str | Unset):
        age_range (None | str | Unset):
        geography (None | str | Unset):
        role_title (None | str | Unset):
        demographics (None | PersonaUpdateDemographicsType0 | Unset):
        psychographics (None | PersonaUpdatePsychographicsType0 | Unset):
        pain_points (list[str] | None | Unset):
        goals (list[str] | None | Unset):
        preferred_channels (list[str] | None | Unset):
        content_preferences (None | PersonaUpdateContentPreferencesType0 | Unset):
        buying_committee_role (None | str | Unset):
        tier (None | str | Unset):
        status (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    archetype_label: None | str | Unset = UNSET
    age_range: None | str | Unset = UNSET
    geography: None | str | Unset = UNSET
    role_title: None | str | Unset = UNSET
    demographics: None | PersonaUpdateDemographicsType0 | Unset = UNSET
    psychographics: None | PersonaUpdatePsychographicsType0 | Unset = UNSET
    pain_points: list[str] | None | Unset = UNSET
    goals: list[str] | None | Unset = UNSET
    preferred_channels: list[str] | None | Unset = UNSET
    content_preferences: None | PersonaUpdateContentPreferencesType0 | Unset = UNSET
    buying_committee_role: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.persona_update_content_preferences_type_0 import (
            PersonaUpdateContentPreferencesType0,  # noqa: PLC0415
        )
        from ..models.persona_update_demographics_type_0 import PersonaUpdateDemographicsType0  # noqa: PLC0415
        from ..models.persona_update_psychographics_type_0 import PersonaUpdatePsychographicsType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        archetype_label: None | str | Unset
        if isinstance(self.archetype_label, Unset):
            archetype_label = UNSET
        else:
            archetype_label = self.archetype_label

        age_range: None | str | Unset
        if isinstance(self.age_range, Unset):
            age_range = UNSET
        else:
            age_range = self.age_range

        geography: None | str | Unset
        if isinstance(self.geography, Unset):
            geography = UNSET
        else:
            geography = self.geography

        role_title: None | str | Unset
        if isinstance(self.role_title, Unset):
            role_title = UNSET
        else:
            role_title = self.role_title

        demographics: dict[str, Any] | None | Unset
        if isinstance(self.demographics, Unset):
            demographics = UNSET
        elif isinstance(self.demographics, PersonaUpdateDemographicsType0):
            demographics = self.demographics.to_dict()
        else:
            demographics = self.demographics

        psychographics: dict[str, Any] | None | Unset
        if isinstance(self.psychographics, Unset):
            psychographics = UNSET
        elif isinstance(self.psychographics, PersonaUpdatePsychographicsType0):
            psychographics = self.psychographics.to_dict()
        else:
            psychographics = self.psychographics

        pain_points: list[str] | None | Unset
        if isinstance(self.pain_points, Unset):
            pain_points = UNSET
        elif isinstance(self.pain_points, list):
            pain_points = self.pain_points

        else:
            pain_points = self.pain_points

        goals: list[str] | None | Unset
        if isinstance(self.goals, Unset):
            goals = UNSET
        elif isinstance(self.goals, list):
            goals = self.goals

        else:
            goals = self.goals

        preferred_channels: list[str] | None | Unset
        if isinstance(self.preferred_channels, Unset):
            preferred_channels = UNSET
        elif isinstance(self.preferred_channels, list):
            preferred_channels = self.preferred_channels

        else:
            preferred_channels = self.preferred_channels

        content_preferences: dict[str, Any] | None | Unset
        if isinstance(self.content_preferences, Unset):
            content_preferences = UNSET
        elif isinstance(self.content_preferences, PersonaUpdateContentPreferencesType0):
            content_preferences = self.content_preferences.to_dict()
        else:
            content_preferences = self.content_preferences

        buying_committee_role: None | str | Unset
        if isinstance(self.buying_committee_role, Unset):
            buying_committee_role = UNSET
        else:
            buying_committee_role = self.buying_committee_role

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if archetype_label is not UNSET:
            field_dict["archetype_label"] = archetype_label
        if age_range is not UNSET:
            field_dict["age_range"] = age_range
        if geography is not UNSET:
            field_dict["geography"] = geography
        if role_title is not UNSET:
            field_dict["role_title"] = role_title
        if demographics is not UNSET:
            field_dict["demographics"] = demographics
        if psychographics is not UNSET:
            field_dict["psychographics"] = psychographics
        if pain_points is not UNSET:
            field_dict["pain_points"] = pain_points
        if goals is not UNSET:
            field_dict["goals"] = goals
        if preferred_channels is not UNSET:
            field_dict["preferred_channels"] = preferred_channels
        if content_preferences is not UNSET:
            field_dict["content_preferences"] = content_preferences
        if buying_committee_role is not UNSET:
            field_dict["buying_committee_role"] = buying_committee_role
        if tier is not UNSET:
            field_dict["tier"] = tier
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persona_update_content_preferences_type_0 import (
            PersonaUpdateContentPreferencesType0,  # noqa: PLC0415
        )
        from ..models.persona_update_demographics_type_0 import PersonaUpdateDemographicsType0  # noqa: PLC0415
        from ..models.persona_update_psychographics_type_0 import PersonaUpdatePsychographicsType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_archetype_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archetype_label = _parse_archetype_label(d.pop("archetype_label", UNSET))

        def _parse_age_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age_range = _parse_age_range(d.pop("age_range", UNSET))

        def _parse_geography(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geography = _parse_geography(d.pop("geography", UNSET))

        def _parse_role_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_title = _parse_role_title(d.pop("role_title", UNSET))

        def _parse_demographics(data: object) -> None | PersonaUpdateDemographicsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                demographics_type_0 = PersonaUpdateDemographicsType0.from_dict(data)

                return demographics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonaUpdateDemographicsType0 | Unset, data)

        demographics = _parse_demographics(d.pop("demographics", UNSET))

        def _parse_psychographics(data: object) -> None | PersonaUpdatePsychographicsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                psychographics_type_0 = PersonaUpdatePsychographicsType0.from_dict(data)

                return psychographics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonaUpdatePsychographicsType0 | Unset, data)

        psychographics = _parse_psychographics(d.pop("psychographics", UNSET))

        def _parse_pain_points(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pain_points_type_0 = cast(list[str], data)

                return pain_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        pain_points = _parse_pain_points(d.pop("pain_points", UNSET))

        def _parse_goals(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                goals_type_0 = cast(list[str], data)

                return goals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        goals = _parse_goals(d.pop("goals", UNSET))

        def _parse_preferred_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                preferred_channels_type_0 = cast(list[str], data)

                return preferred_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        preferred_channels = _parse_preferred_channels(d.pop("preferred_channels", UNSET))

        def _parse_content_preferences(data: object) -> None | PersonaUpdateContentPreferencesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_preferences_type_0 = PersonaUpdateContentPreferencesType0.from_dict(data)

                return content_preferences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonaUpdateContentPreferencesType0 | Unset, data)

        content_preferences = _parse_content_preferences(d.pop("content_preferences", UNSET))

        def _parse_buying_committee_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buying_committee_role = _parse_buying_committee_role(d.pop("buying_committee_role", UNSET))

        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        persona_update = cls(
            name=name,
            archetype_label=archetype_label,
            age_range=age_range,
            geography=geography,
            role_title=role_title,
            demographics=demographics,
            psychographics=psychographics,
            pain_points=pain_points,
            goals=goals,
            preferred_channels=preferred_channels,
            content_preferences=content_preferences,
            buying_committee_role=buying_committee_role,
            tier=tier,
            status=status,
        )

        persona_update.additional_properties = d
        return persona_update

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
