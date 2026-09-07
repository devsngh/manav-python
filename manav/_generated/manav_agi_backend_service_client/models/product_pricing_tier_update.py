from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_pricing_tier_update_limits_type_0 import ProductPricingTierUpdateLimitsType0


T = TypeVar("T", bound="ProductPricingTierUpdate")


@_attrs_define
class ProductPricingTierUpdate:
    """
    Attributes:
        tier_name (None | str | Unset):
        tier_order (int | None | Unset):
        description (None | str | Unset):
        base_price (float | None | str | Unset):
        currency_id (None | Unset | UUID):
        billing_period (None | str | Unset):
        features (list[str] | None | Unset):
        limits (None | ProductPricingTierUpdateLimitsType0 | Unset):
        is_active (bool | None | Unset):
        effective_from (datetime.date | None | Unset):
        effective_until (datetime.date | None | Unset):
    """

    tier_name: None | str | Unset = UNSET
    tier_order: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    base_price: float | None | str | Unset = UNSET
    currency_id: None | Unset | UUID = UNSET
    billing_period: None | str | Unset = UNSET
    features: list[str] | None | Unset = UNSET
    limits: None | ProductPricingTierUpdateLimitsType0 | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    effective_from: datetime.date | None | Unset = UNSET
    effective_until: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_pricing_tier_update_limits_type_0 import (
            ProductPricingTierUpdateLimitsType0,  # noqa: PLC0415
        )

        tier_name: None | str | Unset
        if isinstance(self.tier_name, Unset):
            tier_name = UNSET
        else:
            tier_name = self.tier_name

        tier_order: int | None | Unset
        if isinstance(self.tier_order, Unset):
            tier_order = UNSET
        else:
            tier_order = self.tier_order

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        base_price: float | None | str | Unset
        if isinstance(self.base_price, Unset):
            base_price = UNSET
        else:
            base_price = self.base_price

        currency_id: None | str | Unset
        if isinstance(self.currency_id, Unset):
            currency_id = UNSET
        elif isinstance(self.currency_id, UUID):
            currency_id = str(self.currency_id)
        else:
            currency_id = self.currency_id

        billing_period: None | str | Unset
        if isinstance(self.billing_period, Unset):
            billing_period = UNSET
        else:
            billing_period = self.billing_period

        features: list[str] | None | Unset
        if isinstance(self.features, Unset):
            features = UNSET
        elif isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        limits: dict[str, Any] | None | Unset
        if isinstance(self.limits, Unset):
            limits = UNSET
        elif isinstance(self.limits, ProductPricingTierUpdateLimitsType0):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        effective_from: None | str | Unset
        if isinstance(self.effective_from, Unset):
            effective_from = UNSET
        elif isinstance(self.effective_from, datetime.date):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        effective_until: None | str | Unset
        if isinstance(self.effective_until, Unset):
            effective_until = UNSET
        elif isinstance(self.effective_until, datetime.date):
            effective_until = self.effective_until.isoformat()
        else:
            effective_until = self.effective_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tier_name is not UNSET:
            field_dict["tier_name"] = tier_name
        if tier_order is not UNSET:
            field_dict["tier_order"] = tier_order
        if description is not UNSET:
            field_dict["description"] = description
        if base_price is not UNSET:
            field_dict["base_price"] = base_price
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if billing_period is not UNSET:
            field_dict["billing_period"] = billing_period
        if features is not UNSET:
            field_dict["features"] = features
        if limits is not UNSET:
            field_dict["limits"] = limits
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if effective_until is not UNSET:
            field_dict["effective_until"] = effective_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_pricing_tier_update_limits_type_0 import (
            ProductPricingTierUpdateLimitsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_tier_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier_name = _parse_tier_name(d.pop("tier_name", UNSET))

        def _parse_tier_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tier_order = _parse_tier_order(d.pop("tier_order", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_base_price(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        base_price = _parse_base_price(d.pop("base_price", UNSET))

        def _parse_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                currency_id_type_0 = UUID(data)

                return currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        currency_id = _parse_currency_id(d.pop("currency_id", UNSET))

        def _parse_billing_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_period = _parse_billing_period(d.pop("billing_period", UNSET))

        def _parse_features(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                features_type_0 = cast(list[str], data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        features = _parse_features(d.pop("features", UNSET))

        def _parse_limits(data: object) -> None | ProductPricingTierUpdateLimitsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_0 = ProductPricingTierUpdateLimitsType0.from_dict(data)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductPricingTierUpdateLimitsType0 | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_effective_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.date.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_from = _parse_effective_from(d.pop("effective_from", UNSET))

        def _parse_effective_until(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_until_type_0 = datetime.date.fromisoformat(data)

                return effective_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_until = _parse_effective_until(d.pop("effective_until", UNSET))

        product_pricing_tier_update = cls(
            tier_name=tier_name,
            tier_order=tier_order,
            description=description,
            base_price=base_price,
            currency_id=currency_id,
            billing_period=billing_period,
            features=features,
            limits=limits,
            is_active=is_active,
            effective_from=effective_from,
            effective_until=effective_until,
        )

        product_pricing_tier_update.additional_properties = d
        return product_pricing_tier_update

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
