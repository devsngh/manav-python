from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_pricing_tier_response_limits_type_0 import ProductPricingTierResponseLimitsType0


T = TypeVar("T", bound="ProductPricingTierResponse")


@_attrs_define
class ProductPricingTierResponse:
    """
    Attributes:
        id (UUID):
        product_id (UUID):
        tier_name (str):
        tier_order (int):
        description (None | str):
        base_price (str):
        currency_id (UUID):
        billing_period (str):
        features (list[str] | None):
        limits (None | ProductPricingTierResponseLimitsType0):
        is_active (bool):
        effective_from (datetime.date | None):
        effective_until (datetime.date | None):
        authored_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    product_id: UUID
    tier_name: str
    tier_order: int
    description: None | str
    base_price: str
    currency_id: UUID
    billing_period: str
    features: list[str] | None
    limits: None | ProductPricingTierResponseLimitsType0
    is_active: bool
    effective_from: datetime.date | None
    effective_until: datetime.date | None
    authored_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_pricing_tier_response_limits_type_0 import (
            ProductPricingTierResponseLimitsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        product_id = str(self.product_id)

        tier_name = self.tier_name

        tier_order = self.tier_order

        description: None | str
        description = self.description

        base_price = self.base_price

        currency_id = str(self.currency_id)

        billing_period = self.billing_period

        features: list[str] | None
        if isinstance(self.features, list):
            features = self.features

        else:
            features = self.features

        limits: dict[str, Any] | None
        if isinstance(self.limits, ProductPricingTierResponseLimitsType0):
            limits = self.limits.to_dict()
        else:
            limits = self.limits

        is_active = self.is_active

        effective_from: None | str
        if isinstance(self.effective_from, datetime.date):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        effective_until: None | str
        if isinstance(self.effective_until, datetime.date):
            effective_until = self.effective_until.isoformat()
        else:
            effective_until = self.effective_until

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product_id": product_id,
                "tier_name": tier_name,
                "tier_order": tier_order,
                "description": description,
                "base_price": base_price,
                "currency_id": currency_id,
                "billing_period": billing_period,
                "features": features,
                "limits": limits,
                "is_active": is_active,
                "effective_from": effective_from,
                "effective_until": effective_until,
                "authored_by_bot_id": authored_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_pricing_tier_response_limits_type_0 import (
            ProductPricingTierResponseLimitsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        product_id = UUID(d.pop("product_id"))

        tier_name = d.pop("tier_name")

        tier_order = d.pop("tier_order")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        base_price = d.pop("base_price")

        currency_id = UUID(d.pop("currency_id"))

        billing_period = d.pop("billing_period")

        def _parse_features(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                features_type_0 = cast(list[str], data)

                return features_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        features = _parse_features(d.pop("features"))

        def _parse_limits(data: object) -> None | ProductPricingTierResponseLimitsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                limits_type_0 = ProductPricingTierResponseLimitsType0.from_dict(data)

                return limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductPricingTierResponseLimitsType0, data)

        limits = _parse_limits(d.pop("limits"))

        is_active = d.pop("is_active")

        def _parse_effective_from(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.date.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        effective_from = _parse_effective_from(d.pop("effective_from"))

        def _parse_effective_until(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_until_type_0 = datetime.date.fromisoformat(data)

                return effective_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        effective_until = _parse_effective_until(d.pop("effective_until"))

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

        product_pricing_tier_response = cls(
            id=id,
            product_id=product_id,
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
            authored_by_bot_id=authored_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        product_pricing_tier_response.additional_properties = d
        return product_pricing_tier_response

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
