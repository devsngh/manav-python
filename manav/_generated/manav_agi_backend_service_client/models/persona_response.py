from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.persona_response_content_preferences_type_0 import PersonaResponseContentPreferencesType0
    from ..models.persona_response_demographics_type_0 import PersonaResponseDemographicsType0
    from ..models.persona_response_psychographics_type_0 import PersonaResponsePsychographicsType0


T = TypeVar("T", bound="PersonaResponse")


@_attrs_define
class PersonaResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        archetype_label (None | str):
        age_range (None | str):
        geography (None | str):
        role_title (None | str):
        demographics (None | PersonaResponseDemographicsType0):
        psychographics (None | PersonaResponsePsychographicsType0):
        pain_points (list[str] | None):
        goals (list[str] | None):
        preferred_channels (list[str] | None):
        content_preferences (None | PersonaResponseContentPreferencesType0):
        buying_committee_role (None | str):
        tier (None | str):
        status (str):
        authored_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
    """

    id: UUID
    org_id: UUID
    name: str
    archetype_label: None | str
    age_range: None | str
    geography: None | str
    role_title: None | str
    demographics: None | PersonaResponseDemographicsType0
    psychographics: None | PersonaResponsePsychographicsType0
    pain_points: list[str] | None
    goals: list[str] | None
    preferred_channels: list[str] | None
    content_preferences: None | PersonaResponseContentPreferencesType0
    buying_committee_role: None | str
    tier: None | str
    status: str
    authored_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.persona_response_content_preferences_type_0 import (
            PersonaResponseContentPreferencesType0,  # noqa: PLC0415
        )
        from ..models.persona_response_demographics_type_0 import PersonaResponseDemographicsType0  # noqa: PLC0415
        from ..models.persona_response_psychographics_type_0 import PersonaResponsePsychographicsType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        archetype_label: None | str
        archetype_label = self.archetype_label

        age_range: None | str
        age_range = self.age_range

        geography: None | str
        geography = self.geography

        role_title: None | str
        role_title = self.role_title

        demographics: dict[str, Any] | None
        if isinstance(self.demographics, PersonaResponseDemographicsType0):
            demographics = self.demographics.to_dict()
        else:
            demographics = self.demographics

        psychographics: dict[str, Any] | None
        if isinstance(self.psychographics, PersonaResponsePsychographicsType0):
            psychographics = self.psychographics.to_dict()
        else:
            psychographics = self.psychographics

        pain_points: list[str] | None
        if isinstance(self.pain_points, list):
            pain_points = self.pain_points

        else:
            pain_points = self.pain_points

        goals: list[str] | None
        if isinstance(self.goals, list):
            goals = self.goals

        else:
            goals = self.goals

        preferred_channels: list[str] | None
        if isinstance(self.preferred_channels, list):
            preferred_channels = self.preferred_channels

        else:
            preferred_channels = self.preferred_channels

        content_preferences: dict[str, Any] | None
        if isinstance(self.content_preferences, PersonaResponseContentPreferencesType0):
            content_preferences = self.content_preferences.to_dict()
        else:
            content_preferences = self.content_preferences

        buying_committee_role: None | str
        buying_committee_role = self.buying_committee_role

        tier: None | str
        tier = self.tier

        status = self.status

        authored_by_bot_id: None | str
        if isinstance(self.authored_by_bot_id, UUID):
            authored_by_bot_id = str(self.authored_by_bot_id)
        else:
            authored_by_bot_id = self.authored_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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
                "name": name,
                "archetype_label": archetype_label,
                "age_range": age_range,
                "geography": geography,
                "role_title": role_title,
                "demographics": demographics,
                "psychographics": psychographics,
                "pain_points": pain_points,
                "goals": goals,
                "preferred_channels": preferred_channels,
                "content_preferences": content_preferences,
                "buying_committee_role": buying_committee_role,
                "tier": tier,
                "status": status,
                "authored_by_bot_id": authored_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persona_response_content_preferences_type_0 import (
            PersonaResponseContentPreferencesType0,  # noqa: PLC0415
        )
        from ..models.persona_response_demographics_type_0 import PersonaResponseDemographicsType0  # noqa: PLC0415
        from ..models.persona_response_psychographics_type_0 import PersonaResponsePsychographicsType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        def _parse_archetype_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        archetype_label = _parse_archetype_label(d.pop("archetype_label"))

        def _parse_age_range(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        age_range = _parse_age_range(d.pop("age_range"))

        def _parse_geography(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        geography = _parse_geography(d.pop("geography"))

        def _parse_role_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        role_title = _parse_role_title(d.pop("role_title"))

        def _parse_demographics(data: object) -> None | PersonaResponseDemographicsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                demographics_type_0 = PersonaResponseDemographicsType0.from_dict(data)

                return demographics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonaResponseDemographicsType0, data)

        demographics = _parse_demographics(d.pop("demographics"))

        def _parse_psychographics(data: object) -> None | PersonaResponsePsychographicsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                psychographics_type_0 = PersonaResponsePsychographicsType0.from_dict(data)

                return psychographics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonaResponsePsychographicsType0, data)

        psychographics = _parse_psychographics(d.pop("psychographics"))

        def _parse_pain_points(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pain_points_type_0 = cast(list[str], data)

                return pain_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        pain_points = _parse_pain_points(d.pop("pain_points"))

        def _parse_goals(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                goals_type_0 = cast(list[str], data)

                return goals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        goals = _parse_goals(d.pop("goals"))

        def _parse_preferred_channels(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                preferred_channels_type_0 = cast(list[str], data)

                return preferred_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        preferred_channels = _parse_preferred_channels(d.pop("preferred_channels"))

        def _parse_content_preferences(data: object) -> None | PersonaResponseContentPreferencesType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_preferences_type_0 = PersonaResponseContentPreferencesType0.from_dict(data)

                return content_preferences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PersonaResponseContentPreferencesType0, data)

        content_preferences = _parse_content_preferences(d.pop("content_preferences"))

        def _parse_buying_committee_role(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        buying_committee_role = _parse_buying_committee_role(d.pop("buying_committee_role"))

        def _parse_tier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier = _parse_tier(d.pop("tier"))

        status = d.pop("status")

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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        persona_response = cls(
            id=id,
            org_id=org_id,
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
            authored_by_bot_id=authored_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        persona_response.additional_properties = d
        return persona_response

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
