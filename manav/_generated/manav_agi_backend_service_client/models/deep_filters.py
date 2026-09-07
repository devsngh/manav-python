from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deep_filters_status_type_0 import DeepFiltersStatusType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepFilters")


@_attrs_define
class DeepFilters:
    """Optional structured filters — all fields are AND-combined.

    Types match the columns they filter. Missing = don't filter.

        Attributes:
            bot_id (None | Unset | UUID):
            org_id (None | Unset | UUID):
            dept_id (None | Unset | UUID):
            user_id (None | Unset | UUID):
            date_from (datetime.datetime | None | Unset):
            date_to (datetime.datetime | None | Unset):
            status (DeepFiltersStatusType0 | None | Unset):
            span_kind (None | str | Unset): LLM/TOOL/MIDDLEWARE/COMMS/SERVER/DB/INTERNAL
            source_type (None | str | Unset): chat/social_dm/meeting/scheduled/task/…
            error_signature (None | str | Unset):
            model_id (None | str | Unset):
            resource (None | str | Unset):
            action (None | str | Unset):
            duration_min_ms (float | None | Unset):
            duration_max_ms (float | None | Unset):
            cost_min_usd (float | None | Unset):
            cost_max_usd (float | None | Unset):
    """

    bot_id: None | Unset | UUID = UNSET
    org_id: None | Unset | UUID = UNSET
    dept_id: None | Unset | UUID = UNSET
    user_id: None | Unset | UUID = UNSET
    date_from: datetime.datetime | None | Unset = UNSET
    date_to: datetime.datetime | None | Unset = UNSET
    status: DeepFiltersStatusType0 | None | Unset = UNSET
    span_kind: None | str | Unset = UNSET
    source_type: None | str | Unset = UNSET
    error_signature: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    resource: None | str | Unset = UNSET
    action: None | str | Unset = UNSET
    duration_min_ms: float | None | Unset = UNSET
    duration_max_ms: float | None | Unset = UNSET
    cost_min_usd: float | None | Unset = UNSET
    cost_max_usd: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        dept_id: None | str | Unset
        if isinstance(self.dept_id, Unset):
            dept_id = UNSET
        elif isinstance(self.dept_id, UUID):
            dept_id = str(self.dept_id)
        else:
            dept_id = self.dept_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.datetime):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.datetime):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, DeepFiltersStatusType0):
            status = self.status.value
        else:
            status = self.status

        span_kind: None | str | Unset
        if isinstance(self.span_kind, Unset):
            span_kind = UNSET
        else:
            span_kind = self.span_kind

        source_type: None | str | Unset
        if isinstance(self.source_type, Unset):
            source_type = UNSET
        else:
            source_type = self.source_type

        error_signature: None | str | Unset
        if isinstance(self.error_signature, Unset):
            error_signature = UNSET
        else:
            error_signature = self.error_signature

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        else:
            action = self.action

        duration_min_ms: float | None | Unset
        if isinstance(self.duration_min_ms, Unset):
            duration_min_ms = UNSET
        else:
            duration_min_ms = self.duration_min_ms

        duration_max_ms: float | None | Unset
        if isinstance(self.duration_max_ms, Unset):
            duration_max_ms = UNSET
        else:
            duration_max_ms = self.duration_max_ms

        cost_min_usd: float | None | Unset
        if isinstance(self.cost_min_usd, Unset):
            cost_min_usd = UNSET
        else:
            cost_min_usd = self.cost_min_usd

        cost_max_usd: float | None | Unset
        if isinstance(self.cost_max_usd, Unset):
            cost_max_usd = UNSET
        else:
            cost_max_usd = self.cost_max_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if dept_id is not UNSET:
            field_dict["dept_id"] = dept_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if status is not UNSET:
            field_dict["status"] = status
        if span_kind is not UNSET:
            field_dict["span_kind"] = span_kind
        if source_type is not UNSET:
            field_dict["source_type"] = source_type
        if error_signature is not UNSET:
            field_dict["error_signature"] = error_signature
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if resource is not UNSET:
            field_dict["resource"] = resource
        if action is not UNSET:
            field_dict["action"] = action
        if duration_min_ms is not UNSET:
            field_dict["duration_min_ms"] = duration_min_ms
        if duration_max_ms is not UNSET:
            field_dict["duration_max_ms"] = duration_max_ms
        if cost_min_usd is not UNSET:
            field_dict["cost_min_usd"] = cost_min_usd
        if cost_max_usd is not UNSET:
            field_dict["cost_max_usd"] = cost_max_usd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_dept_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dept_id_type_0 = UUID(data)

                return dept_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dept_id = _parse_dept_id(d.pop("dept_id", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_date_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = datetime.datetime.fromisoformat(data)

                return date_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = datetime.datetime.fromisoformat(data)

                return date_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_status(data: object) -> DeepFiltersStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = DeepFiltersStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepFiltersStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_span_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        span_kind = _parse_span_kind(d.pop("span_kind", UNSET))

        def _parse_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_type = _parse_source_type(d.pop("source_type", UNSET))

        def _parse_error_signature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_signature = _parse_error_signature(d.pop("error_signature", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource = _parse_resource(d.pop("resource", UNSET))

        def _parse_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        def _parse_duration_min_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_min_ms = _parse_duration_min_ms(d.pop("duration_min_ms", UNSET))

        def _parse_duration_max_ms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_max_ms = _parse_duration_max_ms(d.pop("duration_max_ms", UNSET))

        def _parse_cost_min_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_min_usd = _parse_cost_min_usd(d.pop("cost_min_usd", UNSET))

        def _parse_cost_max_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_max_usd = _parse_cost_max_usd(d.pop("cost_max_usd", UNSET))

        deep_filters = cls(
            bot_id=bot_id,
            org_id=org_id,
            dept_id=dept_id,
            user_id=user_id,
            date_from=date_from,
            date_to=date_to,
            status=status,
            span_kind=span_kind,
            source_type=source_type,
            error_signature=error_signature,
            model_id=model_id,
            resource=resource,
            action=action,
            duration_min_ms=duration_min_ms,
            duration_max_ms=duration_max_ms,
            cost_min_usd=cost_min_usd,
            cost_max_usd=cost_max_usd,
        )

        deep_filters.additional_properties = d
        return deep_filters

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
