from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.window_usage_info import WindowUsageInfo


T = TypeVar("T", bound="TokenQuotaStatusResponse")


@_attrs_define
class TokenQuotaStatusResponse:
    """
    Attributes:
        chat_enabled (bool):
        reason (None | str | Unset):
        uses_byollm (bool | Unset):  Default: False.
        credits_available (int | Unset):  Default: 0.
        credits_low (bool | Unset):  Default: False.
        daily_token_limit (int | Unset):  Default: 0.
        daily_tokens_used (int | Unset):  Default: 0.
        daily_usage_percent (float | Unset):  Default: 0.0.
        current_window (None | Unset | WindowUsageInfo):
        next_window_at (datetime.datetime | None | Unset):
        window_hours (int | Unset):  Default: 4.
        overflow_policy (str | Unset):  Default: 'block'.
    """

    chat_enabled: bool
    reason: None | str | Unset = UNSET
    uses_byollm: bool | Unset = False
    credits_available: int | Unset = 0
    credits_low: bool | Unset = False
    daily_token_limit: int | Unset = 0
    daily_tokens_used: int | Unset = 0
    daily_usage_percent: float | Unset = 0.0
    current_window: None | Unset | WindowUsageInfo = UNSET
    next_window_at: datetime.datetime | None | Unset = UNSET
    window_hours: int | Unset = 4
    overflow_policy: str | Unset = "block"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.window_usage_info import WindowUsageInfo  # noqa: PLC0415

        chat_enabled = self.chat_enabled

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        uses_byollm = self.uses_byollm

        credits_available = self.credits_available

        credits_low = self.credits_low

        daily_token_limit = self.daily_token_limit

        daily_tokens_used = self.daily_tokens_used

        daily_usage_percent = self.daily_usage_percent

        current_window: dict[str, Any] | None | Unset
        if isinstance(self.current_window, Unset):
            current_window = UNSET
        elif isinstance(self.current_window, WindowUsageInfo):
            current_window = self.current_window.to_dict()
        else:
            current_window = self.current_window

        next_window_at: None | str | Unset
        if isinstance(self.next_window_at, Unset):
            next_window_at = UNSET
        elif isinstance(self.next_window_at, datetime.datetime):
            next_window_at = self.next_window_at.isoformat()
        else:
            next_window_at = self.next_window_at

        window_hours = self.window_hours

        overflow_policy = self.overflow_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chat_enabled": chat_enabled,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if uses_byollm is not UNSET:
            field_dict["uses_byollm"] = uses_byollm
        if credits_available is not UNSET:
            field_dict["credits_available"] = credits_available
        if credits_low is not UNSET:
            field_dict["credits_low"] = credits_low
        if daily_token_limit is not UNSET:
            field_dict["daily_token_limit"] = daily_token_limit
        if daily_tokens_used is not UNSET:
            field_dict["daily_tokens_used"] = daily_tokens_used
        if daily_usage_percent is not UNSET:
            field_dict["daily_usage_percent"] = daily_usage_percent
        if current_window is not UNSET:
            field_dict["current_window"] = current_window
        if next_window_at is not UNSET:
            field_dict["next_window_at"] = next_window_at
        if window_hours is not UNSET:
            field_dict["window_hours"] = window_hours
        if overflow_policy is not UNSET:
            field_dict["overflow_policy"] = overflow_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.window_usage_info import WindowUsageInfo  # noqa: PLC0415

        d = dict(src_dict)
        chat_enabled = d.pop("chat_enabled")

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        uses_byollm = d.pop("uses_byollm", UNSET)

        credits_available = d.pop("credits_available", UNSET)

        credits_low = d.pop("credits_low", UNSET)

        daily_token_limit = d.pop("daily_token_limit", UNSET)

        daily_tokens_used = d.pop("daily_tokens_used", UNSET)

        daily_usage_percent = d.pop("daily_usage_percent", UNSET)

        def _parse_current_window(data: object) -> None | Unset | WindowUsageInfo:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_window_type_0 = WindowUsageInfo.from_dict(data)

                return current_window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WindowUsageInfo, data)

        current_window = _parse_current_window(d.pop("current_window", UNSET))

        def _parse_next_window_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_window_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_window_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_window_at = _parse_next_window_at(d.pop("next_window_at", UNSET))

        window_hours = d.pop("window_hours", UNSET)

        overflow_policy = d.pop("overflow_policy", UNSET)

        token_quota_status_response = cls(
            chat_enabled=chat_enabled,
            reason=reason,
            uses_byollm=uses_byollm,
            credits_available=credits_available,
            credits_low=credits_low,
            daily_token_limit=daily_token_limit,
            daily_tokens_used=daily_tokens_used,
            daily_usage_percent=daily_usage_percent,
            current_window=current_window,
            next_window_at=next_window_at,
            window_hours=window_hours,
            overflow_policy=overflow_policy,
        )

        token_quota_status_response.additional_properties = d
        return token_quota_status_response

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
