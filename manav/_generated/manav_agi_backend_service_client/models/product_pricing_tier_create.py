from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_pricing_tier_create_limits_type_0 import ProductPricingTierCreateLimitsType0


T = TypeVar("T", bound="ProductPricingTierCreate")


@_attrs_define
class ProductPricingTierCreate:
    """
    Attributes:
        tier_name (str):
        tier_order (int):
        base_price (float | str):
        currency_id (UUID):
        billing_period (str): monthly / annual / one_time
        description (None | str | Unset):
        features (list[str] | None | Unset):
        limits (None | ProductPricingTierCreateLimitsType0 | Unset):
        is_active (bool | Unset):  Default: True.
        effective_from (datetime.date | None | Unset):
        effective_until (datetime.date | None | Unset):
    """

    tier_name: str
    tier_order: int
    base_price: float | str
    currency_id: UUID
    billing_period: str
    description: None | str | Unset = UNSET
    features: list[str] | None | Unset = UNSET
    limits: None | ProductPricingTierCreateLimitsType0 | Unset = UNSET
    is_active: bool | Unset = True
    effective_from: datetime.date | None | Unset = UNSET
    effective_until: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_pricing_tier_create_limits_type_0 import (
            ProductPricingTierCreateLimitsType0,  # noqa: PLC0415
        )

        tier_name = self.tier_name

        tier_order = self.tier_order

        base_price: float | str
        base_price = self.base_price

        currency_id = str(self.currency_id)

        billing_period = self.billing_period

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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
        elif isinstance(self.limits, ProductPricingTierCreateLimitsType0):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

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
        field_dict.update(
            {
                "tier_name": tier_name,
                "tier_order": tier_order,
                "base_price": base_price,
                "currency_id": currency_id,
                "billing_period": billing_period,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.product_pricing_tier_create_limits_type_0 import (
            ProductPricingTierCreateLimitsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        tier_name = d.pop("tier_name")

        tier_order = d.pop("tier_order")

        def _parse_base_price(data: object) -> float | str:
            return cast(float | str, data)

        base_price = _parse_base_price(d.pop("base_price"))

        currency_id = UUID(d.pop("currency_id"))

        billing_period = d.pop("billing_period")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_limits(data: object) -> None | ProductPricingTierCreateLimitsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_0 = ProductPricingTierCreateLimitsType0.from_dict(data)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductPricingTierCreateLimitsType0 | Unset, data)

        limits = _parse_limits(d.pop("limits", UNSET))

        is_active = d.pop("is_active", UNSET)

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

        product_pricing_tier_create = cls(
            tier_name=tier_name,
            tier_order=tier_order,
            base_price=base_price,
            currency_id=currency_id,
            billing_period=billing_period,
            description=description,
            features=features,
            limits=limits,
            is_active=is_active,
            effective_from=effective_from,
            effective_until=effective_until,
        )

        product_pricing_tier_create.additional_properties = d
        return product_pricing_tier_create

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
