from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotScoreResponse")


@_attrs_define
class BotScoreResponse:
    """Single bot's current score + thresholds.

    Attributes:
        id (UUID):
        bot_id (UUID):
        current_score (float):
        warn_threshold (float):
        alert_threshold (float):
        intervention_threshold (float):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_recalculated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    bot_id: UUID
    current_score: float
    warn_threshold: float
    alert_threshold: float
    intervention_threshold: float
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_recalculated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bot_id = str(self.bot_id)

        current_score = self.current_score

        warn_threshold = self.warn_threshold

        alert_threshold = self.alert_threshold

        intervention_threshold = self.intervention_threshold

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_recalculated_at: None | str | Unset
        if isinstance(self.last_recalculated_at, Unset):
            last_recalculated_at = UNSET
        elif isinstance(self.last_recalculated_at, datetime.datetime):
            last_recalculated_at = self.last_recalculated_at.isoformat()
        else:
            last_recalculated_at = self.last_recalculated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_id": bot_id,
                "current_score": current_score,
                "warn_threshold": warn_threshold,
                "alert_threshold": alert_threshold,
                "intervention_threshold": intervention_threshold,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_recalculated_at is not UNSET:
            field_dict["last_recalculated_at"] = last_recalculated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_id = UUID(d.pop("bot_id"))

        current_score = d.pop("current_score")

        warn_threshold = d.pop("warn_threshold")

        alert_threshold = d.pop("alert_threshold")

        intervention_threshold = d.pop("intervention_threshold")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_last_recalculated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_recalculated_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_recalculated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_recalculated_at = _parse_last_recalculated_at(d.pop("last_recalculated_at", UNSET))

        bot_score_response = cls(
            id=id,
            bot_id=bot_id,
            current_score=current_score,
            warn_threshold=warn_threshold,
            alert_threshold=alert_threshold,
            intervention_threshold=intervention_threshold,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            last_recalculated_at=last_recalculated_at,
        )

        bot_score_response.additional_properties = d
        return bot_score_response

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
